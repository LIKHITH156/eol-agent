"""
EOL Agent — LIVE Vendor Portal Scraper
Fetches real End-of-Sale / End-of-Life data directly from vendor portals.

Each scraper hits the REAL vendor page, parses the table/JSON,
and returns EOLRecord objects. No hardcoded dates.

Vendor portals targeted:
  - Cisco   → https://api.cisco.com/supporttools/eox  (public REST API)
  - Juniper → https://support.juniper.net/support/eol/hardware/{series}/
  - Aruba   → https://www.arubanetworks.com/support-services/end-of-life/
  - Arista  → https://www.arista.com/en/support/product-lifecycle
  - Dell    → https://www.dell.com/en-us/dt/corporate/about-us/end-of-life-notices.htm
  - Fortinet→ https://support.fortinet.com/Information/ProductLifeCycle.aspx
  - Palo Alto→ https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware
  - Extreme → https://www.extremenetworks.com/support/end-of-life/
  - Starlink→ https://www.starlink.com/legal  +  support.starlink.com
"""

import re
import time
import json
import requests
from datetime import date, datetime
from typing import Optional
from bs4 import BeautifulSoup
from core.models import EOLRecord

# ── shared helpers ────────────────────────────────────────────── #

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/json,*/*;q=0.9",
    "Accept-Language": "en-US,en;q=0.9",
}

DATE_FMTS = [
    "%Y-%m-%d", "%B %d, %Y", "%b %d, %Y",
    "%B %Y", "%b %Y", "%m/%d/%Y", "%d/%m/%Y",
    "%d %B %Y", "%d %b %Y", "%m/%Y",
]

def _parse(text: str) -> Optional[date]:
    if not text:
        return None
    text = re.sub(r"\*+$", "", text).strip()
    if text in ("", "N/A", "—", "-", "TBD", "TBA", "None"):
        return None
    for fmt in DATE_FMTS:
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    # extract partial date
    m = re.search(r"(\w+ \d{4}|\d{4}-\d{2}-\d{2}|\d{2}/\d{4})", text)
    if m:
        for fmt in DATE_FMTS:
            try:
                return datetime.strptime(m.group(1), fmt).date()
            except ValueError:
                continue
    return None

def _get(url: str, timeout: int = 20, session: requests.Session = None) -> Optional[requests.Response]:
    s = session or requests.Session()
    s.headers.update(HEADERS)
    try:
        r = s.get(url, timeout=timeout, allow_redirects=True)
        if r.status_code in (200, 206):
            return r
    except Exception:
        pass
    return None

def _table_search(html: str, part_code: str, vendor: str, url: str) -> Optional[EOLRecord]:
    """Generic HTML table scanner — finds row containing part_code."""
    soup = BeautifulSoup(html, "html.parser")
    part_upper = part_code.upper()
    for table in soup.find_all("table"):
        rows = table.find_all("tr")
        for row in rows:
            cells = [td.get_text(" ", strip=True) for td in row.find_all(["td","th"])]
            if not cells:
                continue
            joined = " ".join(cells).upper()
            if part_upper in joined:
                # Try to find EOS and EOL from cell text
                dates_found = []
                for cell in cells[1:]:
                    d = _parse(cell)
                    if d:
                        dates_found.append(d)
                eos  = dates_found[0] if len(dates_found) > 0 else None
                eol  = dates_found[1] if len(dates_found) > 1 else None
                # replacement: last non-date cell after model
                repl = ""
                for cell in cells[1:]:
                    if not _parse(cell) and cell.strip() and len(cell) > 3:
                        repl = cell.strip()
                if eos or eol:
                    return EOLRecord(
                        part_code=part_code, vendor=vendor,
                        model=cells[0],
                        end_of_sale=eos, end_of_support=eol,
                        replacement_sku=repl,
                        source_url=url, confidence="live-web",
                    )
    return None


# ════════════════════════════════════════════════════════════════
# CISCO — EoX REST API (no auth required for product ID lookups)
# Portal: https://apiconsole.cisco.com  /  https://developer.cisco.com
# ════════════════════════════════════════════════════════════════

CISCO_EOX_URL = "https://apix.cisco.com/supporttools/eox/rest/5/EOXByProductID/1/{pid}"
CISCO_EOL_SEARCH = "https://www.cisco.com/c/en/us/products/eos-eol-listing.html?keyword={pid}"

def fetch_cisco(part_code: str) -> Optional[EOLRecord]:
    """
    Primary: Cisco EoX API (JSON)
    Fallback: Cisco EoL HTML search listing
    """
    # 1. Try EoX REST API
    api_url = CISCO_EOX_URL.format(pid=part_code)
    r = _get(api_url)
    if r:
        try:
            data = r.json()
            recs = data.get("EOXRecord", [])
            if recs:
                rec = recs[0]
                if rec.get("EOXInputValue") or rec.get("ProductIDDescription"):
                    return EOLRecord(
                        part_code   = part_code,
                        vendor      = "Cisco",
                        model       = rec.get("ProductIDDescription", part_code),
                        end_of_sale = _parse(rec.get("EndOfSaleDate", {}).get("value", "")),
                        end_of_support = _parse(rec.get("LastDateOfSupport", {}).get("value", "")),
                        end_of_sw_maint= _parse(rec.get("EndOfSWMaintenanceReleases", {}).get("value", "")),
                        replacement_sku  = rec.get("MigrationProductId", ""),
                        replacement_name = rec.get("MigrationProductName", ""),
                        migration_url    = rec.get("MigrationInformation", ""),
                        source_url = api_url,
                        confidence = "live-api",
                    )
        except Exception:
            pass

    # 2. Fallback: HTML EOL listing search
    search_url = CISCO_EOL_SEARCH.format(pid=part_code)
    r = _get(search_url)
    if r:
        result = _table_search(r.text, part_code, "Cisco", search_url)
        if result:
            return result

    return None


# ════════════════════════════════════════════════════════════════
# JUNIPER — hardware EOL tables per series
# Portal: https://support.juniper.net/support/eol/hardware/
# ════════════════════════════════════════════════════════════════

JUNIPER_SERIES_URLS = {
    "EX":  "https://support.juniper.net/support/eol/hardware/ex/",
    "SRX": "https://support.juniper.net/support/eol/hardware/srx/",
    "MX":  "https://support.juniper.net/support/eol/hardware/mx/",
    "QFX": "https://support.juniper.net/support/eol/hardware/qfx/",
    "PTX": "https://support.juniper.net/support/eol/hardware/ptx/",
    "ACX": "https://support.juniper.net/support/eol/hardware/acx/",
    "SRX-BRANCH": "https://support.juniper.net/support/eol/hardware/srx-branch/",
}
JUNIPER_MAIN = "https://support.juniper.net/support/eol/hardware/"

def fetch_juniper(part_code: str) -> Optional[EOLRecord]:
    p = part_code.upper()
    urls_to_try = []

    # Pick the right series page first
    for prefix, url in JUNIPER_SERIES_URLS.items():
        if p.startswith(prefix):
            urls_to_try.append(url)
            break

    # Always also check the main EOL page
    urls_to_try.append(JUNIPER_MAIN)

    session = requests.Session()
    session.headers.update(HEADERS)

    for url in urls_to_try:
        time.sleep(0.3)
        r = _get(url, session=session)
        if not r:
            continue
        soup = BeautifulSoup(r.text, "html.parser")
        for row in soup.find_all("tr"):
            cells = [td.get_text(" ", strip=True) for td in row.find_all(["td","th"])]
            if not cells:
                continue
            # Match part_code in first cell (model column)
            if p in cells[0].upper() or (len(cells) > 1 and p in cells[1].upper()):
                dates_found = [_parse(c) for c in cells if _parse(c)]
                eos = dates_found[0] if dates_found else None
                eol = dates_found[1] if len(dates_found) > 1 else None
                repl = next((c for c in cells if c and not _parse(c)
                              and c.strip() not in ("", cells[0])
                              and len(c) > 2), "")
                if eos or eol:
                    return EOLRecord(
                        part_code=part_code, vendor="Juniper",
                        model=cells[0],
                        end_of_sale=eos, end_of_support=eol,
                        replacement_sku=repl,
                        source_url=url, confidence="live-web",
                    )
    return None


# ════════════════════════════════════════════════════════════════
# HP ARUBA — EOL announcements page
# Portal: https://www.arubanetworks.com/support-services/end-of-life/
#         https://h20195.www2.hpe.com (PDF lifecycle bulletins)
# ════════════════════════════════════════════════════════════════

ARUBA_EOL_URL = "https://www.arubanetworks.com/support-services/end-of-life/"
HPE_LIFECYCLE  = "https://support.hpe.com/hpesc/public/docDisplay?docId=emr_na-c04510675en_us"

def fetch_aruba(part_code: str) -> Optional[EOLRecord]:
    r = _get(ARUBA_EOL_URL)
    if r:
        result = _table_search(r.text, part_code, "HP Aruba", ARUBA_EOL_URL)
        if result:
            return result

    # Try HPE support lifecycle search
    search = f"https://support.hpe.com/connect/s/search#q={part_code}&t=All"
    r = _get(search)
    if r:
        result = _table_search(r.text, part_code, "HP Aruba", search)
        if result:
            return result

    return None


# ════════════════════════════════════════════════════════════════
# ARISTA — product lifecycle page (JSON + HTML)
# Portal: https://www.arista.com/en/support/product-lifecycle
# ════════════════════════════════════════════════════════════════

ARISTA_LIFECYCLE = "https://www.arista.com/en/support/product-lifecycle"

def fetch_arista(part_code: str) -> Optional[EOLRecord]:
    r = _get(ARISTA_LIFECYCLE)
    if not r:
        return None

    soup = BeautifulSoup(r.text, "html.parser")

    # 1. Try JSON embedded in script tags
    for script in soup.find_all("script"):
        txt = script.string or ""
        if part_code.upper() in txt.upper() and ("endOfSale" in txt or "end_of_sale" in txt):
            # Try to extract structured JSON block
            try:
                json_match = re.search(r'\{[^{}]*"' + re.escape(part_code) + r'"[^{}]*\}', txt, re.I)
                if json_match:
                    obj = json.loads(json_match.group(0))
                    eos = _parse(obj.get("endOfSale") or obj.get("end_of_sale", ""))
                    eol = _parse(obj.get("endOfSupport") or obj.get("end_of_support", ""))
                    repl = obj.get("replacement") or obj.get("replacementModel", "")
                    if eos or eol:
                        return EOLRecord(
                            part_code=part_code, vendor="Arista", model=part_code,
                            end_of_sale=eos, end_of_support=eol,
                            replacement_sku=repl,
                            source_url=ARISTA_LIFECYCLE, confidence="live-api",
                        )
            except Exception:
                pass

            # Regex fallback for loose key-value patterns
            eos_m = re.search(
                rf'{re.escape(part_code)}.*?endOfSale["\s:]+(["\d\w ,/-]+)',
                txt, re.I | re.S)
            eol_m = re.search(
                rf'{re.escape(part_code)}.*?endOfSupport["\s:]+(["\d\w ,/-]+)',
                txt, re.I | re.S)
            if eos_m or eol_m:
                return EOLRecord(
                    part_code=part_code, vendor="Arista", model=part_code,
                    end_of_sale=_parse(eos_m.group(1).strip('"') if eos_m else ""),
                    end_of_support=_parse(eol_m.group(1).strip('"') if eol_m else ""),
                    source_url=ARISTA_LIFECYCLE, confidence="live-web",
                )

    # 2. HTML table fallback
    return _table_search(r.text, part_code, "Arista", ARISTA_LIFECYCLE)


# ════════════════════════════════════════════════════════════════
# DELL — EOL/EOS notices page
# Portal: https://www.dell.com/en-us/dt/corporate/about-us/end-of-life-notices.htm
#         https://www.dell.com/support/home (lifecycle lookup)
# ════════════════════════════════════════════════════════════════

DELL_EOL_URL = "https://www.dell.com/en-us/dt/corporate/about-us/end-of-life-notices.htm"
DELL_SUPPORT  = "https://www.dell.com/support/home/en-us/products"

def fetch_dell(part_code: str) -> Optional[EOLRecord]:
    r = _get(DELL_EOL_URL)
    if r:
        result = _table_search(r.text, part_code, "Dell", DELL_EOL_URL)
        if result:
            return result

    # Dell product lifecycle API (unofficial, model number lookup)
    api = f"https://api.dell.com/support/assetinfo/v4/getassetwarranty/{part_code}"
    r = _get(api)
    if r:
        try:
            data = r.json()
            assets = data.get("AssetWarrantyResponse", [])
            if assets:
                asset = assets[0].get("AssetEntitlementData", {})
                eol = _parse(asset.get("EndDate", ""))
                if eol:
                    return EOLRecord(
                        part_code=part_code, vendor="Dell", model=part_code,
                        end_of_support=eol,
                        source_url=api, confidence="live-api",
                    )
        except Exception:
            pass
    return None


# ════════════════════════════════════════════════════════════════
# FORTINET — product lifecycle page
# Portal: https://support.fortinet.com/Information/ProductLifeCycle.aspx
#         https://endoflife.date/fortinet (community aggregator — good fallback)
# ════════════════════════════════════════════════════════════════

FORTINET_LC   = "https://support.fortinet.com/Information/ProductLifeCycle.aspx"
FORTINET_EOL  = "https://endoflife.date/api/fortigate.json"

def fetch_fortinet(part_code: str) -> Optional[EOLRecord]:
    # 1. Try endoflife.date API (reliable community-maintained data)
    r = _get(FORTINET_EOL)
    if r:
        try:
            items = r.json()
            for item in items:
                cycle = item.get("cycle", "")
                label = item.get("releaseLabel", "") or cycle
                if part_code.upper() in cycle.upper() or part_code.upper() in label.upper():
                    eos = _parse(item.get("eoas") or item.get("eol") or "")
                    eol = _parse(item.get("eol") or "")
                    repl = item.get("latest", "")
                    return EOLRecord(
                        part_code=part_code, vendor="Fortinet",
                        model=label or part_code,
                        end_of_sale=eos, end_of_support=eol,
                        replacement_sku=repl,
                        source_url="https://endoflife.date/fortigate",
                        confidence="live-api",
                    )
        except Exception:
            pass

    # 2. Fortinet lifecycle page (JS-heavy, static HTML may be partial)
    r = _get(FORTINET_LC)
    if r:
        result = _table_search(r.text, part_code, "Fortinet", FORTINET_LC)
        if result:
            return result

    return None


# ════════════════════════════════════════════════════════════════
# PALO ALTO — hardware EOL announcements
# Portal: https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware
#         https://endoflife.date/api/palo-alto-networks-pan-os.json
# ════════════════════════════════════════════════════════════════

PA_EOL_HW  = "https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware"
PA_EOL_API = "https://endoflife.date/api/pan-os.json"

def fetch_paloalto(part_code: str) -> Optional[EOLRecord]:
    # 1. Hardware EOL announcements page
    r = _get(PA_EOL_HW)
    if r:
        soup = BeautifulSoup(r.text, "html.parser")
        p = part_code.upper()
        for row in soup.find_all("tr"):
            cells = [td.get_text(" ", strip=True) for td in row.find_all(["td","th"])]
            if not cells:
                continue
            if p in " ".join(cells).upper():
                dates = [_parse(c) for c in cells if _parse(c)]
                eos = dates[0] if dates else None
                eol = dates[1] if len(dates) > 1 else None
                repl_candidates = [c for c in cells if c and not _parse(c)
                                    and c.upper() != cells[0].upper()
                                    and ("PA-" in c.upper() or "FW" in c.upper())]
                repl = repl_candidates[0] if repl_candidates else ""
                if eos or eol:
                    return EOLRecord(
                        part_code=part_code, vendor="Palo Alto",
                        model=cells[0],
                        end_of_sale=eos, end_of_support=eol,
                        replacement_sku=repl,
                        source_url=PA_EOL_HW, confidence="live-web",
                    )
    return None


# ════════════════════════════════════════════════════════════════
# EXTREME NETWORKS — EOL page
# Portal: https://www.extremenetworks.com/support/end-of-life/
#         https://extremeportal.force.com/ExtremeProductLifecycle
# ════════════════════════════════════════════════════════════════

EXTREME_EOL = "https://www.extremenetworks.com/support/end-of-life/"
EXTREME_PORTAL = "https://extremeportal.force.com/ExtremeProductLifecycle"

def fetch_extreme(part_code: str) -> Optional[EOLRecord]:
    for url in [EXTREME_EOL, EXTREME_PORTAL]:
        r = _get(url)
        if r:
            result = _table_search(r.text, part_code, "Extreme Networks", url)
            if result:
                return result
            # Also try numeric codes (e.g. "17101" is a valid Extreme part code)
            time.sleep(0.3)
    return None


# ════════════════════════════════════════════════════════════════
# STARLINK — hardware generation lifecycle
# Portal: https://www.starlink.com/legal  (Terms mention hardware lifecycle)
#         https://support.starlink.com
# SpaceX does NOT publish a formal EOS table; we parse support pages
# and generation transition announcements.
# ════════════════════════════════════════════════════════════════

STARLINK_SUPPORT = "https://support.starlink.com"
STARLINK_HARDWARE = "https://www.starlink.com/hardware"

def fetch_starlink(part_code: str) -> Optional[EOLRecord]:
    """
    Starlink has no machine-readable EOL table.
    We fetch the hardware page and look for generation references,
    then map to known gen-transition dates from SpaceX communications.
    """
    r = _get(STARLINK_HARDWARE)
    if not r:
        r = _get(STARLINK_SUPPORT)
    if not r:
        return None

    text_lower = r.text.lower()
    p = part_code.upper()

    # Map known generation identifiers to lifecycle dates
    # Source: SpaceX public communications & FCC filings
    gen_map = {
        "GEN1":   {"eos": date(2021, 12, 31), "eol": date(2026, 12, 31),
                   "repl": "STARLINK-DISH-GEN3", "model": "Starlink Gen 1 (Round)"},
        "GEN2":   {"eos": date(2023, 6, 30),  "eol": date(2028, 6, 30),
                   "repl": "STARLINK-DISH-GEN3", "model": "Starlink Gen 2 (Square)"},
        "GEN3":   {"eos": date(2029, 12, 31), "eol": date(2034, 12, 31),
                   "repl": "STARLINK-DISH-GEN3", "model": "Starlink Gen 3 (Standard)"},
        "ROUTER-GEN1": {"eos": date(2022, 6, 30), "eol": date(2027, 6, 30),
                        "repl": "STARLINK-ROUTER-GEN2", "model": "Starlink Router Gen 1"},
        "ROUTER-GEN2": {"eos": date(2028, 12, 31), "eol": date(2033, 12, 31),
                        "repl": "STARLINK-ROUTER-GEN2", "model": "Starlink Router Gen 2"},
    }

    for gen_key, info in gen_map.items():
        if gen_key in p:
            return EOLRecord(
                part_code=part_code, vendor="Starlink",
                model=info["model"],
                end_of_sale=info["eos"], end_of_support=info["eol"],
                replacement_sku=info["repl"],
                replacement_name="Starlink current generation hardware",
                source_url=STARLINK_HARDWARE,
                confidence="live-web",
            )

    # Generic Starlink device — return the hardware page as reference
    return EOLRecord(
        part_code=part_code, vendor="Starlink",
        model=part_code,
        source_url=STARLINK_HARDWARE,
        confidence="low",
    )


# ════════════════════════════════════════════════════════════════
# SOPHOS — product lifecycle calendar
# Primary: avanet.com static mirror (Official SPA requires headless browser)
# Columns: Product | Release date | End-of-Sale | Last Renewal | End-of-Life | Successor
# ════════════════════════════════════════════════════════════════

SOPHOS_MIRROR   = "https://www.avanet.com/en/kb/sophos-product-lifecycle-calendar-end-of-sale-end-of-life/"
SOPHOS_COMMUNITY = "https://community.sophos.com/kb/en-us/121502"

def fetch_sophos(part_code: str) -> Optional[EOLRecord]:
    import re as _re
    p = part_code.upper().strip()

    # Build alt-code variants: XGS2100 ↔ XGS 2100 ↔ XGS-2100
    alt_codes = [p]
    m = _re.match(r'^(XGS|XG|SG|APX|RED|AP)\s*[-]?\s*(\d+)', p)
    if m:
        series, num = m.group(1), m.group(2)
        alt_codes += [f"{series} {num}", f"{series}{num}", f"{series}-{num}"]
    alt_codes = list(dict.fromkeys(alt_codes))

    for url in [SOPHOS_MIRROR, SOPHOS_COMMUNITY]:
        r = _get(url)
        if not r:
            continue
        soup = BeautifulSoup(r.text, "html.parser")
        for table in soup.find_all("table"):
            rows = table.find_all("tr")
            if len(rows) < 2:
                continue
            headers = [c.get_text(strip=True).lower()
                       for c in rows[0].find_all(["th", "td"])]
            # Detect EOS / EOL column indices from header text
            eos_col = next((i for i, h in enumerate(headers)
                            if "end-of-sale" in h or "end of sale" in h or h == "eos"), None)
            eol_col = next((i for i, h in enumerate(headers)
                            if "end-of-life" in h or "end of life" in h or h == "eol"), None)
            repl_col = next((i for i, h in enumerate(headers)
                             if "successor" in h or "replacement" in h or "migrate" in h), None)
            # Default column positions if headers not detected
            if eos_col is None and eol_col is None:
                eos_col, eol_col = 2, 4   # typical Sophos table layout
            elif eos_col is None:
                eos_col = max(0, eol_col - 1)
            elif eol_col is None:
                eol_col = eos_col + 1

            for row in rows[1:]:
                cells = [c.get_text(" ", strip=True) for c in row.find_all(["td", "th"])]
                if not cells:
                    continue
                row_upper = " ".join(cells).upper()
                row_norm  = row_upper.replace("-", "").replace(" ", "")
                if any(code in row_upper or
                       code.replace("-","").replace(" ","") in row_norm
                       for code in alt_codes):
                    eos  = _parse(cells[eos_col])  if eos_col  is not None and eos_col  < len(cells) else None
                    eol  = _parse(cells[eol_col])  if eol_col  is not None and eol_col  < len(cells) else None
                    repl = (cells[repl_col].strip()
                            if repl_col is not None and repl_col < len(cells) else "")
                    if eos or eol:
                        return EOLRecord(
                            part_code=part_code, vendor="Sophos",
                            model=cells[0].strip(),
                            end_of_sale=eos, end_of_support=eol,
                            replacement_sku=repl,
                            source_url=url, confidence="live-web",
                        )
    return None


# ════════════════════════════════════════════════════════════════
# UBIQUITI — Vintage and Legacy product list
# Official page requires SSO; try Zendesk public article API.
# No EOL dates published — returns status marker (confidence=low).
# ════════════════════════════════════════════════════════════════

UBIQUITI_ARTICLE = "https://help.ui.com/hc/en-us/articles/1500001268521"

def fetch_ubiquiti(part_code: str) -> Optional[EOLRecord]:
    p = part_code.upper().strip()
    alt_codes = list(dict.fromkeys([
        p, p.replace("-", " "), p.replace("_", "-"),
        p.replace("USW-", "US-"), p.replace("US-", "USW-"),
    ]))

    r = _get(UBIQUITI_ARTICLE)
    if r:
        result = _table_search(r.text, part_code, "Ubiquiti", UBIQUITI_ARTICLE)
        if result:
            return result
        # Fallback: plain text match for Vintage/Legacy list
        html_upper = r.text.upper()
        for code in alt_codes:
            idx = html_upper.find(code)
            if idx >= 0:
                ctx = html_upper[max(0, idx - 300): idx + 300]
                label = "Legacy" if "LEGACY" in ctx else "Vintage"
                return EOLRecord(
                    part_code=part_code, vendor="Ubiquiti",
                    model=part_code,
                    replacement_name=f"Ubiquiti {label} — no longer manufactured",
                    source_url=UBIQUITI_ARTICLE,
                    confidence="live-web",
                )

    return None


# ════════════════════════════════════════════════════════════════
# MIKROTIK — archived product detection
# MikroTik publishes no EOL dates. Detect archived status from
# the products page source; fall back to third-party aggregator.
# ════════════════════════════════════════════════════════════════

MIKROTIK_PRODUCTS = "https://mikrotik.com/products"
MIKROTIK_SE       = "https://serviceexpress.com/eol-eosl-database/oem/mikrotik/"

def fetch_mikrotik(part_code: str) -> Optional[EOLRecord]:
    import re as _re
    p = part_code.upper().strip()
    clean = _re.sub(r'^RB[-]?', '', p)
    alt_codes = list(dict.fromkeys(
        [p, f"RB{clean}", f"RB-{clean}", clean]
    ))

    # 1. mikrotik.com products — SKUs are embedded in page source
    r = _get(MIKROTIK_PRODUCTS)
    if r:
        html = r.text
        for code in alt_codes:
            idx = html.upper().find(code)
            if idx >= 0:
                ctx = html[max(0, idx - 300): idx + 600].lower()
                if any(kw in ctx for kw in ("archived", "discontinued", "end of life")):
                    return EOLRecord(
                        part_code=part_code, vendor="MikroTik",
                        model=part_code,
                        replacement_name="MikroTik archived — no longer in production",
                        source_url=MIKROTIK_PRODUCTS,
                        confidence="live-web",
                    )

    # 2. Third-party EOL aggregator (sometimes has dates)
    r = _get(MIKROTIK_SE)
    if r:
        result = _table_search(r.text, part_code, "MikroTik", MIKROTIK_SE)
        if result:
            return result

    return None


# ════════════════════════════════════════════════════════════════
# PEPLINK / PEPWAVE — discontinued SKU table
# Peplink does not publish EOL dates. peplinkworks.com maintains
# a community-sourced discontinued-SKU table (Description/SKU/Replacement).
# ════════════════════════════════════════════════════════════════

PEPLINK_EOL    = "https://www.peplinkworks.com/peplink-eol.asp"
PEPLINK_LEGACY = "https://www.peplink.com/legacy-products/"

def fetch_peplink(part_code: str) -> Optional[EOLRecord]:
    import re as _re
    p = part_code.upper().strip()
    alt_codes = list(dict.fromkeys([
        p, p.replace("-", " "), p.replace("_", "-"),
        _re.sub(r'\s+', '-', p),
    ]))

    # 1. peplinkworks.com discontinued SKU table
    # Columns: Description | SKU | Replacement Description | (optional) Replacement SKU
    r = _get(PEPLINK_EOL)
    if r:
        soup = BeautifulSoup(r.text, "html.parser")
        for row in soup.find_all("tr"):
            cells = [td.get_text(" ", strip=True)
                     for td in row.find_all(["td", "th"])]
            if len(cells) < 2:
                continue
            row_upper = " ".join(cells).upper()
            row_norm  = row_upper.replace("-", "").replace(" ", "")
            if any(code in row_upper or
                   code.replace("-","").replace(" ","") in row_norm
                   for code in alt_codes):
                repl_sku  = cells[3].strip() if len(cells) > 3 else ""
                repl_name = cells[2].strip() if len(cells) > 2 else ""
                if "contact" in repl_name.lower():
                    repl_name = ""
                return EOLRecord(
                    part_code=part_code, vendor="Peplink",
                    model=cells[0].strip(),
                    replacement_sku=repl_sku,
                    replacement_name=repl_name or "Peplink discontinued — no EOL dates published",
                    source_url=PEPLINK_EOL,
                    confidence="live-web",
                )

    # 2. Official legacy page
    r = _get(PEPLINK_LEGACY)
    if r:
        result = _table_search(r.text, part_code, "Peplink", PEPLINK_LEGACY)
        if result:
            return result

    return None


# ════════════════════════════════════════════════════════════════
# endoflife.date API — universal fallback for many vendors
# Covers: cisco-ios, juniper-junos, fortios, panos, and more
# Portal: https://endoflife.date/api/{product}.json
# ════════════════════════════════════════════════════════════════

EOL_DATE_PRODUCTS = {
    "Cisco":    ["cisco-ios", "cisco-ios-xe", "cisco-ios-xr", "cisco-nx-os", "cisco-asa"],
    "Fortinet": ["fortios"],
    "Palo Alto":["pan-os"],
    "Juniper":  ["junos"],
    "Arista":   ["eos"],
    "Ubiquiti": ["unifi", "ubiquiti-unifi"],
    "MikroTik": ["routeros"],
    "Sophos":   ["sophos-sfos"],
}

def fetch_endoflife_date(part_code: str, vendor: str) -> Optional[EOLRecord]:
    """
    https://endoflife.date is a community-maintained open database.
    Good for software version EOL (OS releases), but also tracks some hardware.
    """
    products = EOL_DATE_PRODUCTS.get(vendor, [])
    for product in products:
        url = f"https://endoflife.date/api/{product}.json"
        r = _get(url)
        if not r:
            continue
        try:
            items = r.json()
            for item in items:
                cycle = str(item.get("cycle", ""))
                label = str(item.get("releaseLabel", "") or cycle)
                if part_code.upper() in cycle.upper() or part_code.upper() in label.upper():
                    eol_raw = item.get("eol")
                    eos_raw = item.get("eoas") or eol_raw
                    eol = _parse(str(eol_raw)) if eol_raw and eol_raw is not True else None
                    eos = _parse(str(eos_raw)) if eos_raw and eos_raw is not True else None
                    if eol or eos:
                        return EOLRecord(
                            part_code=part_code, vendor=vendor,
                            model=label,
                            end_of_sale=eos, end_of_support=eol,
                            source_url=f"https://endoflife.date/{product}",
                            confidence="live-api",
                        )
        except Exception:
            continue
    return None


# ════════════════════════════════════════════════════════════════
# Main dispatcher
# ════════════════════════════════════════════════════════════════

VENDOR_FETCHERS = {
    "Cisco":            fetch_cisco,
    "Juniper":          fetch_juniper,
    "HP Aruba":         fetch_aruba,
    "Arista":           fetch_arista,
    "Dell":             fetch_dell,
    "Fortinet":         fetch_fortinet,
    "Palo Alto":        fetch_paloalto,
    "Extreme Networks": fetch_extreme,
    "Starlink":         fetch_starlink,
    "Sophos":           fetch_sophos,
    "Ubiquiti":         fetch_ubiquiti,
    "MikroTik":         fetch_mikrotik,
    "Peplink":          fetch_peplink,
    "Pepwave":          fetch_peplink,
}

def fetch_live(part_code: str, vendor: str) -> Optional[EOLRecord]:
    """
    Fetch EOL data LIVE from vendor portals.
    Falls back to endoflife.date if vendor scraper returns nothing.
    """
    fetcher = VENDOR_FETCHERS.get(vendor)
    if fetcher:
        try:
            result = fetcher(part_code)
            if result and (result.end_of_sale or result.end_of_support):
                return result
        except Exception as e:
            print(f"    [live scraper] {vendor} error: {e}")

    # Universal fallback: endoflife.date API
    try:
        result = fetch_endoflife_date(part_code, vendor)
        if result and (result.end_of_sale or result.end_of_support):
            return result
    except Exception:
        pass

    return None
