"""
EOL Agent — Flask API Server  v3.0
Improvements over v2:
  - SQLite persistence: scan results survive server restarts
  - Parallel device processing (ThreadPoolExecutor)
  - Server-Sent Events (SSE) for real-time scan progress
  - Scan history endpoint
  - .env config support
  - Date validation on all scraped data
"""

import sys
import os
import io
import json
import time
import threading
import traceback
from datetime import date, datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from flask import Flask, jsonify, request, send_file, Response
from flask_cors import CORS

# Load .env if present
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

sys.path.insert(0, os.path.dirname(__file__))

from core.models     import EOLStatus
from core.servicenow import ServiceNowConnector, get_sample_devices
from core.researcher import EOLResearcher, infer_vendor, clear_html_cache
from core.analyser   import EOLAnalyser
from core.live_scraper import fetch_live, VENDOR_FETCHERS
from core.cache      import (
    save_scan, get_latest_scan, get_scan_history,
    result_to_dict, dict_to_result,
)
from reports.excel_report import ExcelReportGenerator

app = Flask(__name__, static_folder="frontend", static_url_path="")
CORS(app)

PORT = int(os.environ.get("PORT", os.environ.get("FLASK_PORT", 8080)))

# ── In-memory state ───────────────────────────────────────────── #
_state = {
    "snow_config":    None,
    "devices":        [],
    "results":        [],        # AnalysisResult objects (in-memory)
    "scan_running":   False,
    "scan_log":       [],
    "scan_done":      False,
    "scan_source":    "sample",
    "scan_total":     0,
    # Excel upload state
    "excel_loaded":   False,
    "excel_filename": "",
    "excel_count":    0,
    "excel_preview":  [],        # first 5 rows for preview
    # Persisted (loaded from SQLite on startup)
    "last_at_risk":  [],
    "last_safe":     [],
    "last_stats":    {},
}
_state_lock = threading.Lock()


def _log(msg: str):
    with _state_lock:
        _state["scan_log"].append(msg)
    print(msg)


# ── Startup: restore last scan from SQLite ────────────────────── #

def _restore_last_scan():
    scan = get_latest_scan()
    if scan:
        _state["last_at_risk"] = scan["at_risk"]
        _state["last_safe"]    = scan["safe"]
        _state["last_stats"]   = scan["stats"]
        _state["scan_done"]    = True
        print(f"[Startup] Restored last scan ({scan['device_count']} devices, {scan['run_at'][:10]})")

_restore_last_scan()

# ── Pre-configure from env if present ────────────────────────── #
if os.environ.get("SNOW_URL"):
    _state["snow_config"] = {
        "url":   os.environ["SNOW_URL"],
        "user":  os.environ.get("SNOW_USER", ""),
        "pwd":   os.environ.get("SNOW_PASSWORD", ""),
        "table": os.environ.get("SNOW_TABLE", "cmdb_ci_netgear"),
    }


# ─────────────────────────────────────────────────────────────── #
#  Helpers                                                         #
# ─────────────────────────────────────────────────────────────── #

def _device_to_dict(d):
    return {
        "sys_id":      d.sys_id,    "name":        d.name,
        "part_code":   d.part_code, "vendor":      d.vendor,
        "model":       d.model,     "serial":      d.serial,
        "ip_address":  d.ip_address,"location":    d.location,
        "assigned_to": d.assigned_to,"quantity":   d.quantity,
    }

def _current_status_payload(include_results: bool = False) -> dict:
    with _state_lock:
        results    = list(_state["results"])
        running    = _state["scan_running"]
        done       = _state["scan_done"]
        log        = list(_state["scan_log"][-30:])
        scan_total = _state["scan_total"]   # set at scan start, never changes mid-scan

    if results:
        at_risk = [result_to_dict(r) for r in results if r.is_at_risk]
        safe    = [result_to_dict(r) for r in results if r.is_safe]
        stats   = EOLAnalyser.summary_stats(results)
    else:
        at_risk = _state["last_at_risk"]
        safe    = _state["last_safe"]
        stats   = _state["last_stats"]

    payload = {
        "running":   running,
        "done":      done,
        "processed": len(results),
        "total":     scan_total,
        "log":       log,
        "stats":     stats,
    }
    if include_results or done:
        payload["at_risk"] = at_risk
        payload["safe"]    = safe
    return payload


# ─────────────────────────────────────────────────────────────── #
#  Routes                                                          #
# ─────────────────────────────────────────────────────────────── #

@app.route("/")
def index():
    return send_file("frontend/index.html")


@app.route("/api/status")
def status():
    return jsonify({
        "status":          "running",
        "version":         "3.0",
        "vendors":         list(VENDOR_FETCHERS.keys()),
        "devices_loaded":  len(_state["devices"]),
        "scan_done":       _state["scan_done"],
    })


@app.route("/api/vendors")
def vendors():
    return jsonify({"vendors": [
        {"name": "Cisco",            "portal": "https://api.cisco.com/supporttools/eox",                          "type": "REST API"},
        {"name": "Juniper",          "portal": "https://support.juniper.net/support/eol/hardware/",               "type": "HTML Table"},
        {"name": "HP Aruba",         "portal": "https://www.arubanetworks.com/support-services/end-of-life/",     "type": "HTML Table"},
        {"name": "Arista",           "portal": "https://www.arista.com/en/support/product-lifecycle",             "type": "JSON + HTML"},
        {"name": "Dell",             "portal": "https://www.dell.com/en-us/dt/corporate/about-us/end-of-life-notices.htm", "type": "HTML Table"},
        {"name": "Fortinet",         "portal": "https://endoflife.date/api/fortigate.json",                       "type": "REST API"},
        {"name": "Palo Alto",        "portal": "https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware", "type": "HTML Table"},
        {"name": "Extreme Networks", "portal": "https://www.extremenetworks.com/support/end-of-life/",            "type": "HTML Table"},
        {"name": "Cisco Meraki",     "portal": "https://endoflife.date/api/cisco-meraki-mr.json",                 "type": "endoflife.date (free)"},
        {"name": "Starlink",         "portal": "https://www.starlink.com/hardware",                               "type": "Web Scrape"},
    ]})


# ── ServiceNow ───────────────────────────────────────────────── #

@app.route("/api/connect/servicenow", methods=["POST"])
def connect_snow():
    body  = request.json or {}
    url   = body.get("url", "").strip()
    user  = body.get("username", "").strip()
    pwd   = body.get("password", "").strip()
    table = body.get("table", "cmdb_ci_netgear")
    if not (url and user and pwd):
        return jsonify({"status": "error", "message": "url, username and password are required"}), 400
    try:
        conn = ServiceNowConnector(url, user, pwd, table=table)
        test = conn.test_connection()
        if test["status"] != "ok":
            return jsonify({"status": "error", "message": test.get("message", "Connection failed")}), 400
        _state["snow_config"] = {"url": url, "user": user, "pwd": pwd, "table": table}
        return jsonify({"status": "ok", "message": "ServiceNow connected successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# ── Excel file upload ─────────────────────────────────────────── #

# Column name variants to search (case-insensitive).
# More-specific / longer strings must come BEFORE short ones so exact
# and partial matching don't grab the wrong column.
_COL_VARIANTS = {
    "model_id":    ["asset type model", "model id", "model_id", "modelid",
                    "model number", "model no", "part code", "part no",
                    "partcode", "part_code", "model"],
    "asset":       ["asset tag", "asset number", "asset no",
                    "asset ib item id", "asset request id", "asset"],
    "vendor":      ["manufacturer", "vendor", "mfr", "make"],
    "serial":      ["serial number", "serial no", "serial", "s/n", "sn"],
    # hostname/host name before bare "name" so "Client Name" doesn't
    # accidentally become the device display name.
    # "asset type" is last-resort fallback when no hostname column exists.
    "name":        ["host name", "hostname", "dnsname", "dns name",
                    "device name", "display name", "asset type"],
    "hostname":    ["host name", "hostname", "dnsname", "dns name"],
    "ip":          ["management ip address", "management ip",
                    "ip address", "mgmt ip", "ip"],
    "location":    ["site ref", "site name", "site", "location"],
    "city":        ["city"],
    "country":     ["country"],
    # "client name" is the primary fallback when no dedicated "company" column exists
    "company":     ["client name", "client", "company", "customer",
                    "account name", "organisation", "organization"],
    "owner":       ["hardware maintained by", "h w maintained by",
                    "hw maintained by", "owner", "assigned to"],
    "hw_status":   ["hardware status", "hw status", "asset type status"],
    "op_status":   ["operational status", "op status"],
    "existing_eol":["eol status", "eol"],
    "existing_eos":["eos date", "eol date", "end of sale", "end of life"],
    "ios_version": ["ios version", "firmware version", "software version"],
    "contract":    ["cisco contract number", "contract number", "contract"],
}


def _find_col_idx(headers_lower: list, variants: list) -> int | None:
    for v in variants:
        try:
            return headers_lower.index(v.lower())
        except ValueError:
            pass
    # partial match fallback
    for i, h in enumerate(headers_lower):
        if any(v.lower() in h for v in variants):
            return i
    return None


def _cell(row, idx, default=""):
    if idx is None or idx >= len(row):
        return default
    v = row[idx].value
    return str(v).strip() if v is not None else default


@app.route("/api/upload/excel", methods=["POST"])
def upload_excel():
    if "file" not in request.files:
        return jsonify({"status": "error", "message": "No file part in request"}), 400

    f = request.files["file"]
    if not f.filename:
        return jsonify({"status": "error", "message": "No file selected"}), 400
    if not f.filename.lower().endswith((".xlsx", ".xls")):
        return jsonify({"status": "error", "message": "Only .xlsx / .xls files are supported"}), 400

    try:
        import openpyxl
        data = f.read()
        wb   = openpyxl.load_workbook(io.BytesIO(data), read_only=True, data_only=True)
        ws   = wb.active

        rows = list(ws.iter_rows())
        if not rows:
            return jsonify({"status": "error", "message": "Excel file is empty"}), 400

        # ── Auto-detect header row (scan first 10 rows) ───────────
        # Files often have title/banner rows before the real header.
        # Score by counting cells whose text CONTAINS a known variant (one direction
        # only — avoids short data-cell values falsely matching long variant strings).
        all_variants_flat = [v.lower() for variants in _COL_VARIANTS.values() for v in variants]

        header_row_idx = 0
        best_score     = 0
        for i, row in enumerate(rows[:10]):
            cells = [str(c.value or "").strip().lower() for c in row]
            score = sum(1 for c in cells if c and any(v in c for v in all_variants_flat))
            if score > best_score:
                best_score     = score
                header_row_idx = i

        raw_headers   = [str(c.value or "").strip() for c in rows[header_row_idx]]
        headers_lower = [h.lower() for h in raw_headers]
        data_rows     = rows[header_row_idx + 1:]

        col = {k: _find_col_idx(headers_lower, variants)
               for k, variants in _COL_VARIANTS.items()}

        # ── Explicit overrides (run after generic matching) ────────
        # These guarantee specific column names from this file format are
        # always found even if variant matching misses them.
        def _exact(names):
            for n in names:
                if n in headers_lower:
                    return headers_lower.index(n)
            return None

        # "Client Name" → company  (must always win)
        _client_col = _exact(["client name", "client_name"])
        if _client_col is not None:
            col["company"] = _client_col

        # "Host Name" / "DNSName" → primary device name
        _host_col = _exact(["host name", "hostname", "dnsname", "dns name"])
        if _host_col is not None:
            col["hostname"] = _host_col
            col["name"]     = _host_col

        # "Asset Type" → device name fallback (used when host name cell is empty)
        col["asset_type_col"] = _exact(["asset type"])

        # "Asset Type Model" → model_id
        _model_col = _exact(["asset type model", "asset_type_model"])
        if _model_col is not None:
            col["model_id"] = _model_col

        # "Site Name" → location
        _site_col = _exact(["site name", "site_name"])
        if _site_col is not None:
            col["location"] = _site_col

        # ── Conflict guard ────────────────────────────────────────
        # company column must NEVER be reused as device name
        company_col = col.get("company")
        if company_col is not None:
            if col.get("name")         == company_col:
                col["name"]         = None
            if col.get("hostname")     == company_col:
                col["hostname"]     = None
            if col.get("asset_type_col") == company_col:
                col["asset_type_col"] = None

        # If no dedicated name column at all, promote Asset Type as primary name
        if col.get("name") is None and col.get("hostname") is None:
            col["name"] = col.get("asset_type_col")

        if col["model_id"] is None:
            return jsonify({
                "status":  "error",
                "message": (f"Could not find a 'Model ID' / 'Asset Type Model' column. "
                            f"Header row detected at row {header_row_idx + 1}. "
                            f"Columns found: {', '.join(h for h in raw_headers if h)[:200]}"),
            }), 400

        # ── Build Device objects ──────────────────────────────────
        from core.models import Device
        devices  = []
        skipped  = 0
        preview  = []   # first 5 valid rows for UI preview

        for row_idx, row in enumerate(data_rows, start=header_row_idx + 2):
            # Use Model ID only — Vendor column contains 3rd-party IT vendor, not hardware maker
            part_code = _cell(row, col["model_id"]).upper().strip()
            if not part_code or part_code in ("NONE", "N/A", "-", "NA", "NULL"):
                skipped += 1
                continue

            vendor_hint = infer_vendor(part_code)

            # Device name: hostname > name > Asset Type > row number
            name = (_cell(row, col["hostname"])
                    or _cell(row, col["name"])
                    or _cell(row, col.get("asset_type_col"))
                    or f"Row-{row_idx}")

            # Company: dedicated company/client column, else fall back to "Client Name"
            # _find_col_idx already maps "client name" → col["company"], but if the
            # file has neither, col["company"] is None and _cell returns "".
            company_val = _cell(row, col["company"])

            location_parts = list(filter(None, [
                company_val,
                _cell(row, col["location"]),
                _cell(row, col["city"]),
                _cell(row, col["country"]),
            ]))
            location = " | ".join(location_parts) or ""

            dev = Device(
                sys_id     = f"xlsx-{row_idx}",
                name       = name,
                part_code  = part_code,
                vendor     = vendor_hint,
                model      = part_code,
                serial     = _cell(row, col["serial"]),
                ip_address = _cell(row, col["ip"]),
                location   = location,
                assigned_to= (_cell(row, col["owner"]) or ""),
            )
            devices.append(dev)

            # Build preview row (first 5 devices)
            if len(preview) < 5:
                preview.append({
                    "row":          row_idx,
                    "model_id":     part_code,
                    "name":         name,
                    "vendor":       vendor_hint,
                    "serial":       dev.serial,
                    "ip":           dev.ip_address,
                    "location":     location,
                    "existing_eol": _cell(row, col["existing_eol"]),
                    "existing_eos": _cell(row, col["existing_eos"]),
                    "ios_version":  _cell(row, col["ios_version"]),
                    "hw_status":    _cell(row, col["hw_status"]),
                    "op_status":    _cell(row, col["op_status"]),
                })

        if not devices:
            return jsonify({
                "status": "error",
                "message": f"No valid devices found (all {skipped} rows had empty Model ID)",
            }), 400

        # ── Store in state ────────────────────────────────────────
        with _state_lock:
            _state["devices"]        = devices
            _state["excel_loaded"]   = True
            _state["excel_filename"] = f.filename
            _state["excel_count"]    = len(devices)
            _state["excel_preview"]  = preview
            _state["scan_source"]    = "excel"

        # ── Report which columns were detected ────────────────────
        detected = {k: raw_headers[v] for k, v in col.items() if v is not None}

        # Key field summary for easy debugging
        _name_col = col.get("hostname") or col.get("name") or col.get("asset_type_col")
        key_mappings = {
            "Model ID   →": raw_headers[col["model_id"]]  if col.get("model_id")       is not None else "NOT FOUND",
            "Company    →": raw_headers[col["company"]]   if col.get("company")        is not None else "NOT FOUND",
            "Device Name→": raw_headers[_name_col]        if _name_col                 is not None else "NOT FOUND",
            "Location   →": raw_headers[col["location"]]  if col.get("location")       is not None else "NOT FOUND",
            "Asset Type →": raw_headers[col["asset_type_col"]] if col.get("asset_type_col") is not None else "—",
        }
        mapping_summary = "  |  ".join(f"{k} {v}" for k, v in key_mappings.items())

        return jsonify({
            "status":    "ok",
            "message":   f"Loaded {len(devices)} devices from '{f.filename}' ({skipped} rows skipped). Mappings: {mapping_summary}",
            "count":     len(devices),
            "skipped":   skipped,
            "filename":  f.filename,
            "detected_columns": detected,
            "preview":   preview,
        })

    except Exception as e:
        return jsonify({"status": "error", "message": f"Parse error: {e}"}), 500


@app.route("/api/upload/status")
def upload_status():
    return jsonify({
        "loaded":   _state["excel_loaded"],
        "filename": _state["excel_filename"],
        "count":    _state["excel_count"],
        "preview":  _state["excel_preview"],
    })


# ── Device loading ────────────────────────────────────────────── #

@app.route("/api/devices", methods=["GET"])
def get_devices():
    source = request.args.get("source", "auto")
    if source == "snow" or (source == "auto" and _state["snow_config"]):
        cfg = _state["snow_config"]
        if not cfg:
            return jsonify({"status": "error", "message": "ServiceNow not connected"}), 400
        try:
            conn    = ServiceNowConnector(cfg["url"], cfg["user"], cfg["pwd"], table=cfg["table"])
            devices = conn.get_network_devices()
            _state["devices"] = devices
            return jsonify({"status": "ok", "source": "servicenow", "count": len(devices),
                            "devices": [_device_to_dict(d) for d in devices]})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
    else:
        devices = get_sample_devices()
        _state["devices"] = devices
        return jsonify({"status": "ok", "source": "sample", "count": len(devices),
                        "devices": [_device_to_dict(d) for d in devices]})


# ── Live single-part lookup ───────────────────────────────────── #

@app.route("/api/lookup", methods=["POST"])
def lookup_part():
    body      = request.json or {}
    part_code = body.get("part_code", "").strip()
    vendor    = body.get("vendor", "").strip() or infer_vendor(part_code)
    if not part_code:
        return jsonify({"status": "error", "message": "part_code is required"}), 400

    _log(f"[lookup] {part_code} ({vendor})")
    eol = fetch_live(part_code, vendor)
    if not eol or (not eol.end_of_sale and not eol.end_of_support):
        from core.eol_database import lookup_local
        eol = lookup_local(part_code.upper())
        source_type = "local-db"
    else:
        source_type = eol.confidence

    if not eol:
        return jsonify({"status": "not_found", "part_code": part_code, "vendor": vendor,
                        "message": "Could not find EOL data for this part code", "source": "none"})

    return jsonify({
        "status":    "ok",
        "part_code": part_code,
        "vendor":    vendor,
        "source":    source_type,
        "eol": {
            "model":            eol.model,
            "end_of_sale":      eol.end_of_sale.isoformat()    if eol.end_of_sale    else None,
            "end_of_support":   eol.end_of_support.isoformat() if eol.end_of_support else None,
            "end_of_sw_maint":  eol.end_of_sw_maint.isoformat() if eol.end_of_sw_maint else None,
            "replacement_sku":  eol.replacement_sku,
            "replacement_name": eol.replacement_name,
            "migration_url":    eol.migration_url,
            "source_url":       eol.source_url,
            "confidence":       eol.confidence,
        },
    })


# ── Full analysis (parallel, async background) ────────────────── #

@app.route("/api/analyse", methods=["POST"])
def run_analysis():
    if _state["scan_running"]:
        return jsonify({"status": "already_running"}), 409

    body     = request.json or {}
    source   = body.get("source", "sample")
    use_live = body.get("use_live", False)

    if source == "snow" and _state["snow_config"]:
        cfg     = _state["snow_config"]
        conn    = ServiceNowConnector(cfg["url"], cfg["user"], cfg["pwd"], table=cfg["table"])
        devices = conn.get_network_devices()
    elif source == "excel" and _state["excel_loaded"] and _state["devices"]:
        devices = _state["devices"]   # already parsed from uploaded file
    else:
        devices = get_sample_devices()

    with _state_lock:
        _state["devices"]      = devices
        _state["results"]      = []
        _state["scan_log"]     = []
        _state["scan_running"] = True
        _state["scan_done"]    = False
        _state["scan_source"]  = source
        _state["scan_total"]   = len(devices)

    def _run():
        clear_html_cache()   # reset shared vendor-page HTML cache for this scan
        total = len(devices)
        ordered = [None] * total
        # More workers for local-DB mode (no network); fewer for live web (rate limiting)
        workers = 4 if use_live else 15

        def analyse_one(args):
            idx, device = args
            researcher = EOLResearcher(use_web=use_live)
            analyser   = EOLAnalyser(researcher)
            result     = analyser.analyse_one(device)
            with _state_lock:
                ordered[idx] = result
                # provide unordered live progress
                _state["results"] = [r for r in ordered if r is not None]
                done_count = len(_state["results"])
                _state["scan_log"].append(
                    f"[{done_count}/{total}] {device.part_code} ({device.vendor}) -> {result.status.value}"
                )
            return result

        try:
            with ThreadPoolExecutor(max_workers=workers) as executor:
                futures = {executor.submit(analyse_one, (i, d)): i
                           for i, d in enumerate(devices)}
                for future in as_completed(futures):
                    try:
                        future.result()
                    except Exception as exc:
                        _log(f"[ERROR] device {futures[future]}: {exc}")

            # Final ordered results
            final = [r for r in ordered if r is not None]
            with _state_lock:
                _state["results"]  = final
                _state["scan_done"] = True

            # Persist to SQLite
            at_risk = [result_to_dict(r) for r in final if r.is_at_risk]
            safe    = [result_to_dict(r) for r in final if r.is_safe]
            stats   = EOLAnalyser.summary_stats(final)
            save_scan(source, len(final), stats, at_risk, safe)
            with _state_lock:
                _state["last_at_risk"] = at_risk
                _state["last_safe"]    = safe
                _state["last_stats"]   = stats

            print(f"[Scan] Complete - {len(final)} devices, "
                  f"{stats['expired']} expired, {stats['critical']} critical")

        except Exception:
            _log(f"[FATAL] {traceback.format_exc()}")
        finally:
            with _state_lock:
                _state["scan_running"] = False

    threading.Thread(target=_run, daemon=True).start()
    return jsonify({"status": "started", "total": len(devices)})


# ── SSE: real-time scan progress ──────────────────────────────── #

@app.route("/api/analyse/stream")
def stream_analysis():
    """Server-Sent Events endpoint — replaces polling."""
    def generate():
        # If scan already finished, send one event and close
        if not _state["scan_running"] and _state["scan_done"]:
            payload = _current_status_payload(include_results=True)
            yield f"data: {json.dumps(payload)}\n\n"
            return

        # Stream updates until done
        while _state["scan_running"] or not _state["scan_done"]:
            payload = _current_status_payload(include_results=False)
            yield f"data: {json.dumps(payload)}\n\n"
            time.sleep(0.7)
            if _state["scan_done"]:
                break

        # Final event with full results
        payload = _current_status_payload(include_results=True)
        yield f"data: {json.dumps(payload)}\n\n"

    return Response(
        generate(),
        mimetype="text/event-stream",
        headers={
            "Cache-Control":    "no-cache",
            "X-Accel-Buffering":"no",
            "Connection":       "keep-alive",
        },
    )


# ── Polling fallback (kept for compatibility) ─────────────────── #

@app.route("/api/analyse/status")
def analysis_status():
    return jsonify(_current_status_payload(include_results=True))


# ── Scan history ──────────────────────────────────────────────── #

@app.route("/api/scans/history")
def scans_history():
    limit = int(request.args.get("limit", 20))
    scans = get_scan_history(limit)
    return jsonify({"scans": scans})


# ── Excel report ──────────────────────────────────────────────── #

@app.route("/api/report/excel")
def download_excel():
    vendor_filter  = request.args.get("vendor",  "").strip()
    company_filter = request.args.get("company", "").strip()

    def _company_of(d) -> str:
        """Extract company name: first segment of 'Company | Site | City | Country'."""
        loc = (d.device.location if hasattr(d, "device") else
               (d.get("device") or {}).get("location") or "")
        return (loc or "").split(" | ")[0].strip()

    def _matches(r) -> bool:
        if vendor_filter  and r.device.vendor != vendor_filter:
            return False
        if company_filter and _company_of(r) != company_filter:
            return False
        return True

    def _matches_dict(d) -> bool:
        dev = d.get("device") or {}
        if vendor_filter  and dev.get("vendor") != vendor_filter:
            return False
        if company_filter:
            loc = (dev.get("location") or "").split(" | ")[0].strip()
            if loc != company_filter:
                return False
        return True

    # Prefer live in-memory results; fall back to SQLite cache
    results = _state["results"]
    if results:
        at_risk = [r for r in results if r.is_at_risk and _matches(r)]
        safe    = [r for r in results if r.is_safe    and _matches(r)]
        stats   = EOLAnalyser.summary_stats(at_risk + safe)
    elif _state["last_at_risk"] or _state["last_safe"]:
        # Filter dicts before reconstruction (avoids building objects we'll discard)
        ar_dicts = [d for d in _state["last_at_risk"] if _matches_dict(d)]
        sf_dicts = [d for d in _state["last_safe"]    if _matches_dict(d)]
        at_risk  = [dict_to_result(d) for d in ar_dicts]
        safe     = [dict_to_result(d) for d in sf_dicts]
        stats    = _state["last_stats"]
    else:
        return jsonify({"status": "error", "message": "No analysis results — run a scan first"}), 400

    base_dir   = os.path.abspath(os.path.dirname(__file__))
    output_dir = os.path.join(base_dir, "output")
    os.makedirs(output_dir, exist_ok=True)

    # Build a unique filename when filters are active
    suffix = ""
    if vendor_filter:  suffix += f"_{vendor_filter.replace(' ','_')[:20]}"
    if company_filter: suffix += f"_{company_filter.replace(' ','_')[:20]}"
    import re as _re
    suffix = _re.sub(r"[^a-zA-Z0-9_\-]", "", suffix)
    filename = f"network_eol_report_{date.today().strftime('%Y%m%d')}{suffix}.xlsx"
    path     = os.path.join(output_dir, filename)

    try:
        gen = ExcelReportGenerator(path)
        gen.generate(at_risk, safe, stats, generated_by="EOL Agent v3.0")
    except Exception as e:
        return jsonify({"status": "error", "message": f"Report generation failed: {e}"}), 500

    return send_file(
        os.path.abspath(path),
        as_attachment=True,
        download_name=filename,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )


if __name__ == "__main__":
    os.makedirs("frontend", exist_ok=True)
    os.makedirs("output",   exist_ok=True)
    os.makedirs("data",     exist_ok=True)
    print(f"\n  EOL Agent API v3.0  ->  http://localhost:{PORT}\n")
    app.run(host="0.0.0.0", port=PORT, debug=False)
