# EOL Agent Master — Architecture & Requirements Analysis

## What It Is

**EOL Agent v3.0** — an End-of-Life/End-of-Support intelligence platform for network device inventory. It tracks when network hardware goes out of support, identifies at-risk devices, and generates reports.

---

## Requirements

### Python Dependencies (requirements.txt)

| Package | Purpose |
|---|---|
| `flask>=3.0.0` | REST API + web server |
| `flask-cors>=4.0.0` | Cross-origin requests |
| `requests>=2.31.0` | HTTP client for vendor portals |
| `beautifulsoup4>=4.12.0` + `lxml>=5.0.0` | HTML scraping of vendor pages |
| `openpyxl>=3.1.0` | Excel report generation |
| `python-dotenv>=1.0.0` | `.env` config loading |

### Database

- **SQLite3** (built into Python, no install needed)
- File: `data/eol_cache.db`
- Two tables:
  - `eol_cache` — lookup results with 24h TTL
  - `scan_history` — full scan snapshots for history/restore

```sql
CREATE TABLE eol_cache (
    part_code TEXT PRIMARY KEY,
    vendor TEXT,
    data_json TEXT NOT NULL,
    cached_at TEXT NOT NULL,
    source TEXT
);

CREATE TABLE scan_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_at TEXT NOT NULL,
    source TEXT,
    device_count INTEGER,
    stats_json TEXT,
    at_risk_json TEXT,
    safe_json TEXT
);
```

### External Services (optional)

| Service | Purpose | Auth Required |
|---|---|---|
| ServiceNow CMDB | Pull device inventory | Yes (`SNOW_URL`, `SNOW_USER`, `SNOW_PASSWORD`) |
| endoflife.date API | Community EOL database | No (free public API) |
| Cisco vendor portal | Live EOL scraping | No |
| Juniper vendor portal | Live EOL scraping | No |
| HP Aruba vendor portal | Live EOL scraping | No |
| Arista vendor portal | Live EOL scraping | No |
| Dell vendor portal | Live EOL scraping | No |
| Fortinet vendor portal | Live EOL scraping | No |
| Palo Alto vendor portal | Live EOL scraping | No |
| Extreme Networks portal | Live EOL scraping | No |
| Starlink | Hardcoded lifecycle data | No |

### Environment Variables (.env)

```
FLASK_PORT=8080              # Web server port (default 8080)
FLASK_DEBUG=false            # Debug mode
SNOW_URL=https://yourco.service-now.com
SNOW_USER=api_user
SNOW_PASSWORD=secret
SNOW_TABLE=cmdb_ci_netgear   # CMDB table name
CACHE_TTL_HOURS=24           # EOL lookup cache TTL
```

---

## Project Structure

```
eol_agent_master/
├── app.py                      # Flask API server (REST endpoints + web UI)
├── run_agent.py                # CLI runner (batch processing)
├── requirements.txt            # Python dependencies
├── README.md                   # Documentation
├── .env.example                # Configuration template
├── core/
│   ├── __init__.py
│   ├── models.py               # Data models (Device, EOLRecord, AnalysisResult)
│   ├── servicenow.py           # ServiceNow CMDB connector
│   ├── researcher.py           # EOL lookup engine (4-layer priority)
│   ├── analyser.py             # EOL scoring & risk categorization
│   ├── cache.py                # SQLite persistence for results & history
│   ├── live_scraper.py         # Live vendor portal scrapers
│   ├── eol_database.py         # Local curated EOL DB (120+ records)
│   ├── endoflife_api.py        # Free endoflife.date API wrapper
│   └── master_eol_db.py        # Master asset data mapping
├── reports/
│   ├── __init__.py
│   └── excel_report.py         # Excel report generator (3-sheet workbook)
├── frontend/
│   └── index.html              # Web UI (HTML/CSS/JS)
├── data/
│   └── eol_cache.db            # SQLite: cached EOL lookups & scan history
└── output/                     # Generated Excel reports
```

---

## How It Works — End to End

### 1. Inventory Loading

Three ways to load devices:

- **ServiceNow CMDB** — REST API call to query `cmdb_ci_netgear` table
- **Excel upload** — Smart column auto-detection with fuzzy matching for headers like "Model ID", "Hostname", "IP Address", etc.
- **Demo data** — 48 hardcoded sample devices for testing

### 2. EOL Lookup (per device — 4-layer priority)

For each device's part code, `core/researcher.py` tries in order:

```
1. SQLite cache       →  hit? return immediately (if < 24h old)
2. Local DB           →  120+ curated vendor EOL bulletin records
3. endoflife.date API →  free community-maintained database
4. Live scraping      →  real-time HTML parse of vendor portal
5. UNKNOWN            →  no data found anywhere
```

Vendor is **auto-inferred** from part code patterns:
- `WS-C` → Cisco
- `EX-` → Juniper
- `FG-` → Fortinet
- `MR` / `MS` / `MX` → Cisco Meraki
- `PA-` → Palo Alto
- `JN-` → Juniper

### 3. Risk Scoring (core/analyser.py)

Each device gets a status based on days until End-of-Support:

| Status | Condition | Days Remaining |
|---|---|---|
| **EXPIRED** | EOS date already passed | < 0 |
| **CRITICAL** | Urgent action needed | ≤ 180 (6 months) |
| **WARNING** | Plan replacement | ≤ 365 (12 months) |
| **MONITOR** | Next refresh cycle | ≤ 730 (24 months) |
| **SAFE** | No immediate action | > 730 (2+ years) |
| **UNKNOWN** | No EOL data found | N/A |

Primary risk date = `end_of_support`; falls back to `end_of_sale` if not available.

### 4. Parallel Processing

- Scans run in background using `ThreadPoolExecutor`
- **15 workers** for local DB lookups
- **4 workers** for live web scraping (rate-limited to avoid bans)
- Progress streamed to browser via **Server-Sent Events (SSE)** at `GET /api/analyse/stream`

### 5. Output

- **Web UI** at `http://localhost:8080` — real-time progress dashboard
- **Excel report** — 3-sheet workbook:
  - Sheet 1: At-Risk Devices (color-coded red/amber/yellow by severity)
  - Sheet 2: Safe Devices
  - Sheet 3: Executive Summary with KPI table and bar chart
- **SQLite history** — all scans persisted, restorable on restart
- **ServiceNow write-back** (optional) — pushes EOL status + replacement SKU back to CMDB

---

## Core Module Breakdown

### models.py — Data Models

```
Device          → sys_id, name, part_code, vendor, model, serial, ip, location, qty
EOLRecord       → part_code, end_of_sale, end_of_support, replacement_sku, source_url, confidence
AnalysisResult  → device + eol + status + days_left + risk_date + notes
EOLStatus       → EXPIRED / CRITICAL / WARNING / MONITOR / SAFE / UNKNOWN (Enum)
```

### servicenow.py — CMDB Connector

- `test_connection()` — verify credentials
- `get_network_devices(limit, table)` — query devices from CMDB
- `update_eol_status(sys_id, status, replacement_sku)` — write EOL status back

### researcher.py — EOL Lookup Engine

- 4-layer lookup priority (cache → local DB → API → live scrape)
- Smart HTML table parser: fuzzy header matching, 20+ date format support
- Handles exact + normalized part code matching (no-dash, no-space variants)

### analyser.py — Scoring Engine

- `analyse_one(device)` → single device EOL lookup + risk score
- `analyse_all(devices)` → batch with progress logging
- `split_results(results)` → (at_risk_list, safe_list)
- `summary_stats(results)` → KPI dict for dashboard

### cache.py — SQLite Persistence

- `get_cached_eol(part_code, ttl_hours)` — fetch cached lookup
- `set_cached_eol(part_code, vendor, record, source)` — store result
- `save_scan(...)` — persist full scan to history
- `get_latest_scan()` — restore last completed scan on startup

### excel_report.py — Report Generator

- Color-coded rows (red = expired/critical, amber = warning, yellow = monitor)
- Frozen panes, auto-filter, alternating row colors
- Executive summary with embedded bar chart
- Optional vendor/company filters on export

---

## Flask API Routes (app.py)

| Method | Route | Purpose |
|---|---|---|
| GET | `/` | Serve web UI |
| GET | `/api/status` | Server version & scan state |
| GET | `/api/vendors` | List of 10 supported vendors |
| POST | `/api/connect/servicenow` | Test & store CMDB credentials |
| GET | `/api/devices` | Load devices (ServiceNow or demo) |
| POST | `/api/upload/excel` | Parse Excel inventory file |
| GET | `/api/upload/status` | Preview uploaded file |
| POST | `/api/lookup` | Ad-hoc single part code lookup |
| POST | `/api/analyse` | Start background EOL scan |
| GET | `/api/analyse/stream` | SSE stream for real-time progress |
| GET | `/api/analyse/status` | Polling fallback for scan status |
| GET | `/api/scans/history` | List past scans from SQLite |
| GET | `/api/report/excel` | Download Excel report |

---

## Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Start web server (UI + API at http://localhost:8080)
python app.py

# CLI batch mode (demo data, local DB)
python run_agent.py

# CLI batch mode (ServiceNow + live scraping + write-back)
python run_agent.py --snow --url https://yourco.service-now.com \
  --user api_user --password secret --writeback --live
```

---

## Architecture Diagram

```
┌─────────────────────────────────────────────┐
│             app.py  (Flask API)             │
│   /api/devices  /api/analyse  /api/report   │
└──────────────────┬──────────────────────────┘
                   │
        ┌──────────▼──────────┐
        │  core/analyser.py   │  ← orchestrates per-device scoring
        └──────────┬──────────┘
                   │  (ThreadPoolExecutor: 15 local / 4 live workers)
        ┌──────────▼──────────────────────────────┐
        │         core/researcher.py              │
        │  1.cache → 2.localDB → 3.API → 4.scrape │
        └───┬──────────┬──────────┬───────────────┘
            │          │          │
       SQLite DB    eol_database  endoflife_api.py
       (cache.py)   (120 records) (free public API)
                                  │
                             live_scraper.py
                          (9 vendor portals scraped live)
```

---

*Analysis generated on 2026-05-09*
