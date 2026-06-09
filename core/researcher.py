"""
EOL Agent — Web Research Engine  v3.1
Lookup priority per device:
  1. SQLite cache      (instant, 24-h TTL)
  2. Master DB + Local DB (curated, instant)
  3. endoflife.date API (free, no key — Meraki + Cisco Catalyst + more)
  4. Live vendor portal scraping (smart table parser + POST forms)
  5. Return UNKNOWN
"""

import os
import re
import time
import threading
import requests
from datetime import date, datetime
from typing import Optional
from bs4 import BeautifulSoup
from core.models import EOLRecord
from core.eol_database import lookup_local
import core.cache as cache
from core.endoflife_api import lookup_endoflife

_CACHE_TTL = int(os.environ.get("CACHE_TTL_HOURS", "24"))

# Shared HTML page cache — prevents fetching the same vendor page for every device.
# Filled during a scan; call clear_html_cache() at scan start.
_html_cache: dict[str, str] = {}
_html_lock  = threading.Lock()


def clear_html_cache():
    with _html_lock:
        _html_cache.clear()


# ── Date parsing helpers ──────────────────────────────────────── #

DATE_FORMATS = [
    "%Y-%m-%d", "%B %d, %Y", "%b %d, %Y",
    "%B %Y",    "%b %Y",     "%m/%d/%Y",
    "%d/%m/%Y", "%d %B %Y",  "%d %b %Y",
    "%m/%Y",
]


def parse_date(text: str) -> Optional[date]:
    if not text:
        return None
    text = text.strip().rstrip("*").strip()
    if text in ("", "N/A", "—", "-", "TBD", "TBA", "N.A.", "NA"):
        return None
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    m = re.search(r"(\w+ \d{4}|\d{4}-\d{2}-\d{2}|\d{1,2}/\d{4})", text)
    if m:
        for fmt in DATE_FORMATS:
            try:
                return datetime.strptime(m.group(1), fmt).date()
            except ValueError:
                continue
    return None


def _validate_date(d: Optional[date]) -> Optional[date]:
    if d is None:
        return None
    if not (date(2000, 1, 1) <= d <= date(2045, 12, 31)):
        return None
    return d


def _validate_record(record: EOLRecord) -> EOLRecord:
    record.end_of_sale     = _validate_date(record.end_of_sale)
    record.end_of_support  = _validate_date(record.end_of_support)
    record.end_of_sw_maint = _validate_date(record.end_of_sw_maint)
    return record


def _has_dates(record: Optional[EOLRecord]) -> bool:
    return bool(record and (record.end_of_sale or record.end_of_support))


# ── Vendor identification ─────────────────────────────────────── #

VENDOR_PATTERNS = {
    "Cisco": ["WS-C", "C9", "ASA", "FPR", "ISR", "ASR", "AIR-", "N9K",
              "CISCO", "C88", "C87", "C86", "C85", "C84", "C83", "C82",
              "C921", "C931", "C891", "C881", "C871", "C8200", "C8300",
              "C8500", "C1111", "C1117", "C1121", "CBS3", "N5K-", "N7K-",
              "N3K-", "ME-36", "PIX-", "SF3", "SF5", "SG2", "SG3", "SG35",
              "BE7H", "SNS-", "CW91", "SE-800", "FP4", "FP7", "FP8",
              "CX555", "CX755", "C1-CISCO", "C1921"],
    "Juniper":          ["EX2", "EX3", "EX4", "EX6", "SRX", "QFX", "PTX", "ACX",
                         "NS-", "SSG", "NSISG", "JUNIPER"],
    "HP Aruba":         ["JL", "J9", "J8", "AP-3", "AP-5", "AP-6", "ARUBA",
                         "HP ", "HPE ", "A5500"],
    "Arista":           ["DCS-", "7050", "7060", "7160", "7170", "7280", "7300", "7358", "7010"],
    "Dell":             ["N2024", "N2048", "N3024", "N3048", "N32", "S41", "S42", "S51", "S52", "Z91", "Z93"],
    "Fortinet":         ["FG-", "FW-", "FAZ", "FMG", "FAP", "FS-",
                         "FORTIGATE", "FORTISWITCH", "FORTIAP", "FORTIANALYZER"],
    "Palo Alto":        ["PA-", "PAN-"],
    "Extreme Networks": ["BR-", "AP30", "AP46", "AP305", "AP460",
                         "X460", "X450", "SUMMIT", "FESX", "BIGIRON", "FASTIRON"],
    "Starlink":         ["STARLINK", "SL-"],
    "Cisco Meraki":     ["MR", "MS1", "MS2", "MS3", "MS4", "MS-1", "MS-2",
                         "MX6", "MX7", "MX8", "MX9", "MX10", "MX45", "MX67", "MX68",
                         "MX75", "MX85", "MX95", "MX100", "MX120", "MX250", "MX450",
                         "MX480", "MX960", "MX240", "MG2", "MG4", "MG5", "MV2", "Z3", "Z4"],
    "MikroTik":         ["RB", "MIKROTIK", "CHATEAU", "C53U", "C52U", "CAPLHG", "RBLHG"],
    "Ubiquiti":         ["UAP", "USW", "U6-", "US-8", "NBE-", "NANOSTATION", "UNIFI"],
    "Sophos":           ["XGS", "XG-", "SG-"],
    "Peplink":          ["PEPLINK", "MAX BR", "BR1 MINI"],
}


def infer_vendor(part_code: str, name: str = "") -> str:
    text = (part_code + " " + name).upper()

    fortinet_pats = VENDOR_PATTERNS["Fortinet"]
    if any(text.startswith(p.upper()) or p.upper() in text for p in fortinet_pats):
        return "Fortinet"

    if re.match(r"^M[RSVGX]\d", text) or re.match(r"^Z[345]\b", text):
        return "Cisco Meraki"

    for vendor, patterns in VENDOR_PATTERNS.items():
        if vendor in ("Fortinet", "Cisco Meraki"):
            continue
        if any(text.startswith(p.upper()) or p.upper() in text for p in patterns):
            return vendor

    if re.match(r"^\d{5}$", part_code.strip()):
        return "Extreme Networks"
    return "Can't Predict"


# ─────────────────────────────────────────────────────────────── #
#  Main Researcher class                                           #
# ─────────────────────────────────────────────────────────────── #

class EOLResearcher:
    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) "
            "Gecko/20100101 Firefox/124.0"
        ),
        "Accept":          "text/html,application/xhtml+xml,application/json,*/*;q=0.9",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection":      "keep-alive",
    }
    REQUEST_TIMEOUT = 20

    def __init__(self, use_web: bool = True, rate_limit_s: float = 0.6):
        self.use_web      = use_web
        self.rate_limit_s = rate_limit_s
        self._last_req    = 0.0
        self.session      = requests.Session()
        self.session.headers.update(self.HEADERS)

    # ── Public API ───────────────────────────────────────────────── #

    def lookup(self, part_code: str, vendor: str = "") -> EOLRecord:
        part_clean = part_code.strip()
        part_upper = part_clean.upper()

        # 1. SQLite cache (web results only, TTL-limited)
        cached = cache.get_cached_eol(part_upper, ttl_hours=_CACHE_TTL)
        if cached:
            print(f"    [CACHE] {part_clean:<30} hit (ttl={_CACHE_TTL}h)")
            return cache.dict_to_eolrecord(cached)

        # 2. Master DB + Local curated DB (master takes priority)
        record = lookup_local(part_upper)
        if record:
            source_tag = "MASTER" if record.source_url == "master_assest_data.xlsx" else "DB"
            if record.confidence == "low" and self.use_web:
                print(f"    [{source_tag}] {part_clean:<30} low-conf - checking web")
                web = self._web_lookup(part_clean, record.vendor or infer_vendor(part_upper))
                if _has_dates(web):
                    web = _validate_record(web)
                    web.confidence = "medium"
                    cache.set_cached_eol(part_upper, web.vendor, web, source="web")
                    print(f"    [WEB ] {part_clean:<30} dates filled from web")
                    return web
            print(f"    [{source_tag}] {part_clean:<30} ({record.vendor})")
            return record

        effective_vendor = vendor or infer_vendor(part_upper)

        # 3. endoflife.date free API (no key, authoritative for Meraki + Cisco 9000)
        if self.use_web:
            eold = lookup_endoflife(part_clean)
            if _has_dates(eold):
                eold = _validate_record(eold)
                cache.set_cached_eol(part_upper, eold.vendor, eold, source="endoflife.date")
                print(f"    [EOL.D] {part_clean:<30} (endoflife.date)")
                return eold

        # 4. Live vendor portal scraping
        if self.use_web:
            record = self._web_lookup(part_clean, effective_vendor)
            if _has_dates(record):
                record = _validate_record(record)
                cache.set_cached_eol(part_upper, record.vendor, record, source="web-scrape")
                print(f"    [WEB ] {part_clean:<30} ({effective_vendor})")
                return record

        print(f"    [???] {part_clean:<30} not found ({effective_vendor})")
        return EOLRecord(
            part_code=part_clean, vendor=effective_vendor,
            model=part_clean, confidence="none",
        )

    # ── Web lookup dispatcher ────────────────────────────────────── #

    def _web_lookup(self, part_code: str, vendor: str) -> Optional[EOLRecord]:
        v = vendor.lower()
        dispatch = {
            "cisco meraki":     self._meraki,
            "cisco":            self._cisco,
            "juniper":          self._juniper,
            "hp aruba":         self._aruba,
            "arista":           self._arista,
            "dell":             self._dell,
            "fortinet":         self._fortinet,
            "palo alto":        self._paloalto,
            "extreme networks": self._extreme,
            "starlink":         self._starlink,
            "sophos":           self._sophos,
            "ubiquiti":         self._ubiquiti,
            "mikrotik":         self._mikrotik,
            "peplink":          self._peplink,
            "pepwave":          self._peplink,
        }
        for key, fn in dispatch.items():
            if key in v:
                try:
                    return fn(part_code)
                except Exception as e:
                    print(f"      [err] {vendor} scraper: {e}")
        return None

    # ── CISCO MERAKI ─────────────────────────────────────────────── #

    def _meraki(self, part_code: str) -> Optional[EOLRecord]:
        """Try Meraki EOL pages — endoflife.date is already tried in step 3."""
        urls = [
            "https://documentation.meraki.com/General_Administration/Other_Topics/Meraki_End-of-Life_(EOL)_Products_and_Dates",
            "https://community.meraki.com/t5/Meraki-Community/bd-p/meraki-community",
        ]
        for url in urls:
            result = self._scrape_table_smart(part_code, "Cisco Meraki", url)
            if _has_dates(result):
                return result
        return None

    # ── CISCO ────────────────────────────────────────────────────── #

    def _cisco(self, part_code: str) -> Optional[EOLRecord]:
        """
        Cisco EOL lookup — does NOT require OAuth.
        Tries multiple static HTML sources.
        """
        # Try Cisco's product support page (has EOL info in static HTML)
        p = part_code.upper()

        # Build candidate URLs by product family
        candidate_urls = []

        if p.startswith("WS-C2960") or p.startswith("C2960"):
            candidate_urls.append(
                "https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-2960-x-series-switches/eos-eol-notice-c51-744135.html")
        elif p.startswith("WS-C3650") or p.startswith("C3650"):
            candidate_urls.append(
                "https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-3650-series-switches/eos-eol-notice-c51-741687.html")
        elif p.startswith("WS-C3850") or p.startswith("C3850"):
            candidate_urls.append(
                "https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-3850-series-switches/eos-eol-notice-c51-741704.html")
        elif p.startswith("ASA"):
            candidate_urls.append(
                "https://www.cisco.com/c/en/us/products/collateral/security/asa-5500-series-next-generation-firewalls/eos-eol-notice-c51-736253.html")
        elif p.startswith("FPR"):
            candidate_urls.append(
                "https://www.cisco.com/c/en/us/products/collateral/security/firepower-ngfw/eos-eol-notice-c51-742727.html")
        elif p.startswith(("C9200", "C9300", "C9400", "C9500")):
            candidate_urls.append(
                "https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9000/eol-cisco-catalyst-9000.html")

        # Always try the general EOL listing as fallback
        candidate_urls.append(
            "https://www.cisco.com/c/en/us/products/eos-eol-listing.html")

        for url in candidate_urls:
            result = self._scrape_table_smart(part_code, "Cisco", url)
            if _has_dates(result):
                return result

        return None

    # ── JUNIPER ──────────────────────────────────────────────────── #

    def _juniper(self, part_code: str) -> Optional[EOLRecord]:
        p = part_code.upper()
        series_url_map = {
            "EX":   "https://support.juniper.net/support/eol/hardware/ex/",
            "SRX":  "https://support.juniper.net/support/eol/hardware/srx/",
            "MX":   "https://support.juniper.net/support/eol/hardware/mx/",
            "QFX":  "https://support.juniper.net/support/eol/hardware/qfx/",
            "ACX":  "https://support.juniper.net/support/eol/hardware/acx/",
            "PTX":  "https://support.juniper.net/support/eol/hardware/ptx/",
            "NS-":  "https://support.juniper.net/support/eol/hardware/ns/",
            "SSG":  "https://support.juniper.net/support/eol/hardware/ssg/",
        }
        urls = [v for k, v in series_url_map.items() if p.startswith(k)]
        urls.append("https://support.juniper.net/support/eol/hardware/")
        urls.append("https://support.juniper.net/support/eol/")

        for url in urls:
            result = self._scrape_table_smart(part_code, "Juniper", url)
            if _has_dates(result):
                return result
        return None

    # ── HP ARUBA ─────────────────────────────────────────────────── #

    def _aruba(self, part_code: str) -> Optional[EOLRecord]:
        urls = [
            "https://www.arubanetworks.com/support-services/end-of-life/",
            "https://www.hpe.com/h20195/v2/Getdocument.aspx?docname=c04533547",
            "https://support.hpe.com/connect/s/softwaredetails?language=en_US&section=RELEASE",
        ]
        p = part_code.upper()
        # HPE Aruba switch category pages
        if any(p.startswith(x) for x in ("JL", "J9", "J8")):
            urls.insert(0, "https://www.hpe.com/h20195/v2/Getdocument.aspx?docname=c04531932")

        for url in urls:
            result = self._scrape_table_smart(part_code, "HP Aruba", url)
            if _has_dates(result):
                return result
        return None

    # ── ARISTA ───────────────────────────────────────────────────── #

    def _arista(self, part_code: str) -> Optional[EOLRecord]:
        url = "https://www.arista.com/en/support/product-lifecycle"
        html = self._get_html(url)
        if html:
            # Arista embeds JSON data in script tags
            for script in BeautifulSoup(html, "html.parser").find_all("script"):
                txt = script.string or ""
                if part_code.upper() in txt.upper():
                    eos  = re.search(rf'{re.escape(part_code)}.*?"endOfSale"\s*:\s*"([^"]+)"', txt, re.I | re.S)
                    eol  = re.search(rf'{re.escape(part_code)}.*?"endOfSupport"\s*:\s*"([^"]+)"', txt, re.I | re.S)
                    repl = re.search(rf'{re.escape(part_code)}.*?"replacement"\s*:\s*"([^"]+)"', txt, re.I | re.S)
                    if eos or eol:
                        return EOLRecord(
                            part_code=part_code, vendor="Arista", model=part_code,
                            end_of_sale=parse_date(eos.group(1) if eos else ""),
                            end_of_support=parse_date(eol.group(1) if eol else ""),
                            replacement_sku=repl.group(1) if repl else "",
                            source_url=url, confidence="medium",
                        )
        return self._scrape_table_smart(part_code, "Arista", url)

    # ── DELL ─────────────────────────────────────────────────────── #

    def _dell(self, part_code: str) -> Optional[EOLRecord]:
        urls = [
            "https://www.dell.com/en-us/dt/corporate/about-us/end-of-life-notices.htm",
            "https://www.dell.com/support/home/en-us",
        ]
        for url in urls:
            result = self._scrape_table_smart(part_code, "Dell", url)
            if _has_dates(result):
                return result
        return None

    # ── FORTINET ─────────────────────────────────────────────────── #

    def _fortinet(self, part_code: str) -> Optional[EOLRecord]:
        """
        Multiple strategies for Fortinet EOL data.
        The main lifecycle page is ASP.NET; we try GET then POST.
        """
        p = part_code.upper()
        # Build alt codes to try
        alt_codes = [p]
        if not p.startswith(("FG-", "FGR-", "FWF-", "FS-")):
            alt_codes.append("FG-" + p)
        model_only = p.replace("FG-", "").replace("FGR-", "").replace("FWF-", "")
        if model_only != p:
            alt_codes.append(model_only)

        lifecycle_url = "https://support.fortinet.com/Information/ProductLifeCycle.aspx"

        # Strategy 1: direct GET (sometimes the ASP.NET page renders table in HTML)
        for code in alt_codes:
            result = self._scrape_table_smart(code, "Fortinet", lifecycle_url,
                                              alt_codes=alt_codes)
            if _has_dates(result):
                return result

        # Strategy 2: POST with ViewState (proper ASP.NET form submission)
        result = self._fortinet_post(model_only, alt_codes)
        if _has_dates(result):
            return result

        # Strategy 3: Fortinet's JSON-based product list if exposed
        result = self._fortinet_json(model_only)
        if _has_dates(result):
            return result

        return None

    def _fortinet_post(self, model: str, alt_codes: list) -> Optional[EOLRecord]:
        """Submit ASP.NET form to Fortinet lifecycle page."""
        url = "https://support.fortinet.com/Information/ProductLifeCycle.aspx"
        html = self._get_html(url)
        if not html:
            return None
        soup = BeautifulSoup(html, "html.parser")
        vs   = soup.find("input", {"id": "__VIEWSTATE"})
        ev   = soup.find("input", {"id": "__EVENTVALIDATION"})
        if not vs:
            return None
        try:
            payload = {
                "__VIEWSTATE":       vs.get("value", ""),
                "__EVENTVALIDATION": ev.get("value", "") if ev else "",
                "__EVENTTARGET":     "",
                "__EVENTARGUMENT":   "",
                "ctl00$ContentPlaceHolder1$txtSearch": model,
                "ctl00$ContentPlaceHolder1$btnSearch": "Search",
            }
            resp = self.session.post(url, data=payload,
                                     timeout=self.REQUEST_TIMEOUT,
                                     allow_redirects=True)
            self._last_req = time.time()
            if resp.status_code == 200:
                # Parse response table
                for code in alt_codes:
                    result = self._parse_table_response(resp.text, code, "Fortinet", url)
                    if _has_dates(result):
                        return result
        except Exception as e:
            print(f"      [Fortinet POST] {e}")
        return None

    def _fortinet_json(self, model: str) -> Optional[EOLRecord]:
        """Try Fortinet's product inquiry endpoint if it exists."""
        urls = [
            f"https://support.fortinet.com/Information/ProductLifeCycleJSON.aspx?model={model}",
            f"https://support.fortinet.com/api/eol?model={model}",
        ]
        for url in urls:
            r = self._get_raw(url)
            if r and r.status_code == 200:
                try:
                    data = r.json()
                    if isinstance(data, dict):
                        eos = parse_date(data.get("EndOfSale") or data.get("eos") or "")
                        eol = parse_date(data.get("EndOfSupport") or data.get("eol") or "")
                        if eos or eol:
                            return EOLRecord(
                                part_code=model, vendor="Fortinet", model=model,
                                end_of_sale=eos, end_of_support=eol,
                                source_url=url, confidence="high",
                            )
                except Exception:
                    pass
        return None

    # ── PALO ALTO ────────────────────────────────────────────────── #

    def _paloalto(self, part_code: str) -> Optional[EOLRecord]:
        urls = [
            "https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware",
            "https://live.paloaltonetworks.com/t5/customer-resources/palo-alto-networks-official-support-announcements-hardware/ta-p/302614",
            "https://docs.paloaltonetworks.com/hardware/hardware-reference/hardware-eof",
        ]
        p = part_code.upper()
        alt = [p]
        if p.startswith("PA-"):
            alt.append(p[3:])           # "460" from "PA-460"
        elif not p.startswith("PA-"):
            alt.append("PA-" + p)

        for url in urls:
            result = self._scrape_table_smart(part_code, "Palo Alto", url, alt_codes=alt)
            if _has_dates(result):
                return result
        return None

    # ── EXTREME NETWORKS ─────────────────────────────────────────── #

    def _extreme(self, part_code: str) -> Optional[EOLRecord]:
        urls = [
            "https://www.extremenetworks.com/support/end-of-life/",
            "https://extremeportal.force.com/ExtrSupportHome",
            "https://documentation.extremenetworks.com/eos/",
        ]
        p = part_code.upper()
        alt = [p, p.replace("SUMMIT ", "").replace("SUMMIT-", "")]
        for url in urls:
            result = self._scrape_table_smart(part_code, "Extreme Networks", url, alt_codes=alt)
            if _has_dates(result):
                return result
        return None

    # ── SOPHOS ───────────────────────────────────────────────────── #

    def _sophos(self, part_code: str) -> Optional[EOLRecord]:
        """
        Sophos lifecycle calendar.
        Official page (KBA-000003353) is a Salesforce SPA — use the static
        HTML mirrors that republish the same table data.
        Columns: Product | Release date | End-of-Sale | Last Renewal | End-of-Life | Successor
        """
        p = part_code.upper().strip()

        # Build alt codes to handle spacing variants: XGS2100 ↔ XGS 2100 ↔ XGS-2100
        alt_codes = [p]
        m = re.match(r'^(XGS|XG|SG|APX|RED|AP)\s*[-]?\s*(\d+)', p)
        if m:
            series, num = m.group(1), m.group(2)
            alt_codes += [f"{series} {num}", f"{series}{num}", f"{series}-{num}"]
        alt_codes = list(dict.fromkeys(alt_codes))  # deduplicate, preserve order

        urls = [
            # Third-party static mirror — full table with EOS/EOL dates
            "https://www.avanet.com/en/kb/sophos-product-lifecycle-calendar-end-of-sale-end-of-life/",
            # Sophos community wiki (may render as static HTML)
            "https://community.sophos.com/kb/en-us/121502",
            # Official lifecycle hub (links out, but sometimes has inline content)
            "https://www.sophos.com/en-us/support/lifecycle",
        ]
        for url in urls:
            result = self._scrape_table_smart(part_code, "Sophos", url,
                                              alt_codes=alt_codes)
            if _has_dates(result):
                return result
        return None

    # ── UBIQUITI ─────────────────────────────────────────────────── #

    def _ubiquiti(self, part_code: str) -> Optional[EOLRecord]:
        """
        Ubiquiti Vintage/Legacy product list.
        Official page requires SSO — try the Zendesk public article API first.
        No EOL dates are published; a match marks the device as discontinued
        (confidence=low, no dates → status UNKNOWN, which is honest).
        """
        p = part_code.upper().strip()
        alt_codes = [p, p.replace("-", " "), p.replace("_", "-"),
                     p.replace("USW-", "US-"), p.replace("US-", "USW-")]
        alt_codes = list(dict.fromkeys(alt_codes))

        # Direct article page — publicly accessible, no login required
        article_url = "https://help.ui.com/hc/en-us/articles/1500001268521"
        r = self._get_raw(article_url)
        if r and r.status_code == 200:
            html = r.text
            html_upper = html.upper()
            for code in alt_codes:
                idx = html_upper.find(code)
                if idx >= 0:
                    ctx = html_upper[max(0, idx - 300): idx + 300]
                    label = "Legacy" if "LEGACY" in ctx else "Vintage"
                    print(f"    [UBIQUITI] {part_code} found in {label} list")
                    repl = ""
                    for row in BeautifulSoup(html, "html.parser").find_all("tr"):
                        cells = [c.get_text(" ", strip=True) for c in row.find_all(["td", "th"])]
                        if any(c in " ".join(cells).upper() for c in alt_codes):
                            candidates = [c for c in cells[1:] if c and c.upper() not in alt_codes]
                            repl = candidates[-1] if candidates else ""
                            break
                    return EOLRecord(
                        part_code=part_code, vendor="Ubiquiti",
                        model=part_code,
                        replacement_name=repl or f"Ubiquiti {label} — no longer manufactured",
                        source_url=article_url,
                        confidence="low",
                    )

        return None

    # ── MIKROTIK ─────────────────────────────────────────────────── #

    def _mikrotik(self, part_code: str) -> Optional[EOLRecord]:
        """
        MikroTik does not publish a structured EOL table or dates.
        Strategy: scan mikrotik.com/products for the part code in the page
        source (the JS-rendered product grid embeds SKUs in script data),
        then check if the surrounding context flags it as archived.
        Falls back to a third-party EOL aggregator.
        """
        p = part_code.upper().strip()

        # Normalise RB-prefix variants: RB750Gr3 / RB-750Gr3 / 750Gr3
        alt_codes = [p]
        clean = re.sub(r'^RB[-]?', '', p)
        if clean != p:
            alt_codes += [f"RB{clean}", f"RB-{clean}", clean]
        alt_codes = list(dict.fromkeys(alt_codes))

        # 1. mikrotik.com products page — SKUs appear in the page source
        products_url = "https://mikrotik.com/products"
        r = self._get_raw(products_url)
        if r and r.status_code == 200:
            html = r.text
            for code in alt_codes:
                idx = html.upper().find(code)
                if idx >= 0:
                    ctx = html[max(0, idx - 300): idx + 600].lower()
                    if "archived" in ctx or "discontinued" in ctx or "end of life" in ctx:
                        print(f"    [MIKROTIK] {part_code} found as archived on mikrotik.com")
                        return EOLRecord(
                            part_code=part_code, vendor="MikroTik",
                            model=part_code,
                            replacement_name="MikroTik archived — no longer in production",
                            source_url=products_url,
                            confidence="low",
                        )

        # 2. Third-party EOL aggregator (limited coverage, sometimes has dates)
        se_url = "https://serviceexpress.com/eol-eosl-database/oem/mikrotik/"
        result = self._scrape_table_smart(part_code, "MikroTik", se_url,
                                          alt_codes=alt_codes)
        if _has_dates(result):
            return result

        return None

    # ── PEPLINK / PEPWAVE ─────────────────────────────────────────── #

    def _peplink(self, part_code: str) -> Optional[EOLRecord]:
        """
        Peplink officially does not publish EOL dates.
        peplinkworks.com maintains a community discontinued-SKU table
        (Description / SKU / Replacement). No dates, but a match confirms
        the product is discontinued (returned with confidence=low).
        """
        p = part_code.upper().strip()
        alt_codes = [p, p.replace("-", " "), p.replace("_", "-"),
                     re.sub(r'\s+', '-', p)]
        alt_codes = list(dict.fromkeys(alt_codes))

        # 1. Community discontinued SKU table
        # Columns: Description | SKU | Replacement Description | (optional) Replacement SKU
        eol_url = "https://www.peplinkworks.com/peplink-eol.asp"
        r = self._get_raw(eol_url)
        if r and r.status_code == 200:
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
                    print(f"    [PEPLINK] {part_code} found in discontinued list")
                    return EOLRecord(
                        part_code=part_code, vendor="Peplink",
                        model=cells[0].strip(),
                        replacement_sku=repl_sku,
                        replacement_name=repl_name or "Peplink discontinued — no dates published",
                        source_url=eol_url,
                        confidence="low",
                    )

        # 2. Official legacy products page
        legacy_url = "https://www.peplink.com/legacy-products/"
        result = self._scrape_table_smart(part_code, "Peplink", legacy_url,
                                          alt_codes=alt_codes)
        if result:
            return result

        return None

    # ── STARLINK ─────────────────────────────────────────────────── #

    def _starlink(self, part_code: str) -> Optional[EOLRecord]:
        return EOLRecord(
            part_code=part_code, vendor="Starlink",
            model=part_code,
            source_url="https://www.starlink.com/support",
            confidence="low",
        )

    # ── Smart table scraper ───────────────────────────────────────── #

    def _scrape_table_smart(self, part_code: str, vendor: str, url: str,
                             alt_codes: list = None,
                             post_data: dict = None) -> Optional[EOLRecord]:
        """
        Fetch a page and search all HTML tables for a matching part code row.
        - Detects EOS/EOL columns from header text
        - Tries exact + normalized (no-dash, no-space) matching
        - Falls back to text-proximity date extraction
        """
        html = self._get_html(url) if not post_data else None
        if post_data:
            r = self._get_raw(url, method="POST", data=post_data)
            html = r.text if r else None
        if not html:
            return None

        codes = [part_code.upper()]
        if alt_codes:
            codes.extend(c.upper() for c in alt_codes)

        soup = BeautifulSoup(html, "html.parser")

        for table in soup.find_all("table"):
            rows = table.find_all("tr")
            if len(rows) < 2:
                continue

            # Parse headers from first non-empty row
            header_cells = rows[0].find_all(["th", "td"])
            headers = [c.get_text(strip=True).lower() for c in header_cells]

            eos_col  = self._find_col(headers, ["end of sale", "eos", "end-of-sale", "end of availability"])
            eol_col  = self._find_col(headers, ["end of support", "eol", "end-of-life", "end of life",
                                                  "last date of support", "last support"])
            repl_col = self._find_col(headers, ["replacement", "successor", "migrate to",
                                                  "migration", "substitute"])

            # Default columns if headers undetected
            if eos_col is None and eol_col is None:
                eos_col, eol_col = 1, 2
            elif eos_col is None:
                eos_col = max(0, (eol_col or 2) - 1)
            elif eol_col is None:
                eol_col = eos_col + 1

            for row in rows[1:]:
                cells = [c.get_text(" ", strip=True) for c in row.find_all(["td", "th"])]
                if not cells:
                    continue
                row_text = " ".join(cells).upper()
                row_norm = row_text.replace("-", "").replace(" ", "")

                matched = any(
                    code in row_text or
                    code.replace("-", "").replace(" ", "") in row_norm
                    for code in codes
                )
                if not matched:
                    continue

                eos  = parse_date(cells[eos_col])  if eos_col  < len(cells) else None
                eol  = parse_date(cells[eol_col])  if eol_col  < len(cells) else None
                repl = (cells[repl_col].strip()
                        if repl_col is not None and repl_col < len(cells) else "")

                if eos or eol:
                    return EOLRecord(
                        part_code=part_code, vendor=vendor,
                        model=cells[0].strip(),
                        end_of_sale=eos, end_of_support=eol,
                        replacement_sku=repl,
                        source_url=url, confidence="medium",
                    )

        # Fallback: text proximity scan
        return self._text_scan_dates(html, part_code, vendor, url, codes)

    def _parse_table_response(self, html: str, part_code: str,
                               vendor: str, url: str) -> Optional[EOLRecord]:
        """Parse a table from raw HTML (used after POST responses)."""
        return self._scrape_table_smart(part_code, vendor, url,
                                        post_data=None) if False else \
               self._text_scan_dates(html, part_code, vendor, url,
                                     [part_code.upper()])

    @staticmethod
    def _find_col(headers: list, keywords: list) -> Optional[int]:
        for i, h in enumerate(headers):
            if any(kw in h for kw in keywords):
                return i
        return None

    def _text_scan_dates(self, html: str, part_code: str, vendor: str,
                          url: str, codes: list) -> Optional[EOLRecord]:
        """Last-resort: find part code in raw text and extract nearby dates."""
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(" ")
        tu   = text.upper()

        date_re = re.compile(
            r'\b(\d{4}-\d{2}-\d{2}'
            r'|\w+ \d{1,2},? \d{4}'
            r'|\d{1,2}[/-]\d{1,2}[/-]\d{4}'
            r'|\w+ \d{4})\b',
            re.I
        )

        for code in codes:
            idx = tu.find(code)
            if idx < 0:
                norm = code.replace("-", "").replace(" ", "")
                norm_t = tu.replace("-", "").replace(" ", "")
                ni = norm_t.find(norm)
                if ni < 0:
                    continue
                idx = ni

            nearby = text[max(0, idx - 80): idx + 500]
            found_dates = []
            for m in date_re.finditer(nearby):
                d = parse_date(m.group(1))
                if d and date(2000, 1, 1) <= d <= date(2045, 12, 31):
                    found_dates.append(d)

            if found_dates:
                return EOLRecord(
                    part_code=part_code, vendor=vendor, model=part_code,
                    end_of_sale=found_dates[0],
                    end_of_support=found_dates[1] if len(found_dates) > 1 else None,
                    source_url=url, confidence="low",
                )

        return None

    # ── HTTP helpers ─────────────────────────────────────────────── #

    def _get_html(self, url: str) -> Optional[str]:
        """Fetch HTML with shared in-memory caching (prevents duplicate requests)."""
        with _html_lock:
            if url in _html_cache:
                return _html_cache[url]
        r = self._get_raw(url)
        if r:
            with _html_lock:
                _html_cache[url] = r.text
            return r.text
        return None

    def _get(self, url: str, retries: int = 2) -> Optional[requests.Response]:
        return self._get_raw(url, retries=retries)

    def _get_raw(self, url: str, retries: int = 2,
                 method: str = "GET", data: dict = None) -> Optional[requests.Response]:
        if not self.use_web:
            return None
        for attempt in range(retries + 1):
            elapsed = time.time() - self._last_req
            if elapsed < self.rate_limit_s:
                time.sleep(self.rate_limit_s - elapsed)
            try:
                if method.upper() == "POST":
                    r = self.session.post(url, data=data or {},
                                          timeout=self.REQUEST_TIMEOUT,
                                          allow_redirects=True)
                else:
                    r = self.session.get(url, timeout=self.REQUEST_TIMEOUT,
                                         allow_redirects=True)
                self._last_req = time.time()
                if r.status_code in (200, 206):
                    return r
                if r.status_code == 429:
                    time.sleep(2 ** attempt * 3)
                    continue
                if r.status_code >= 500 and attempt < retries:
                    time.sleep(1.5 ** attempt)
                    continue
            except requests.exceptions.Timeout:
                if attempt < retries:
                    time.sleep(0.5)
            except requests.exceptions.ConnectionError:
                if attempt < retries:
                    time.sleep(1)
            except requests.exceptions.RequestException:
                break
        return None
