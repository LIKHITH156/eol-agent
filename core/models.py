"""
EOL Agent — Data Models
Defines Device, EOLRecord, and AnalysisResult used across the system.
"""

from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Optional


class EOLStatus(Enum):
    EXPIRED     = "EOL/EOS — Expired"
    CRITICAL    = "Critical — < 6 months"
    WARNING     = "Warning — 6–12 months"
    MONITOR     = "Monitor — 12–24 months"
    SAFE        = "Safe — 2+ years"
    UNKNOWN     = "EOS/EOL Not Announced"


# Thresholds in days
THRESHOLDS = {
    EOLStatus.CRITICAL: 180,
    EOLStatus.WARNING:  365,
    EOLStatus.MONITOR:  730,
}


@dataclass
class Device:
    """Represents one CI record from ServiceNow CMDB."""
    sys_id:       str
    name:         str
    part_code:    str          # e.g. WS-C2960X-24TS-L
    vendor:       str
    model:        str
    serial:       str = ""
    ip_address:   str = ""
    location:     str = ""
    assigned_to:  str = ""
    quantity:     int = 1


@dataclass
class EOLRecord:
    """EOL/EOS lifecycle dates for a device model."""
    part_code:          str
    vendor:             str
    model:              str
    end_of_sale:        Optional[date] = None   # EOS — no longer sold
    end_of_support:     Optional[date] = None   # EOL — no SW/HW support
    end_of_sw_maint:    Optional[date] = None   # End of SW maintenance releases
    replacement_sku:    str = ""
    replacement_name:   str = ""
    migration_url:      str = ""
    source_url:         str = ""
    confidence:         str = "high"            # high / medium / low


@dataclass
class AnalysisResult:
    """Combined result of a device + its EOL lookup."""
    device:      Device
    eol:         Optional[EOLRecord]
    status:      EOLStatus
    days_left:   Optional[int]          # days until the soonest critical date
    risk_date:   Optional[date]         # the soonest critical date
    notes:       str = ""

    @property
    def is_at_risk(self) -> bool:
        return self.status in (EOLStatus.EXPIRED, EOLStatus.CRITICAL,
                               EOLStatus.WARNING, EOLStatus.MONITOR)

    @property
    def is_safe(self) -> bool:
        return self.status in (EOLStatus.SAFE, EOLStatus.UNKNOWN)
