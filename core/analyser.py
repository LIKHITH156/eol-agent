"""
EOL Agent — Analysis Engine
Scores each device against its EOL dates and produces AnalysisResult objects.
"""

from datetime import date
from typing import Optional
from core.models import (
    Device, EOLRecord, AnalysisResult,
    EOLStatus, THRESHOLDS
)
from core.researcher import EOLResearcher


class EOLAnalyser:
    """
    Takes a list of Device objects, looks up their EOL dates,
    and returns categorised AnalysisResult objects.
    """

    def __init__(self, researcher: Optional[EOLResearcher] = None):
        self.researcher = researcher or EOLResearcher()

    def analyse_all(self, devices: list[Device]) -> list[AnalysisResult]:
        results = []
        total = len(devices)
        for i, device in enumerate(devices, 1):
            print(f"[{i}/{total}] Analysing {device.part_code} ({device.name})")
            result = self.analyse_one(device)
            results.append(result)
        print(f"\n[Analyser] Done - {total} devices processed.")
        return results

    def analyse_one(self, device: Device) -> AnalysisResult:
        eol_record = self.researcher.lookup(device.part_code, device.vendor)
        status, days_left, risk_date = self._score(eol_record)
        notes = self._build_notes(device, eol_record, status)
        return AnalysisResult(
            device    = device,
            eol       = eol_record,
            status    = status,
            days_left = days_left,
            risk_date = risk_date,
            notes     = notes,
        )

    # ---------------------------------------------------------------- #

    def _score(self, eol: Optional[EOLRecord]) -> tuple[EOLStatus, Optional[int], Optional[date]]:
        if not eol:
            return EOLStatus.UNKNOWN, None, None

        today = date.today()

        # Collect relevant dates (prefer EOS as the action trigger)
        candidates = []
        if eol.end_of_sale:
            candidates.append(eol.end_of_sale)
        if eol.end_of_support:
            candidates.append(eol.end_of_support)
        if eol.end_of_sw_maint:
            candidates.append(eol.end_of_sw_maint)

        if not candidates:
            return EOLStatus.UNKNOWN, None, None

        # Use end_of_support as primary risk date; fall back to EOS
        risk_date = eol.end_of_support or eol.end_of_sale
        days_left = (risk_date - today).days

        if days_left < 0:
            return EOLStatus.EXPIRED, days_left, risk_date
        elif days_left <= THRESHOLDS[EOLStatus.CRITICAL]:
            return EOLStatus.CRITICAL, days_left, risk_date
        elif days_left <= THRESHOLDS[EOLStatus.WARNING]:
            return EOLStatus.WARNING, days_left, risk_date
        elif days_left <= THRESHOLDS[EOLStatus.MONITOR]:
            return EOLStatus.MONITOR, days_left, risk_date
        else:
            return EOLStatus.SAFE, days_left, risk_date

    def _build_notes(self, device: Device, eol: Optional[EOLRecord], status: EOLStatus) -> str:
        if not eol:
            return "EOL data not found — manual verification recommended."

        # Confidence-based messages
        if eol.confidence == "low":
            return ("EOL/EOS dates not yet published by vendor. "
                    "Device is in active support but official lifecycle dates are unavailable. "
                    "Check vendor portal for updates.")
        if eol.confidence == "none":
            return ("EOL/EOS data not found in database or official vendor portals. "
                    "This may be a non-standard, virtual, or regional model. "
                    "Manual verification recommended.")

        if not eol.end_of_support and not eol.end_of_sale:
            return "EOL/EOS dates not published by vendor — manual verification recommended."

        notes = []
        if status == EOLStatus.EXPIRED:
            notes.append("⚠ Device has passed End-of-Support. No patches or TAC support available.")
        elif status == EOLStatus.CRITICAL:
            notes.append("⚠ End-of-Support in under 6 months. Replacement procurement should start now.")
        elif status == EOLStatus.WARNING:
            notes.append("Plan replacement within 6–12 months. Begin vendor evaluation.")
        elif status == EOLStatus.MONITOR:
            notes.append("Monitor — include in next refresh cycle.")
        if eol.replacement_sku and eol.replacement_sku not in (eol.part_code, ""):
            notes.append(f"Recommended replacement: {eol.replacement_sku}")
        return " | ".join(notes)

    # ---------------------------------------------------------------- #
    #  Summary helpers                                                   #
    # ---------------------------------------------------------------- #

    @staticmethod
    def split_results(results: list[AnalysisResult]) -> tuple[list[AnalysisResult], list[AnalysisResult]]:
        """Return (at_risk_list, safe_list)."""
        at_risk = [r for r in results if r.is_at_risk]
        safe    = [r for r in results if r.is_safe]
        # Sort at_risk by days_left ascending (most urgent first)
        at_risk.sort(key=lambda r: (r.days_left is None, r.days_left or 0))
        return at_risk, safe

    @staticmethod
    def summary_stats(results: list[AnalysisResult]) -> dict:
        total    = len(results)
        expired  = sum(1 for r in results if r.status == EOLStatus.EXPIRED)
        critical = sum(1 for r in results if r.status == EOLStatus.CRITICAL)
        warning  = sum(1 for r in results if r.status == EOLStatus.WARNING)
        monitor  = sum(1 for r in results if r.status == EOLStatus.MONITOR)
        safe     = sum(1 for r in results if r.status == EOLStatus.SAFE)
        unknown  = sum(1 for r in results if r.status == EOLStatus.UNKNOWN)
        return {
            "total": total, "expired": expired, "critical": critical,
            "warning": warning, "monitor": monitor, "safe": safe, "unknown": unknown,
        }
