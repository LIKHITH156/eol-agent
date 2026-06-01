"""
SQLite-backed cache for EOL lookup results and scan history.
Persists across server restarts — no more lost state on reload.
"""

import sqlite3
import json
import os
import threading
from datetime import datetime, timedelta, date
from typing import Optional

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "eol_cache.db")
_lock = threading.Lock()


def _connect():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with _lock, _connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS eol_cache (
                part_code  TEXT PRIMARY KEY,
                vendor     TEXT,
                data_json  TEXT NOT NULL,
                cached_at  TEXT NOT NULL,
                source     TEXT
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS scan_history (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                run_at       TEXT NOT NULL,
                source       TEXT,
                device_count INTEGER,
                stats_json   TEXT,
                at_risk_json TEXT,
                safe_json    TEXT
            )
        """)
        conn.commit()


init_db()

# ── EOL lookup cache ──────────────────────────────────────────── #

def get_cached_eol(part_code: str, ttl_hours: int = 24) -> Optional[dict]:
    with _lock, _connect() as conn:
        row = conn.execute(
            "SELECT data_json, cached_at FROM eol_cache WHERE part_code = ?",
            (part_code.upper(),),
        ).fetchone()
    if not row:
        return None
    data_json, cached_at = row
    age = datetime.now() - datetime.fromisoformat(cached_at)
    if age > timedelta(hours=ttl_hours):
        return None
    return json.loads(data_json)


def set_cached_eol(part_code: str, vendor: str, record, source: str = "web"):
    """Serialize an EOLRecord and store it in the cache."""
    data = _record_to_dict(record)
    with _lock, _connect() as conn:
        conn.execute(
            """INSERT OR REPLACE INTO eol_cache
               (part_code, vendor, data_json, cached_at, source)
               VALUES (?, ?, ?, ?, ?)""",
            (part_code.upper(), vendor, json.dumps(data),
             datetime.now().isoformat(), source),
        )
        conn.commit()


def dict_to_eolrecord(data: dict):
    from core.models import EOLRecord
    def _d(s): return date.fromisoformat(s) if s else None
    return EOLRecord(
        part_code=data.get("part_code", ""),
        vendor=data.get("vendor", ""),
        model=data.get("model", ""),
        end_of_sale=_d(data.get("end_of_sale")),
        end_of_support=_d(data.get("end_of_support")),
        end_of_sw_maint=_d(data.get("end_of_sw_maint")),
        replacement_sku=data.get("replacement_sku", ""),
        replacement_name=data.get("replacement_name", ""),
        migration_url=data.get("migration_url", ""),
        source_url=data.get("source_url", ""),
        confidence=data.get("confidence", "high"),
    )


def _record_to_dict(record) -> dict:
    def _s(d): return d.isoformat() if d else None
    return {
        "part_code":       record.part_code,
        "vendor":          record.vendor,
        "model":           record.model,
        "end_of_sale":     _s(record.end_of_sale),
        "end_of_support":  _s(record.end_of_support),
        "end_of_sw_maint": _s(record.end_of_sw_maint),
        "replacement_sku":  record.replacement_sku,
        "replacement_name": record.replacement_name,
        "migration_url":    record.migration_url,
        "source_url":       record.source_url,
        "confidence":       record.confidence,
    }


# ── Scan history ──────────────────────────────────────────────── #

def save_scan(source: str, device_count: int, stats: dict,
              at_risk_json: list, safe_json: list):
    with _lock, _connect() as conn:
        conn.execute(
            """INSERT INTO scan_history
               (run_at, source, device_count, stats_json, at_risk_json, safe_json)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (
                datetime.now().isoformat(), source, device_count,
                json.dumps(stats),
                json.dumps(at_risk_json),
                json.dumps(safe_json),
            ),
        )
        conn.commit()


def get_latest_scan() -> Optional[dict]:
    with _lock, _connect() as conn:
        row = conn.execute(
            """SELECT run_at, source, device_count, stats_json, at_risk_json, safe_json
               FROM scan_history ORDER BY id DESC LIMIT 1"""
        ).fetchone()
    if not row:
        return None
    run_at, source, device_count, stats_json, at_risk_json, safe_json = row
    return {
        "run_at":       run_at,
        "source":       source,
        "device_count": device_count,
        "stats":        json.loads(stats_json),
        "at_risk":      json.loads(at_risk_json),
        "safe":         json.loads(safe_json),
    }


def get_scan_history(limit: int = 20) -> list:
    with _lock, _connect() as conn:
        rows = conn.execute(
            """SELECT id, run_at, source, device_count, stats_json
               FROM scan_history ORDER BY id DESC LIMIT ?""",
            (limit,),
        ).fetchall()
    result = []
    for row_id, run_at, source, device_count, stats_json in rows:
        result.append({
            "id":           row_id,
            "run_at":       run_at,
            "source":       source,
            "device_count": device_count,
            "stats":        json.loads(stats_json),
        })
    return result


# ── Result serialization helpers ──────────────────────────────── #

def result_to_dict(r) -> dict:
    """Serialize an AnalysisResult to a JSON-safe dict."""
    d = r.device
    e = r.eol
    return {
        "device": {
            "sys_id":      d.sys_id,
            "name":        d.name,
            "part_code":   d.part_code,
            "vendor":      d.vendor,
            "model":       d.model,
            "serial":      d.serial,
            "ip_address":  d.ip_address,
            "location":    d.location,
            "assigned_to": d.assigned_to,
            "quantity":    d.quantity,
        },
        "status":     r.status.value,
        "status_key": r.status.name,
        "days_left":  r.days_left,
        "risk_date":  r.risk_date.isoformat() if r.risk_date else None,
        "notes":      r.notes,
        "is_at_risk": r.is_at_risk,
        "eol": {
            "model":            e.model           if e else "",
            "end_of_sale":      e.end_of_sale.isoformat()     if e and e.end_of_sale     else None,
            "end_of_support":   e.end_of_support.isoformat()  if e and e.end_of_support  else None,
            "end_of_sw_maint":  e.end_of_sw_maint.isoformat() if e and e.end_of_sw_maint else None,
            "replacement_sku":  e.replacement_sku  if e else "",
            "replacement_name": e.replacement_name if e else "",
            "migration_url":    e.migration_url    if e else "",
            "source_url":       e.source_url       if e else "",
            "confidence":       e.confidence       if e else "none",
        } if e else None,
    }


def dict_to_result(d: dict):
    """Reconstruct an AnalysisResult from a serialized dict (for Excel generation after restart)."""
    from core.models import Device, EOLRecord, AnalysisResult, EOLStatus
    dev_d = d["device"]
    device = Device(
        sys_id=dev_d["sys_id"], name=dev_d["name"], part_code=dev_d["part_code"],
        vendor=dev_d["vendor"], model=dev_d["model"], serial=dev_d.get("serial", ""),
        ip_address=dev_d.get("ip_address", ""), location=dev_d.get("location", ""),
        assigned_to=dev_d.get("assigned_to", ""), quantity=dev_d.get("quantity", 1),
    )
    eol_d = d.get("eol")
    eol = None
    if eol_d:
        def _p(s): return date.fromisoformat(s) if s else None
        eol = EOLRecord(
            part_code=dev_d["part_code"], vendor=dev_d["vendor"],
            model=eol_d.get("model", dev_d["part_code"]),
            end_of_sale=_p(eol_d.get("end_of_sale")),
            end_of_support=_p(eol_d.get("end_of_support")),
            end_of_sw_maint=_p(eol_d.get("end_of_sw_maint")),
            replacement_sku=eol_d.get("replacement_sku", ""),
            replacement_name=eol_d.get("replacement_name", ""),
            migration_url=eol_d.get("migration_url", ""),
            source_url=eol_d.get("source_url", ""),
            confidence=eol_d.get("confidence", "none"),
        )
    status_map = {s.name: s for s in EOLStatus}
    status = status_map.get(d.get("status_key", ""), EOLStatus.UNKNOWN)
    risk_date = date.fromisoformat(d["risk_date"]) if d.get("risk_date") else None
    return AnalysisResult(
        device=device, eol=eol, status=status,
        days_left=d.get("days_left"), risk_date=risk_date,
        notes=d.get("notes", ""),
    )
