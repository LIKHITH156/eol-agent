"""
EOL Agent — CLI Runner  v3.0
Uses ThreadPoolExecutor for parallel device lookups (5-10x faster).

Usage (demo mode):
    python run_agent.py

Usage (with ServiceNow):
    python run_agent.py --snow --url https://yourco.service-now.com --user api_user --password secret

Usage (with live web scraping):
    python run_agent.py --live
"""

import sys
import os
import argparse
import threading
from datetime import date
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load .env if present
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

sys.path.insert(0, os.path.dirname(__file__))

from core.models     import EOLStatus
from core.servicenow import ServiceNowConnector, get_sample_devices
from core.researcher import EOLResearcher
from core.analyser   import EOLAnalyser
from core.cache      import save_scan, result_to_dict
from reports.excel_report import ExcelReportGenerator


RESET  = "\033[0m";  BOLD  = "\033[1m"
RED    = "\033[31m"; YELLOW = "\033[33m"
GREEN  = "\033[32m"; CYAN  = "\033[36m"
WHITE  = "\033[97m"

def hdr(msg):  print(f"\n{BOLD}{CYAN}{'─'*60}{RESET}\n{BOLD}{WHITE}  {msg}{RESET}\n{'─'*60}")
def ok(msg):   print(f"  {GREEN}✔  {msg}{RESET}")
def warn(msg): print(f"  {YELLOW}⚠  {msg}{RESET}")
def err(msg):  print(f"  {RED}✖  {msg}{RESET}")


# ── Parallel analysis ─────────────────────────────────────────── #

def run_parallel(devices, use_web: bool = False) -> list:
    total   = len(devices)
    ordered = [None] * total
    counter = [0]
    lock    = threading.Lock()
    workers = 4 if use_web else 15

    def analyse(item):
        idx, device = item
        result = EOLAnalyser(EOLResearcher(use_web=use_web)).analyse_one(device)
        with lock:
            ordered[idx] = result
            counter[0]  += 1
            status_col = (RED if result.status in (EOLStatus.EXPIRED, EOLStatus.CRITICAL)
                          else YELLOW if result.status in (EOLStatus.WARNING, EOLStatus.MONITOR)
                          else GREEN)
            print(f"  [{counter[0]:>3}/{total}] {device.part_code:<28} "
                  f"{status_col}{result.status.value}{RESET}")
        return result

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(analyse, (i, d)): i for i, d in enumerate(devices)}
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as exc:
                err(f"Device {futures[future]}: {exc}")

    return [r for r in ordered if r is not None]


# ─────────────────────────────────────────────────────────────── #

def run(args):
    hdr("Network EOL Intelligence Agent v3.0 — Starting")

    # ── Step 1: Pull devices ─────────────────────────────── #
    hdr("Step 1 — Loading Device Inventory")

    connector = None
    if args.snow:
        ok(f"Connecting to ServiceNow: {args.url}")
        connector = ServiceNowConnector(args.url, args.user, args.password, table=args.table)
        test = connector.test_connection()
        if test["status"] != "ok":
            err(f"ServiceNow connection failed: {test['message']}")
            sys.exit(1)
        ok("ServiceNow connection verified")
        devices = connector.get_network_devices(limit=args.limit)
    else:
        warn("Demo mode — using built-in sample inventory")
        warn("Add --snow --url ... --user ... --password ... to use your CMDB")
        devices = get_sample_devices()

    ok(f"Loaded {len(devices)} devices")

    # ── Step 2: Parallel EOL Research & Analysis ──────────── #
    hdr(f"Step 2 — EOL Research & Analysis  (parallel, {'live web' if args.live else 'local DB'})")

    results = run_parallel(devices, use_web=args.live)

    at_risk, safe = EOLAnalyser.split_results(results)
    stats         = EOLAnalyser.summary_stats(results)

    # ── Step 3: Console summary ───────────────────────────── #
    hdr("Step 3 — Analysis Summary")
    print(f"""
  Total devices analysed  : {stats['total']}
  ──────────────────────────────────────
  {RED}EOL/EOS — Expired       : {stats['expired']}{RESET}
  {RED}Critical  (<6 months)   : {stats['critical']}{RESET}
  {YELLOW}Warning   (6–12 months) : {stats['warning']}{RESET}
  {YELLOW}Monitor   (12–24 months): {stats['monitor']}{RESET}
  {GREEN}Safe      (2+ years)    : {stats['safe']}{RESET}
  Unknown / not found     : {stats['unknown']}
    """)

    if at_risk:
        print(f"  {BOLD}⚠  Top At-Risk Devices:{RESET}")
        for r in at_risk[:10]:
            days_txt = f"{r.days_left}d" if r.days_left is not None else "—"
            repl     = r.eol.replacement_sku if r.eol and r.eol.replacement_sku else "—"
            colour   = RED if r.status in (EOLStatus.EXPIRED, EOLStatus.CRITICAL) else YELLOW
            print(f"  {colour}  {r.device.part_code:<28} {r.status.value:<30} "
                  f"({days_txt:>8})  → {repl}{RESET}")

    # ── Step 4: Save to SQLite history ───────────────────── #
    at_risk_json = [result_to_dict(r) for r in at_risk]
    safe_json    = [result_to_dict(r) for r in safe]
    save_scan("snow" if args.snow else "sample", len(results), stats, at_risk_json, safe_json)
    ok("Scan saved to history database")

    # ── Step 5: ServiceNow write-back (optional) ──────────── #
    if args.snow and args.writeback and connector:
        hdr("Step 5 — Writing EOL Status back to ServiceNow CMDB")
        updated = 0
        for r in results:
            repl = (r.eol.replacement_sku if r.eol else "") or ""
            if connector.update_eol_status(r.device.sys_id, r.status.value, repl):
                updated += 1
        ok(f"Updated {updated}/{len(results)} CI records in ServiceNow")

    # ── Step 6: Excel report ──────────────────────────────── #
    hdr("Step 6 — Generating Excel Report")

    output_dir  = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(output_dir, exist_ok=True)
    report_name = f"network_eol_report_{date.today().strftime('%Y%m%d')}.xlsx"
    report_path = os.path.join(output_dir, report_name)

    ExcelReportGenerator(report_path).generate(at_risk, safe, stats, generated_by="EOL Agent v3.0")

    ok(f"Report saved → {report_path}")
    ok(f"Sheet 1 (At-Risk): {len(at_risk)} devices")
    ok(f"Sheet 2 (Safe):    {len(safe)} devices")
    ok(f"Sheet 3: Executive Summary + Chart")

    hdr("Done ✔")
    return report_path


def parse_args():
    p = argparse.ArgumentParser(description="Network EOL Intelligence Agent v3.0")
    p.add_argument("--snow",      action="store_true", help="Connect to ServiceNow CMDB")
    p.add_argument("--url",       default=os.environ.get("SNOW_URL", ""))
    p.add_argument("--user",      default=os.environ.get("SNOW_USER", ""))
    p.add_argument("--password",  default=os.environ.get("SNOW_PASSWORD", ""))
    p.add_argument("--table",     default=os.environ.get("SNOW_TABLE", "cmdb_ci_netgear"))
    p.add_argument("--limit",     type=int, default=1000)
    p.add_argument("--writeback", action="store_true", help="Write EOL status back to ServiceNow")
    p.add_argument("--live",      action="store_true", help="Enable live vendor portal scraping")
    return p.parse_args()


if __name__ == "__main__":
    args = parse_args()
    path = run(args)
    print(f"\n  Report: {path}\n")
