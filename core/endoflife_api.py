"""
Free EOL data from endoflife.date (https://endoflife.date/api/).
No API key, no registration — completely free and open.

Covers: Cisco Meraki, Cisco Catalyst 9000, Cisco ISR/ASR,
        Fortinet FortiGate (firmware), Juniper EX/SRX,
        Palo Alto PAN-OS, Arista EOS, and more.
"""

import re
import requests
from datetime import date, datetime
from typing import Optional
from core.models import EOLRecord

BASE_URL = "https://endoflife.date/api"
TIMEOUT  = 10
HEADERS  = {"Accept": "application/json", "User-Agent": "EOL-Agent/3.0 (free-tier)"}

# ── Product slug maps ──────────────────────────────────────────── #

# Cisco Meraki: part-code prefix → product slug
_MERAKI_SLUGS = {
    "MR":  "cisco-meraki-mr",
    "MS":  "cisco-meraki-ms",
    "MX":  "cisco-meraki-mx",
    "MG":  "cisco-meraki-mg",
    "MV":  "cisco-meraki-mv",
    "Z3":  "cisco-meraki-mz",
    "Z4":  "cisco-meraki-mz",
    "Z5":  "cisco-meraki-mz",
}

# Cisco Catalyst / ISR / ASR: part-code prefix → product slug
_CISCO_HW_SLUGS = {
    "C9200L":  "cisco-catalyst-9200",
    "C9200":   "cisco-catalyst-9200",
    "C9300L":  "cisco-catalyst-9300",
    "C9300X":  "cisco-catalyst-9300",
    "C9300":   "cisco-catalyst-9300",
    "C9400":   "cisco-catalyst-9400",
    "C9500X":  "cisco-catalyst-9500",
    "C9500":   "cisco-catalyst-9500",
    "C9600":   "cisco-catalyst-9600",
    "C9800":   "cisco-catalyst-9800",
    "C1111":   "cisco-1100-series-isr",
    "C1117":   "cisco-1100-series-isr",
    "C1121":   "cisco-1100-series-isr",
    "C8200":   "cisco-catalyst-8000v",
    "C8300":   "cisco-catalyst-8000v",
    "ISR4321": "cisco-4000-series-isr",
    "ISR4331": "cisco-4000-series-isr",
    "ISR4351": "cisco-4000-series-isr",
    "ISR4431": "cisco-4000-series-isr",
    "ISR4451": "cisco-4000-series-isr",
    "ASR1001": "cisco-asr-1000-series",
    "ASR1002": "cisco-asr-1000-series",
    "ASR1004": "cisco-asr-1000-series",
    "ASR1006": "cisco-asr-1000-series",
}

# Other vendors: part-code prefix → product slug
_VENDOR_SLUGS = {
    "FG-":   "fortigate",       # Fortinet FortiGate
    "FGR-":  "fortigate",
    "EX2":   "juniper-ex",      # Juniper EX series
    "EX3":   "juniper-ex",
    "EX4":   "juniper-ex",
    "SRX":   "juniper-srx",     # Juniper SRX series
    "QFX":   "juniper-qfx",     # Juniper QFX
    "DCS-":  "arista-eos",      # Arista (EOS software)
}

# In-memory product-cycle cache to avoid repeat full-list fetches per scan
_product_cache: dict[str, list] = {}


def _parse_date(s) -> Optional[date]:
    if not s or str(s) in ("false", "true", "None", ""):
        return None
    try:
        return datetime.strptime(str(s)[:10], "%Y-%m-%d").date()
    except Exception:
        return None


def _fetch_cycles(product: str) -> list:
    if product in _product_cache:
        return _product_cache[product]
    try:
        r = requests.get(f"{BASE_URL}/{product}.json", timeout=TIMEOUT, headers=HEADERS)
        if r.status_code == 200:
            data = r.json()
            if isinstance(data, list) and data:
                _product_cache[product] = data
                return data
    except Exception:
        pass
    _product_cache[product] = []   # cache miss so we don't retry
    return []


def _best_cycle(part_upper: str, cycles: list) -> Optional[dict]:
    """Find the cycle that best matches the given part code."""
    # 1. Exact cycle name in part code
    for c in cycles:
        cn = str(c.get("cycle", "")).upper()
        if cn and (cn == part_upper or cn in part_upper or part_upper.startswith(cn)):
            return c

    # 2. Model number extraction match
    m = re.search(r'[A-Z]+[-\s]?(\d+\w*)', part_upper)
    if m:
        num = m.group(1)
        for c in cycles:
            cn = str(c.get("cycle", "")).upper()
            if num in cn or cn.startswith(num):
                return c

    # 3. Any numeric substring match
    nums = re.findall(r'\d+', part_upper)
    if nums:
        for c in cycles:
            cn = str(c.get("cycle", ""))
            if any(n in cn for n in nums if len(n) >= 2):
                return c

    # 4. Return most recent cycle as last resort if it has an EOL date
    if cycles:
        recent = sorted(cycles, key=lambda x: str(x.get("cycle", "")), reverse=True)
        if recent[0].get("eol") or recent[0].get("eoas"):
            return recent[0]

    return None


def _make_record(part_code: str, vendor: str, cycle: dict, slug: str) -> Optional[EOLRecord]:
    """Convert a cycle dict to an EOLRecord."""
    eos = _parse_date(cycle.get("eoas") or cycle.get("discontinued"))
    eol = _parse_date(cycle.get("eol") or cycle.get("support"))
    if not eos and not eol:
        return None
    link = cycle.get("link") or f"https://endoflife.date/{slug}"
    return EOLRecord(
        part_code=part_code,
        vendor=vendor,
        model=f"{part_code} (cycle {cycle.get('cycle','?')})",
        end_of_sale=eos,
        end_of_support=eol,
        source_url=link,
        confidence="high",
    )


def lookup_endoflife(part_code: str) -> Optional[EOLRecord]:
    """
    Query endoflife.date for the given hardware part code.
    Returns EOLRecord on success, None if not found.
    """
    part_upper = part_code.upper().strip()

    # ── Cisco Meraki ───────────────────────────────────────────── #
    for prefix, slug in _MERAKI_SLUGS.items():
        if part_upper.startswith(prefix):
            cycles = _fetch_cycles(slug)
            if cycles:
                cycle = _best_cycle(part_upper, cycles)
                if cycle:
                    return _make_record(part_code, "Cisco Meraki", cycle, slug)

    # ── Cisco Catalyst / ISR / ASR ─────────────────────────────── #
    for prefix, slug in _CISCO_HW_SLUGS.items():
        if part_upper.startswith(prefix.upper()):
            cycles = _fetch_cycles(slug)
            if cycles:
                cycle = _best_cycle(part_upper, cycles)
                if cycle:
                    return _make_record(part_code, "Cisco", cycle, slug)

    # ── Other vendors ──────────────────────────────────────────── #
    for prefix, slug in _VENDOR_SLUGS.items():
        if part_upper.startswith(prefix.upper()):
            cycles = _fetch_cycles(slug)
            if cycles:
                cycle = _best_cycle(part_upper, cycles)
                if cycle:
                    vendor = "Fortinet" if "fortigate" in slug else \
                             "Juniper"  if "juniper"  in slug else \
                             "Arista"   if "arista"   in slug else "Unknown"
                    return _make_record(part_code, vendor, cycle, slug)

    return None


def clear_cache():
    """Clear in-memory product cycle cache (useful between test runs)."""
    _product_cache.clear()
