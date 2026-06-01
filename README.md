# Network EOL Intelligence Agent v2.0

A full-stack agent that fetches real-time EOL/EOS data from vendor portals,
analyses your network inventory, and generates reports.

## Supported Vendors (9)
Cisco · Juniper · HP Aruba · Arista · Dell · Fortinet · Palo Alto · Extreme Networks · Starlink

## Quick Start

### 1. Install dependencies
```bash
pip install flask flask-cors requests beautifulsoup4 openpyxl
```

### 2. Start the server
```bash
cd eol_agent
python app.py
```
Open http://localhost:5000 in your browser.

### 3. Run a scan
- Go to **Run Scan** in the sidebar
- Choose **"Built-in sample inventory"** (no setup needed) or **ServiceNow CMDB**
- Choose **"Local DB only"** (fast) or **"Live vendor portals"** (real-time)
- Click **Start Scan**

---

## ServiceNow Connection
**Where to configure:** `core/servicenow.py` — or use the ServiceNow panel in the UI

1. Enter your instance URL: `https://yourco.service-now.com`
2. Enter username + password (read access to CMDB is sufficient)
3. Select the CMDB table (`cmdb_ci_netgear` recommended for network gear)
4. Click **Test & Connect**

### Required CMDB fields
| Field | Purpose |
|---|---|
| `name` | Device hostname |
| `model_number` or `u_part_code` | Part code for EOL lookup |
| `manufacturer` | Vendor name |
| `serial_number` | Serial |
| `ip_address` | IP |
| `location` | Site/floor |

### Optional write-back fields (add these to your CMDB table)
| Field | Value written |
|---|---|
| `u_eol_status` | EOL status string |
| `u_replacement_sku` | Recommended replacement part code |

---

## Live EOL Data Sources
Each vendor has its own scraper hitting the real portal:

| Vendor | Portal | Method |
|---|---|---|
| Cisco | `api.cisco.com/supporttools/eox` | REST API |
| Juniper | `support.juniper.net/support/eol/hardware/` | HTML Table |
| HP Aruba | `arubanetworks.com/support-services/end-of-life/` | HTML Table |
| Arista | `arista.com/en/support/product-lifecycle` | JSON + HTML |
| Dell | `dell.com/.../end-of-life-notices.htm` | HTML Table |
| Fortinet | `endoflife.date/api/fortigate.json` | REST API |
| Palo Alto | `paloaltonetworks.com/.../end-of-life-announcements/hardware` | HTML Table |
| Extreme Networks | `extremenetworks.com/support/end-of-life/` | HTML Table |
| Starlink | `starlink.com/hardware` | Web Scrape |

**Important:** Live mode requires internet access to these portals.
Local DB mode uses the curated database in `core/eol_database.py` (120+ records, no internet needed).

---

## Project Structure
```
eol_agent/
├── app.py                  # Flask API server  ← START HERE
├── frontend/
│   └── index.html          # Full web UI
├── core/
│   ├── models.py           # Data models (Device, EOLRecord, AnalysisResult)
│   ├── servicenow.py       # ServiceNow CMDB connector  ← SNOW CONFIG
│   ├── eol_database.py     # Local curated EOL DB (120+ records, 9 vendors)
│   ├── live_scraper.py     # Real-time vendor portal scrapers  ← LIVE DATA
│   ├── researcher.py       # Lookup engine (DB → live → fallback)
│   └── analyser.py         # Scoring engine
├── reports/
│   └── excel_report.py     # Excel report generator (3 sheets)
└── run_agent.py            # CLI runner (no UI needed)
```

## CLI Usage (no UI)
```bash
# Demo mode (48 sample devices, local DB)
python run_agent.py

# With ServiceNow + live vendor portals
python run_agent.py --snow \
  --url https://yourco.service-now.com \
  --user api_user \
  --password secret \
  --writeback
```
