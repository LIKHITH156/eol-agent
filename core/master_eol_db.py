"""
EOL Agent — Master Asset EOL Database
Source: master_assest_data.xlsx — 478 real device models
This database takes PRIORITY over the generic LOCAL_EOL_DB.
Statuses: Data found | Date not published | Non Cisco | Data not found
"""

from datetime import date
from core.models import EOLRecord

MASTER_EOL_DB: dict[str, EOLRecord] = {

    # Data found
    "Z3C-HW-WW": EOLRecord(
        part_code="Z3C-HW-WW", vendor="Cisco", model="Z3C-HW-WW",
        end_of_sale=date(2024, 2, 11), end_of_support=date(2029, 11, 2), end_of_sw_maint=None,
        replacement_sku="Z4C-HW",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MX64-HW": EOLRecord(
        part_code="MX64-HW", vendor="Cisco", model="MX64-HW",
        end_of_sale=date(2022, 7, 26), end_of_support=date(2027, 7, 26), end_of_sw_maint=None,
        replacement_sku="MX67-HW",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "MX67C-HW-WW": EOLRecord(
        part_code="MX67C-HW-WW", vendor="Cisco", model="MX67C-HW-WW",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MX84-HW": EOLRecord(
        part_code="MX84-HW", vendor="Cisco", model="MX84-HW",
        end_of_sale=date(2021, 10, 31), end_of_support=date(2026, 10, 31), end_of_sw_maint=None,
        replacement_sku="MX85-HW",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MR46-HW": EOLRecord(
        part_code="MR46-HW", vendor="Cisco", model="MR46-HW",
        end_of_sale=date(2022, 7, 14), end_of_support=date(2026, 7, 21), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "871": EOLRecord(
        part_code="871", vendor="Cisco", model="871",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASA5525-K9": EOLRecord(
        part_code="ASA5525-K9", vendor="Cisco", model="ASA5525-K9",
        end_of_sale=date(2020, 9, 4), end_of_support=date(2025, 9, 30), end_of_sw_maint=date(2021, 4, 9),
        replacement_sku="Cisco Firepower 2100 Series",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASA5545-MB": EOLRecord(
        part_code="ASA5545-MB", vendor="Cisco", model="ASA5545-MB",
        end_of_sale=date(2020, 9, 4), end_of_support=date(2025, 9, 30), end_of_sw_maint=date(2021, 4, 9),
        replacement_sku="Cisco Firepower 2100 Series",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "MX67-HW": EOLRecord(
        part_code="MX67-HW", vendor="Cisco", model="MX67-HW",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "MX67": EOLRecord(
        part_code="MX67", vendor="Cisco", model="MX67",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "MX 67": EOLRecord(
        part_code="MX 67", vendor="Cisco", model="MX 67",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "MX450-HW": EOLRecord(
        part_code="MX450-HW", vendor="Cisco", model="MX450-HW",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MX100-HW": EOLRecord(
        part_code="MX100-HW", vendor="Cisco", model="MX100-HW",
        end_of_sale=date(2022, 2, 1), end_of_support=date(2027, 2, 1), end_of_sw_maint=None,
        replacement_sku="MX95-HW",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MX100": EOLRecord(
        part_code="MX100", vendor="Cisco", model="MX100",
        end_of_sale=date(2022, 2, 1), end_of_support=date(2027, 2, 1), end_of_sw_maint=None,
        replacement_sku="MX95",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASA5506-K9": EOLRecord(
        part_code="ASA5506-K9", vendor="Cisco", model="ASA5506-K9",
        end_of_sale=date(2021, 8, 2), end_of_support=date(2026, 8, 31), end_of_sw_maint=date(2022, 2, 8),
        replacement_sku="Cisco Firepower 1000",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "PIX-525": EOLRecord(
        part_code="PIX-525", vendor="Cisco", model="PIX-525",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "VIC-2FXO": EOLRecord(
        part_code="VIC-2FXO", vendor="Cisco", model="VIC-2FXO",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="NIM-2FXO",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "CISCO PIX-525": EOLRecord(
        part_code="CISCO PIX-525", vendor="Cisco", model="CISCO PIX-525",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data not found
    "FAZ300D": EOLRecord(
        part_code="FAZ300D", vendor="Fortinet", model="FAZ300D",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="none",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASA5508-FTD-K9": EOLRecord(
        part_code="ASA5508-FTD-K9", vendor="Cisco", model="ASA5508-FTD-K9",
        end_of_sale=date(2021, 8, 2), end_of_support=date(2026, 8, 31), end_of_sw_maint=date(2022, 2, 8),
        replacement_sku="Cisco Firepower 1000 Serie",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "FPR-1010": EOLRecord(
        part_code="FPR-1010", vendor="Cisco", model="FPR-1010",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASA5506-SEC-BUN-K9": EOLRecord(
        part_code="ASA5506-SEC-BUN-K9", vendor="Cisco", model="ASA5506-SEC-BUN-K9",
        end_of_sale=date(2021, 8, 2), end_of_support=date(2026, 8, 31), end_of_sw_maint=date(2022, 2, 8),
        replacement_sku="Cisco Firepower 1000",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASA5506-K8": EOLRecord(
        part_code="ASA5506-K8", vendor="Cisco", model="ASA5506-K8",
        end_of_sale=date(2021, 8, 2), end_of_support=date(2026, 8, 31), end_of_sw_maint=date(2022, 2, 8),
        replacement_sku="Cisco Firepower 1000",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "FPR1010-NGFW-K9": EOLRecord(
        part_code="FPR1010-NGFW-K9", vendor="Cisco", model="FPR1010-NGFW-K9",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO FIREPOWER 4115 THREAT": EOLRecord(
        part_code="Cisco Firepower 4115 Threat", vendor="Cisco", model="Cisco Firepower 4115 Threat",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASA5508-K9": EOLRecord(
        part_code="ASA5508-K9", vendor="Cisco", model="ASA5508-K9",
        end_of_sale=date(2021, 8, 2), end_of_support=date(2026, 8, 31), end_of_sw_maint=date(2022, 2, 8),
        replacement_sku="Cisco Firepower 1000 Series Appliances",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "FPR1010": EOLRecord(
        part_code="FPR1010", vendor="Cisco", model="FPR1010",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "FPR4110-NGFW-K9": EOLRecord(
        part_code="FPR4110-NGFW-K9", vendor="Cisco", model="FPR4110-NGFW-K9",
        end_of_sale=date(2022, 1, 31), end_of_support=date(2027, 1, 31), end_of_sw_maint=None,
        replacement_sku="Cisco Firepower 4112 Series",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Non Cisco
    "FPR1010-ASA-K9": EOLRecord(
        part_code="FPR1010-ASA-K9", vendor="Unknown", model="FPR1010-ASA-K9",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="none",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASA5506-SEC-BUN-K8": EOLRecord(
        part_code="ASA5506-SEC-BUN-K8", vendor="Cisco", model="ASA5506-SEC-BUN-K8",
        end_of_sale=date(2021, 8, 2), end_of_support=date(2026, 8, 31), end_of_sw_maint=date(2022, 2, 8),
        replacement_sku="Cisco Firepower 1000",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASA5585-S20-K9": EOLRecord(
        part_code="ASA5585-S20-K9", vendor="Cisco", model="ASA5585-S20-K9",
        end_of_sale=date(2018, 6, 1), end_of_support=date(2023, 5, 31), end_of_sw_maint=None,
        replacement_sku="Cisco Firepower 4100",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASA5555-K9": EOLRecord(
        part_code="ASA5555-K9", vendor="Cisco", model="ASA5555-K9",
        end_of_sale=date(2020, 9, 4), end_of_support=date(2025, 9, 30), end_of_sw_maint=date(2021, 4, 9),
        replacement_sku="Cisco Firepower 2100 Series",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASA5545-K9": EOLRecord(
        part_code="ASA5545-K9", vendor="Cisco", model="ASA5545-K9",
        end_of_sale=date(2020, 9, 4), end_of_support=date(2025, 9, 30), end_of_sw_maint=date(2021, 4, 9),
        replacement_sku="Cisco Firepower 2100 Series Appliances",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASA5545-2SSD120-K9": EOLRecord(
        part_code="ASA5545-2SSD120-K9", vendor="Cisco", model="ASA5545-2SSD120-K9",
        end_of_sale=date(2022, 9, 2), end_of_support=date(2025, 9, 30), end_of_sw_maint=date(2023, 2, 9),
        replacement_sku="Cisco Firepower 2100 Series",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASA5505-50-BUN-K9": EOLRecord(
        part_code="ASA5505-50-BUN-K9", vendor="Cisco", model="ASA5505-50-BUN-K9",
        end_of_sale=date(2017, 8, 25), end_of_support=date(2022, 8, 31), end_of_sw_maint=None,
        replacement_sku="ASA5506-X",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "FPR-1010E": EOLRecord(
        part_code="FPR-1010E", vendor="Cisco", model="FPR-1010E",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASA5506-SSD": EOLRecord(
        part_code="ASA5506-SSD", vendor="Cisco", model="ASA5506-SSD",
        end_of_sale=date(2021, 8, 2), end_of_support=date(2026, 8, 31), end_of_sw_maint=date(2022, 2, 8),
        replacement_sku="Cisco Firepower 1000",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASA5505-K8": EOLRecord(
        part_code="ASA5505-K8", vendor="Cisco", model="ASA5505-K8",
        end_of_sale=date(2017, 8, 25), end_of_support=date(2022, 8, 31), end_of_sw_maint=None,
        replacement_sku="ASA5506-X",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4331-VSEC/K9": EOLRecord(
        part_code="ISR4331-VSEC/K9", vendor="Cisco", model="ISR4331-VSEC/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO ISR4431/K9": EOLRecord(
        part_code="Cisco ISR4431/K9", vendor="Cisco", model="Cisco ISR4431/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8300-1N1S-4T2X",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4351-V/K9": EOLRecord(
        part_code="ISR4351-V/K9", vendor="Cisco", model="ISR4351-V/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8300-2N2S-6T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4451-X/K9": EOLRecord(
        part_code="ISR4451-X/K9", vendor="Cisco", model="ISR4451-X/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8300-2N2S-4T2X",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C8300-1N1S-4T2X": EOLRecord(
        part_code="C8300-1N1S-4T2X", vendor="Cisco", model="C8300-1N1S-4T2X",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8300-1N1S-4T2X",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1921/K9": EOLRecord(
        part_code="CISCO1921/K9", vendor="Cisco", model="CISCO1921/K9",
        end_of_sale=date(2018, 9, 29), end_of_support=date(2023, 9, 30), end_of_sw_maint=date(2019, 9, 29),
        replacement_sku="ISR4221/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1921-SEC/K9": EOLRecord(
        part_code="CISCO1921-SEC/K9", vendor="Cisco", model="CISCO1921-SEC/K9",
        end_of_sale=date(2018, 9, 29), end_of_support=date(2023, 9, 30), end_of_sw_maint=date(2019, 9, 29),
        replacement_sku="ISR4221-SEC/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4321-SEC/K9": EOLRecord(
        part_code="ISR4321-SEC/K9", vendor="Cisco", model="ISR4321-SEC/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C921-4P": EOLRecord(
        part_code="C921-4P", vendor="Cisco", model="C921-4P",
        end_of_sale=date(2022, 4, 30), end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4331-SEC/K9": EOLRecord(
        part_code="ISR4331-SEC/K9", vendor="Cisco", model="ISR4331-SEC/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4331/K9": EOLRecord(
        part_code="ISR4331/K9", vendor="Cisco", model="ISR4331/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C881-K9": EOLRecord(
        part_code="C881-K9", vendor="Cisco", model="C881-K9",
        end_of_sale=date(2020, 10, 29), end_of_support=date(2025, 10, 31), end_of_sw_maint=date(2021, 10, 29),
        replacement_sku="C921-4P",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO 871 (MPC8272)": EOLRecord(
        part_code="Cisco 871 (MPC8272)", vendor="Cisco", model="Cisco 871 (MPC8272)",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO 871-SEC-K9": EOLRecord(
        part_code="Cisco 871-SEC-K9", vendor="Cisco", model="Cisco 871-SEC-K9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO871": EOLRecord(
        part_code="CISCO871", vendor="Cisco", model="CISCO871",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO3925-SEC/K9": EOLRecord(
        part_code="CISCO3925-SEC/K9", vendor="Cisco", model="CISCO3925-SEC/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4431-SEC/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C1111-8P": EOLRecord(
        part_code="C1111-8P", vendor="Cisco", model="C1111-8P",
        end_of_sale=date(2023, 5, 9), end_of_support=date(2028, 5, 31), end_of_sw_maint=date(2024, 8, 5),
        replacement_sku="ISR 1100 8P",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO888-SEC-K9": EOLRecord(
        part_code="CISCO888-SEC-K9", vendor="Cisco", model="CISCO888-SEC-K9",
        end_of_sale=date(2015, 10, 1), end_of_support=date(2020, 9, 30), end_of_sw_maint=date(2016, 9, 30),
        replacement_sku="C888-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "3825": EOLRecord(
        part_code="3825", vendor="Cisco", model="3825",
        end_of_sale=date(2015, 8, 6), end_of_support=date(2020, 8, 31), end_of_sw_maint=date(2016, 5, 8),
        replacement_sku="no replacement available",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "3620": EOLRecord(
        part_code="3620", vendor="Cisco", model="3620",
        end_of_sale=date(2003, 12, 31), end_of_support=date(2008, 12, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO 877 (MPC8272)": EOLRecord(
        part_code="Cisco 877 (MPC8272)", vendor="Cisco", model="Cisco 877 (MPC8272)",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "877": EOLRecord(
        part_code="877", vendor="Cisco", model="877",
        end_of_sale=date(2012, 6, 15), end_of_support=date(2017, 6, 30), end_of_sw_maint=date(2013, 6, 15),
        replacement_sku="887VA",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO801": EOLRecord(
        part_code="CISCO801", vendor="Cisco", model="CISCO801",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO877-K9": EOLRecord(
        part_code="CISCO877-K9", vendor="Cisco", model="CISCO877-K9",
        end_of_sale=date(2011, 12, 20), end_of_support=date(2016, 12, 31), end_of_sw_maint=date(2012, 12, 19),
        replacement_sku="CISCO887VA-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO877W-G-E-K9": EOLRecord(
        part_code="CISCO877W-G-E-K9", vendor="Cisco", model="CISCO877W-G-E-K9",
        end_of_sale=date(2011, 12, 20), end_of_support=date(2016, 12, 31), end_of_sw_maint=date(2012, 12, 19),
        replacement_sku="C887VA-W-E-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO 877": EOLRecord(
        part_code="Cisco 877", vendor="Cisco", model="Cisco 877",
        end_of_sale=date(2012, 6, 15), end_of_support=date(2017, 6, 30), end_of_sw_maint=date(2013, 6, 15),
        replacement_sku="CISCO887VA",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C887VA-K9": EOLRecord(
        part_code="C887VA-K9", vendor="Cisco", model="C887VA-K9",
        end_of_sale=date(2020, 10, 29), end_of_support=date(2025, 10, 31), end_of_sw_maint=date(2021, 10, 29),
        replacement_sku="C1117-4P",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO887VA-K9": EOLRecord(
        part_code="CISCO887VA-K9", vendor="Cisco", model="CISCO887VA-K9",
        end_of_sale=date(2014, 8, 22), end_of_support=date(2019, 8, 31), end_of_sw_maint=date(2015, 8, 22),
        replacement_sku="C887VA-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C2901-CME-SRST/K9": EOLRecord(
        part_code="C2901-CME-SRST/K9", vendor="Cisco", model="C2901-CME-SRST/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4321-V/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1841-2SHDSL": EOLRecord(
        part_code="CISCO1841-2SHDSL", vendor="Cisco", model="CISCO1841-2SHDSL",
        end_of_sale=date(2014, 7, 5), end_of_support=date(2023, 10, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO3945E-SEC/K9": EOLRecord(
        part_code="CISCO3945E-SEC/K9", vendor="Cisco", model="CISCO3945E-SEC/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4431-SEC/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4431-AX/K9": EOLRecord(
        part_code="ISR4431-AX/K9", vendor="Cisco", model="ISR4431-AX/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8300-1N1S-4T2X",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASR1001-X=": EOLRecord(
        part_code="ASR1001-X=", vendor="Cisco", model="ASR1001-X=",
        end_of_sale=date(2022, 8, 1), end_of_support=date(2027, 7, 31), end_of_sw_maint=date(2023, 1, 8),
        replacement_sku="C8500L-8S4X",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4431-SEC/K9": EOLRecord(
        part_code="ISR4431-SEC/K9", vendor="Cisco", model="ISR4431-SEC/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8300-1N1S-4T2X",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C888EA-K9": EOLRecord(
        part_code="C888EA-K9", vendor="Cisco", model="C888EA-K9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "837": EOLRecord(
        part_code="837", vendor="Cisco", model="837",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C887VA-K9 + SL-880-AIS": EOLRecord(
        part_code="C887VA-K9 + SL-880-AIS", vendor="Cisco", model="C887VA-K9 + SL-880-AIS",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "VG224": EOLRecord(
        part_code="VG224", vendor="Cisco", model="VG224",
        end_of_sale=date(2015, 4, 24), end_of_support=date(2020, 4, 30), end_of_sw_maint=date(2016, 4, 23),
        replacement_sku="VG310",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO837-K9": EOLRecord(
        part_code="CISCO837-K9", vendor="Cisco", model="CISCO837-K9",
        end_of_sale=date(2007, 6, 30), end_of_support=date(2012, 6, 28), end_of_sw_maint=date(2008, 6, 30),
        replacement_sku="CISCO877-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C887VA-V-K9": EOLRecord(
        part_code="C887VA-V-K9", vendor="Cisco", model="C887VA-V-K9",
        end_of_sale=date(2016, 3, 31), end_of_support=date(2021, 3, 31), end_of_sw_maint=date(2017, 3, 31),
        replacement_sku="C881-V-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO837-K9-64": EOLRecord(
        part_code="CISCO837-K9-64", vendor="Cisco", model="CISCO837-K9-64",
        end_of_sale=date(2007, 6, 30), end_of_support=date(2012, 6, 28), end_of_sw_maint=date(2008, 6, 30),
        replacement_sku="CISCO877-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO837-SEC-K9": EOLRecord(
        part_code="CISCO837-SEC-K9", vendor="Cisco", model="CISCO837-SEC-K9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MCS 7800": EOLRecord(
        part_code="MCS 7800", vendor="Cisco", model="MCS 7800",
        end_of_sale=date(2012, 10, 13), end_of_support=date(2017, 10, 31), end_of_sw_maint=None,
        replacement_sku="Cisco UCS",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "DL360G5": EOLRecord(
        part_code="DL360G5", vendor="Cisco", model="DL360G5",
        end_of_sale=None, end_of_support=date(2014, 11, 30), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "DL380G5": EOLRecord(
        part_code="DL380G5", vendor="Cisco", model="DL380G5",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO3845": EOLRecord(
        part_code="CISCO3845", vendor="Cisco", model="CISCO3845",
        end_of_sale=date(2015, 8, 6), end_of_support=date(2020, 8, 31), end_of_sw_maint=date(2016, 5, 8),
        replacement_sku="no replacement available",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C881G-4G-GA-K9": EOLRecord(
        part_code="C881G-4G-GA-K9", vendor="Cisco", model="C881G-4G-GA-K9",
        end_of_sale=date(2019, 7, 29), end_of_support=date(2024, 7, 31), end_of_sw_maint=date(2020, 7, 29),
        replacement_sku="C1111-4PLTEEA",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "3845": EOLRecord(
        part_code="3845", vendor="Cisco", model="3845",
        end_of_sale=date(2011, 11, 1), end_of_support=date(2016, 11, 1), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "C1-CISCO4331/K9": EOLRecord(
        part_code="C1-CISCO4331/K9", vendor="Cisco", model="C1-CISCO4331/K9",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C881G+7-K9": EOLRecord(
        part_code="C881G+7-K9", vendor="Cisco", model="C881G+7-K9",
        end_of_sale=date(2020, 4, 29), end_of_support=date(2025, 4, 30), end_of_sw_maint=date(2021, 4, 29),
        replacement_sku="C1111",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C819G-4G-G-K9": EOLRecord(
        part_code="C819G-4G-G-K9", vendor="Cisco", model="C819G-4G-G-K9",
        end_of_sale=date(2015, 12, 9), end_of_support=date(2020, 12, 31), end_of_sw_maint=date(2016, 8, 12),
        replacement_sku="C819G-4G-GA-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C881-V-K9": EOLRecord(
        part_code="C881-V-K9", vendor="Cisco", model="C881-V-K9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C1111-4PLTEEA": EOLRecord(
        part_code="C1111-4PLTEEA", vendor="Cisco", model="C1111-4PLTEEA",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2020, 1, 27), end_of_sw_maint=None,
        replacement_sku="no replacement available",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C896VAG-LTE-GA-K9": EOLRecord(
        part_code="C896VAG-LTE-GA-K9", vendor="Cisco", model="C896VAG-LTE-GA-K9",
        end_of_sale=date(2019, 7, 29), end_of_support=date(2024, 7, 31), end_of_sw_maint=date(2020, 7, 29),
        replacement_sku="C896VAG-LTE-GA-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO876-K9": EOLRecord(
        part_code="CISCO876-K9", vendor="Cisco", model="CISCO876-K9",
        end_of_sale=date(2011, 12, 20), end_of_support=date(2016, 12, 31), end_of_sw_maint=date(2013, 12, 19),
        replacement_sku="CISCO886VA-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C887VA-V-K9-RF": EOLRecord(
        part_code="C887VA-V-K9-RF", vendor="Cisco", model="C887VA-V-K9-RF",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="C881-V-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C1111-4P": EOLRecord(
        part_code="C1111-4P", vendor="Cisco", model="C1111-4P",
        end_of_sale=date(2023, 5, 9), end_of_support=date(2028, 5, 31), end_of_sw_maint=date(2024, 8, 5),
        replacement_sku="C1131-8PWA",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "827H": EOLRecord(
        part_code="827H", vendor="Cisco", model="827H",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C1121-4P": EOLRecord(
        part_code="C1121-4P", vendor="Cisco", model="C1121-4P",
        end_of_sale=date(2025, 10, 31), end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO887VA-SEC-K9": EOLRecord(
        part_code="CISCO887VA-SEC-K9", vendor="Cisco", model="CISCO887VA-SEC-K9",
        end_of_sale=date(2014, 7, 3), end_of_support=date(2019, 7, 31), end_of_sw_maint=date(2015, 3, 7),
        replacement_sku="C887VA-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C881G+7-K9-WS": EOLRecord(
        part_code="C881G+7-K9-WS", vendor="Cisco", model="C881G+7-K9-WS",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO3825": EOLRecord(
        part_code="CISCO3825", vendor="Cisco", model="CISCO3825",
        end_of_sale=date(2011, 11, 1), end_of_support=date(2016, 10, 31), end_of_sw_maint=date(2014, 10, 31),
        replacement_sku="CISCO3925/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO 887VAG2": EOLRecord(
        part_code="Cisco 887VAG2", vendor="Cisco", model="Cisco 887VAG2",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO836-SI-K9-64": EOLRecord(
        part_code="CISCO836-SI-K9-64", vendor="Cisco", model="CISCO836-SI-K9-64",
        end_of_sale=date(2007, 6, 30), end_of_support=date(2012, 6, 28), end_of_sw_maint=date(2008, 6, 30),
        replacement_sku="CISCO876-SEC-I-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO886VA-K9": EOLRecord(
        part_code="CISCO886VA-K9", vendor="Cisco", model="CISCO886VA-K9",
        end_of_sale=date(2014, 8, 22), end_of_support=date(2019, 8, 31), end_of_sw_maint=date(2015, 8, 22),
        replacement_sku="C886VA-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO876-SEC-K9": EOLRecord(
        part_code="CISCO876-SEC-K9", vendor="Cisco", model="CISCO876-SEC-K9",
        end_of_sale=date(2011, 12, 20), end_of_support=date(2016, 12, 31), end_of_sw_maint=date(2012, 12, 19),
        replacement_sku="CISCO886VA-SEC-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO836-K9": EOLRecord(
        part_code="CISCO836-K9", vendor="Cisco", model="CISCO836-K9",
        end_of_sale=date(2007, 6, 30), end_of_support=date(2012, 6, 28), end_of_sw_maint=date(2008, 6, 30),
        replacement_sku="CISCO876-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO886VA-SEC-K9": EOLRecord(
        part_code="CISCO886VA-SEC-K9", vendor="Cisco", model="CISCO886VA-SEC-K9",
        end_of_sale=date(2014, 7, 3), end_of_support=date(2019, 7, 31), end_of_sw_maint=date(2015, 3, 7),
        replacement_sku="C886VA-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1941/K9": EOLRecord(
        part_code="CISCO1941/K9", vendor="Cisco", model="CISCO1941/K9",
        end_of_sale=date(2018, 9, 29), end_of_support=date(2023, 9, 30), end_of_sw_maint=date(2019, 9, 29),
        replacement_sku="ISR4221/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2921-SEC/K9": EOLRecord(
        part_code="CISCO2921-SEC/K9", vendor="Cisco", model="CISCO2921-SEC/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4331-SEC/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO871-K9": EOLRecord(
        part_code="CISCO871-K9", vendor="Cisco", model="CISCO871-K9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO881-SEC-K9": EOLRecord(
        part_code="CISCO881-SEC-K9", vendor="Cisco", model="CISCO881-SEC-K9",
        end_of_sale=date(2014, 7, 3), end_of_support=date(2019, 7, 31), end_of_sw_maint=date(2015, 3, 7),
        replacement_sku="C881-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO881G-G-K9": EOLRecord(
        part_code="CISCO881G-G-K9", vendor="Cisco", model="CISCO881G-G-K9",
        end_of_sale=date(2012, 10, 10), end_of_support=date(2017, 10, 31), end_of_sw_maint=date(2013, 10, 10),
        replacement_sku="C881G+7-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO881G-K9": EOLRecord(
        part_code="CISCO881G-K9", vendor="Cisco", model="CISCO881G-K9",
        end_of_sale=date(2012, 10, 10), end_of_support=date(2017, 10, 31), end_of_sw_maint=None,
        replacement_sku="C881G+7-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO871-SEC-K9": EOLRecord(
        part_code="CISCO871-SEC-K9", vendor="Cisco", model="CISCO871-SEC-K9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="CISCO881-SEC-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO878-K9": EOLRecord(
        part_code="CISCO878-K9", vendor="Cisco", model="CISCO878-K9",
        end_of_sale=date(2011, 5, 10), end_of_support=date(2016, 5, 31), end_of_sw_maint=date(2012, 9, 5),
        replacement_sku="CISCO888-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C892FSP-K9": EOLRecord(
        part_code="C892FSP-K9", vendor="Cisco", model="C892FSP-K9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4331-V/K9": EOLRecord(
        part_code="ISR4331-V/K9", vendor="Cisco", model="ISR4331-V/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO3945/K9": EOLRecord(
        part_code="CISCO3945/K9", vendor="Cisco", model="CISCO3945/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4451-X/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C2921-VSEC-CUBE/K9": EOLRecord(
        part_code="C2921-VSEC-CUBE/K9", vendor="Cisco", model="C2921-VSEC-CUBE/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4331-VSEC/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4331-SEC/K9-WS": EOLRecord(
        part_code="ISR4331-SEC/K9-WS", vendor="Cisco", model="ISR4331-SEC/K9-WS",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "C1111X-8P": EOLRecord(
        part_code="C1111X-8P", vendor="Cisco", model="C1111X-8P",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C886VA-K9": EOLRecord(
        part_code="C886VA-K9", vendor="Cisco", model="C886VA-K9",
        end_of_sale=date(2020, 4, 29), end_of_support=date(2025, 4, 30), end_of_sw_maint=date(2021, 4, 29),
        replacement_sku="C1116-4P",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1941-SEC/K9": EOLRecord(
        part_code="CISCO1941-SEC/K9", vendor="Cisco", model="CISCO1941-SEC/K9",
        end_of_sale=date(2018, 9, 29), end_of_support=date(2023, 9, 30), end_of_sw_maint=date(2019, 9, 29),
        replacement_sku="ISR4221-SEC/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO3945-SEC/K9": EOLRecord(
        part_code="CISCO3945-SEC/K9", vendor="Cisco", model="CISCO3945-SEC/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4431-SEC/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2901-SEC/K9": EOLRecord(
        part_code="CISCO2901-SEC/K9", vendor="Cisco", model="CISCO2901-SEC/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4321-SEC/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2951-SEC/K9": EOLRecord(
        part_code="CISCO2951-SEC/K9", vendor="Cisco", model="CISCO2951-SEC/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4351-SEC/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "1710": EOLRecord(
        part_code="1710", vendor="Cisco", model="1710",
        end_of_sale=date(2007, 3, 27), end_of_support=date(2012, 3, 27), end_of_sw_maint=None,
        replacement_sku="no replacement available",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C801": EOLRecord(
        part_code="c801", vendor="Cisco", model="c801",
        end_of_sale=date(2007, 7, 16), end_of_support=date(2012, 7, 14), end_of_sw_maint=date(2008, 7, 15),
        replacement_sku="CISCO876-SEC-I-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "1721": EOLRecord(
        part_code="1721", vendor="Cisco", model="1721",
        end_of_sale=date(2007, 3, 27), end_of_support=date(2012, 3, 27), end_of_sw_maint=None,
        replacement_sku="no replacement available",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO887-K9": EOLRecord(
        part_code="CISCO887-K9", vendor="Cisco", model="CISCO887-K9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO887G-K9-RF": EOLRecord(
        part_code="CISCO887G-K9-RF", vendor="Cisco", model="CISCO887G-K9-RF",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4321/K9": EOLRecord(
        part_code="ISR4321/K9", vendor="Cisco", model="ISR4321/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C927-4P": EOLRecord(
        part_code="C927-4P", vendor="Cisco", model="C927-4P",
        end_of_sale=date(2022, 4, 30), end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "C1118-8P": EOLRecord(
        part_code="C1118-8P", vendor="Cisco", model="C1118-8P",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO851W-G-E-K9": EOLRecord(
        part_code="CISCO851W-G-E-K9", vendor="Cisco", model="CISCO851W-G-E-K9",
        end_of_sale=date(2010, 7, 15), end_of_support=date(2015, 7, 31), end_of_sw_maint=date(2013, 7, 15),
        replacement_sku="CISCO861W-GN-E-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C881W-E-K9": EOLRecord(
        part_code="C881W-E-K9", vendor="Cisco", model="C881W-E-K9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO857W-G-E-K9": EOLRecord(
        part_code="CISCO857W-G-E-K9", vendor="Cisco", model="CISCO857W-G-E-K9",
        end_of_sale=date(2011, 12, 20), end_of_support=date(2016, 12, 31), end_of_sw_maint=date(2013, 12, 19),
        replacement_sku="Cisco 880VA Series",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO 2801": EOLRecord(
        part_code="Cisco 2801", vendor="Cisco", model="Cisco 2801",
        end_of_sale=date(2011, 11, 1), end_of_support=date(2016, 10, 31), end_of_sw_maint=date(2014, 10, 31),
        replacement_sku="CISCO2901/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2801": EOLRecord(
        part_code="CISCO2801", vendor="Cisco", model="CISCO2801",
        end_of_sale=date(2011, 11, 1), end_of_support=date(2016, 10, 31), end_of_sw_maint=date(2014, 10, 31),
        replacement_sku="CISCO2901/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C897VA-K9": EOLRecord(
        part_code="C897VA-K9", vendor="Cisco", model="C897VA-K9",
        end_of_sale=date(2019, 7, 29), end_of_support=date(2024, 7, 31), end_of_sw_maint=date(2020, 7, 28),
        replacement_sku="C1113-8P",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2911/K9": EOLRecord(
        part_code="CISCO2911/K9", vendor="Cisco", model="CISCO2911/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4331/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2901/K9": EOLRecord(
        part_code="CISCO2901/K9", vendor="Cisco", model="CISCO2901/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="C1-CISCO4321/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4221/K9": EOLRecord(
        part_code="ISR4221/K9", vendor="Cisco", model="ISR4221/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200L-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C899G-LTE-GA-K9": EOLRecord(
        part_code="C899G-LTE-GA-K9", vendor="Cisco", model="C899G-LTE-GA-K9",
        end_of_sale=date(2019, 7, 29), end_of_support=date(2024, 7, 31), end_of_sw_maint=date(2020, 7, 29),
        replacement_sku="C1111-8PLTEEA",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C891F-K9": EOLRecord(
        part_code="C891F-K9", vendor="Cisco", model="C891F-K9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C1111-8PLTEEA": EOLRecord(
        part_code="C1111-8PLTEEA", vendor="Cisco", model="C1111-8PLTEEA",
        end_of_sale=date(2023, 5, 9), end_of_support=date(2028, 5, 31), end_of_sw_maint=date(2024, 8, 5),
        replacement_sku="C1131-8PLTEPWA",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C897VAG-LTE-GA-K9": EOLRecord(
        part_code="C897VAG-LTE-GA-K9", vendor="Cisco", model="C897VAG-LTE-GA-K9",
        end_of_sale=date(2019, 7, 29), end_of_support=date(2024, 7, 31), end_of_sw_maint=date(2020, 7, 29),
        replacement_sku="C1113-8PLTEEA",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C897VAGW-LTE-GAEK9": EOLRecord(
        part_code="C897VAGW-LTE-GAEK9", vendor="Cisco", model="C897VAGW-LTE-GAEK9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4221-SEC/K9": EOLRecord(
        part_code="ISR4221-SEC/K9", vendor="Cisco", model="ISR4221-SEC/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200L-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4351/K9": EOLRecord(
        part_code="ISR4351/K9", vendor="Cisco", model="ISR4351/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8300-2N2S-6T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO3925/K9": EOLRecord(
        part_code="CISCO3925/K9", vendor="Cisco", model="CISCO3925/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4431/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO3925E-SEC/K9": EOLRecord(
        part_code="CISCO3925E-SEC/K9", vendor="Cisco", model="CISCO3925E-SEC/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="CISCO3925E-SEC/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO3925E/K9": EOLRecord(
        part_code="CISCO3925E/K9", vendor="Cisco", model="CISCO3925E/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4431/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2911-SEC/K9": EOLRecord(
        part_code="CISCO2911-SEC/K9", vendor="Cisco", model="CISCO2911-SEC/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="SR4331-SEC/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1921-SECK9-WS": EOLRecord(
        part_code="CISCO1921-SECK9-WS", vendor="Cisco", model="CISCO1921-SECK9-WS",
        end_of_sale=date(2018, 9, 29), end_of_support=date(2023, 9, 30), end_of_sw_maint=date(2019, 9, 29),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4351-SEC/K9": EOLRecord(
        part_code="ISR4351-SEC/K9", vendor="Cisco", model="ISR4351-SEC/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8300-2N2S-6T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2951/K9": EOLRecord(
        part_code="CISCO2951/K9", vendor="Cisco", model="CISCO2951/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4351/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASR1001-2.5G-VPNK9": EOLRecord(
        part_code="ASR1001-2.5G-VPNK9", vendor="Cisco", model="ASR1001-2.5G-VPNK9",
        end_of_sale=date(2016, 4, 29), end_of_support=date(2021, 4, 30), end_of_sw_maint=None,
        replacement_sku="ASR1001X-2.5G-VPN",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASR1001-2_5G-VPNK9": EOLRecord(
        part_code="ASR1001-2_5G-VPNK9", vendor="Cisco", model="ASR1001-2_5G-VPNK9",
        end_of_sale=date(2013, 11, 29), end_of_support=date(2018, 11, 30), end_of_sw_maint=date(2014, 11, 29),
        replacement_sku="Cisco ASR 1002",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASR1001X-2.5G-VPN": EOLRecord(
        part_code="ASR1001X-2.5G-VPN", vendor="Cisco", model="ASR1001X-2.5G-VPN",
        end_of_sale=date(2022, 8, 1), end_of_support=date(2027, 7, 31), end_of_sw_maint=date(2023, 1, 8),
        replacement_sku="C8500L-8S4X",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2811": EOLRecord(
        part_code="CISCO2811", vendor="Cisco", model="CISCO2811",
        end_of_sale=date(2011, 11, 1), end_of_support=date(2016, 11, 1), end_of_sw_maint=None,
        replacement_sku="CISCO2911",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO7301": EOLRecord(
        part_code="CISCO7301", vendor="Cisco", model="CISCO7301",
        end_of_sale=date(2012, 9, 29), end_of_support=date(2017, 9, 30), end_of_sw_maint=date(2015, 9, 29),
        replacement_sku="ASR 1000",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO ISR4451-X/K9": EOLRecord(
        part_code="cisco ISR4451-X/K9", vendor="Cisco", model="cisco ISR4451-X/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8300-2N2S-4T2X",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO CISCO1941/K9": EOLRecord(
        part_code="Cisco CISCO1941/K9", vendor="Cisco", model="Cisco CISCO1941/K9",
        end_of_sale=date(2018, 9, 29), end_of_support=date(2023, 9, 30), end_of_sw_maint=date(2019, 9, 29),
        replacement_sku="ISR4221/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO ISR4321/K9": EOLRecord(
        part_code="Cisco ISR4321/K9", vendor="Cisco", model="Cisco ISR4321/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO C887VA-K9": EOLRecord(
        part_code="Cisco C887VA-K9", vendor="Cisco", model="Cisco C887VA-K9",
        end_of_sale=date(2020, 10, 29), end_of_support=date(2025, 10, 31), end_of_sw_maint=date(2021, 10, 29),
        replacement_sku="C1117-4P",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C931-4P": EOLRecord(
        part_code="C931-4P", vendor="Cisco", model="C931-4P",
        end_of_sale=date(2022, 4, 30), end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO CISCO3945-CHASSIS": EOLRecord(
        part_code="Cisco CISCO3945-CHASSIS", vendor="Cisco", model="Cisco CISCO3945-CHASSIS",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4451-X/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO CISCO2951/K9": EOLRecord(
        part_code="Cisco CISCO2951/K9", vendor="Cisco", model="Cisco CISCO2951/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4351/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO 1801 (MPC8500)": EOLRecord(
        part_code="Cisco 1801 (MPC8500)", vendor="Cisco", model="Cisco 1801 (MPC8500)",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1812/K9": EOLRecord(
        part_code="CISCO1812/K9", vendor="Cisco", model="CISCO1812/K9",
        end_of_sale=date(2014, 5, 7), end_of_support=date(2023, 10, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO CISCO2911/K9": EOLRecord(
        part_code="Cisco CISCO2911/K9", vendor="Cisco", model="Cisco CISCO2911/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="C1-CISCO4331/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO C886VAJ-K9": EOLRecord(
        part_code="Cisco C886VAJ-K9", vendor="Cisco", model="Cisco C886VAJ-K9",
        end_of_sale=date(2020, 10, 29), end_of_support=date(2025, 10, 31), end_of_sw_maint=date(2021, 10, 29),
        replacement_sku="C1117-4P",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "C8300-1N1S-6T": EOLRecord(
        part_code="C8300-1N1S-6T", vendor="Cisco", model="C8300-1N1S-6T",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO3945E/K9": EOLRecord(
        part_code="CISCO3945E/K9", vendor="Cisco", model="CISCO3945E/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4431/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C1-CISCO4451/K9": EOLRecord(
        part_code="C1-CISCO4451/K9", vendor="Cisco", model="C1-CISCO4451/K9",
        end_of_sale=date(2022, 10, 28), end_of_support=date(2027, 10, 31), end_of_sw_maint=date(2023, 10, 28),
        replacement_sku="ISR4451-X/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C1-CISCO4321/K9": EOLRecord(
        part_code="C1-CISCO4321/K9", vendor="Cisco", model="C1-CISCO4321/K9",
        end_of_sale=date(2022, 10, 28), end_of_support=date(2027, 10, 31), end_of_sw_maint=date(2023, 10, 28),
        replacement_sku="ISR4321/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASR1001X-2.5G-K9": EOLRecord(
        part_code="ASR1001X-2.5G-K9", vendor="Cisco", model="ASR1001X-2.5G-K9",
        end_of_sale=date(2022, 8, 1), end_of_support=date(2027, 7, 31), end_of_sw_maint=date(2023, 1, 8),
        replacement_sku="C8500L-8S4X",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO 2851": EOLRecord(
        part_code="Cisco 2851", vendor="Cisco", model="Cisco 2851",
        end_of_sale=date(2015, 8, 7), end_of_support=date(2020, 8, 31), end_of_sw_maint=date(2016, 6, 8),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO C897VAG-LTE-GA-K9": EOLRecord(
        part_code="Cisco C897VAG-LTE-GA-K9", vendor="Cisco", model="Cisco C897VAG-LTE-GA-K9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C1113-8PLTELA": EOLRecord(
        part_code="C1113-8PLTELA", vendor="Cisco", model="C1113-8PLTELA",
        end_of_sale=date(2023, 5, 9), end_of_support=date(2028, 5, 31), end_of_sw_maint=date(2024, 8, 5),
        replacement_sku="C1131-8PLTEPWZ",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO892-K9": EOLRecord(
        part_code="CISCO892-K9", vendor="Cisco", model="CISCO892-K9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "TL-MR6400": EOLRecord(
        part_code="TL-MR6400", vendor="Cisco", model="TL-MR6400",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO C1113-8PLTELA": EOLRecord(
        part_code="Cisco C1113-8PLTELA", vendor="Cisco", model="Cisco C1113-8PLTELA",
        end_of_sale=date(2023, 5, 9), end_of_support=date(2028, 5, 31), end_of_sw_maint=date(2024, 8, 5),
        replacement_sku="C1131-8PLTEP",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASR1001=": EOLRecord(
        part_code="ASR1001=", vendor="Cisco", model="ASR1001=",
        end_of_sale=date(2016, 4, 29), end_of_support=date(2021, 4, 30), end_of_sw_maint=None,
        replacement_sku="ASR1001-X=",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASR1001-X": EOLRecord(
        part_code="ASR1001-X", vendor="Cisco", model="ASR1001-X",
        end_of_sale=date(2022, 8, 1), end_of_support=date(2027, 7, 31), end_of_sw_maint=date(2023, 1, 8),
        replacement_sku="C8500L-8S4X",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO888G-K9": EOLRecord(
        part_code="CISCO888G-K9", vendor="Cisco", model="CISCO888G-K9",
        end_of_sale=date(2012, 10, 10), end_of_support=date(2017, 10, 31), end_of_sw_maint=date(2013, 10, 10),
        replacement_sku="no replacement available",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1841": EOLRecord(
        part_code="CISCO1841", vendor="Cisco", model="CISCO1841",
        end_of_sale=date(2014, 5, 7), end_of_support=date(2023, 10, 31), end_of_sw_maint=None,
        replacement_sku="CISCO1941",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1841-ADSL": EOLRecord(
        part_code="CISCO1841-ADSL", vendor="Cisco", model="CISCO1841-ADSL",
        end_of_sale=date(2014, 5, 7), end_of_support=date(2023, 10, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO3845-HSEC/K9": EOLRecord(
        part_code="CISCO3845-HSEC/K9", vendor="Cisco", model="CISCO3845-HSEC/K9",
        end_of_sale=date(2011, 11, 1), end_of_support=date(2016, 10, 31), end_of_sw_maint=date(2014, 10, 31),
        replacement_sku="CISCO3945E-SEC/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO881-K9": EOLRecord(
        part_code="CISCO881-K9", vendor="Cisco", model="CISCO881-K9",
        end_of_sale=date(2014, 8, 22), end_of_support=date(2019, 8, 31), end_of_sw_maint=date(2015, 8, 22),
        replacement_sku="C881-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C886VAJ-K9": EOLRecord(
        part_code="C886VAJ-K9", vendor="Cisco", model="C886VAJ-K9",
        end_of_sale=date(2020, 4, 29), end_of_support=date(2025, 4, 30), end_of_sw_maint=date(2021, 4, 29),
        replacement_sku="C1117-4P",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4331-AXV/K9": EOLRecord(
        part_code="ISR4331-AXV/K9", vendor="Cisco", model="ISR4331-AXV/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C887VAG-4G-GA-K9": EOLRecord(
        part_code="C887VAG-4G-GA-K9", vendor="Cisco", model="C887VAG-4G-GA-K9",
        end_of_sale=date(2019, 7, 29), end_of_support=date(2024, 7, 31), end_of_sw_maint=date(2020, 7, 28),
        replacement_sku="C1117-4PLTEEA",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3560CX-8TC-S": EOLRecord(
        part_code="WS-C3560CX-8TC-S", vendor="Cisco", model="WS-C3560CX-8TC-S",
        end_of_sale=date(2024, 4, 30), end_of_support=date(2029, 4, 30), end_of_sw_maint=date(2025, 4, 30),
        replacement_sku="C9200CX-12T-2X2G-A",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C921-4PLTEGB": EOLRecord(
        part_code="C921-4PLTEGB", vendor="Cisco", model="C921-4PLTEGB",
        end_of_sale=date(2022, 4, 30), end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C927-4PLTEGB": EOLRecord(
        part_code="C927-4PLTEGB", vendor="Cisco", model="C927-4PLTEGB",
        end_of_sale=date(2022, 4, 30), end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1712": EOLRecord(
        part_code="CISCO1712", vendor="Cisco", model="CISCO1712",
        end_of_sale=date(2007, 3, 27), end_of_support=date(2012, 3, 27), end_of_sw_maint=None,
        replacement_sku="no replacement available",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1841-HSEC/K9": EOLRecord(
        part_code="CISCO1841-HSEC/K9", vendor="Cisco", model="CISCO1841-HSEC/K9",
        end_of_sale=date(2011, 11, 1), end_of_support=date(2016, 10, 31), end_of_sw_maint=date(2014, 10, 31),
        replacement_sku="CISCO1941-SEC/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO857-K9": EOLRecord(
        part_code="CISCO857-K9", vendor="Cisco", model="CISCO857-K9",
        end_of_sale=date(2011, 12, 20), end_of_support=date(2016, 12, 31), end_of_sw_maint=date(2013, 12, 19),
        replacement_sku="CISCO887VA-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1905BR/K9=": EOLRecord(
        part_code="CISCO1905BR/K9=", vendor="Cisco", model="CISCO1905BR/K9=",
        end_of_sale=date(2020, 5, 8), end_of_support=date(2025, 5, 31), end_of_sw_maint=date(2021, 8, 5),
        replacement_sku="ISR4221/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1905BR/K9": EOLRecord(
        part_code="CISCO1905BR/K9", vendor="Cisco", model="CISCO1905BR/K9",
        end_of_sale=date(2020, 5, 8), end_of_support=date(2025, 5, 31), end_of_sw_maint=date(2021, 8, 5),
        replacement_sku="ISR4221/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1721": EOLRecord(
        part_code="CISCO1721", vendor="Cisco", model="CISCO1721",
        end_of_sale=date(2007, 3, 27), end_of_support=date(2012, 3, 27), end_of_sw_maint=None,
        replacement_sku="Wic-1t",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO877-M-K9": EOLRecord(
        part_code="CISCO877-M-K9", vendor="Cisco", model="CISCO877-M-K9",
        end_of_sale=date(2012, 6, 15), end_of_support=date(2017, 6, 30), end_of_sw_maint=date(2013, 6, 15),
        replacement_sku="CISCO887VA-M-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO877-SEC-K9": EOLRecord(
        part_code="CISCO877-SEC-K9", vendor="Cisco", model="CISCO877-SEC-K9",
        end_of_sale=date(2011, 12, 20), end_of_support=date(2016, 12, 31), end_of_sw_maint=date(2012, 12, 19),
        replacement_sku="CISCO887VA-SEC-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1801/K9": EOLRecord(
        part_code="CISCO1801/K9", vendor="Cisco", model="CISCO1801/K9",
        end_of_sale=date(2023, 10, 31), end_of_support=date(2018, 3, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2621XM": EOLRecord(
        part_code="CISCO2621XM", vendor="Cisco", model="CISCO2621XM",
        end_of_sale=date(2007, 3, 27), end_of_support=date(2012, 3, 27), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO 1841": EOLRecord(
        part_code="CISCO 1841", vendor="Cisco", model="CISCO 1841",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO876-SEC-I-K9": EOLRecord(
        part_code="CISCO876-SEC-I-K9", vendor="Cisco", model="CISCO876-SEC-I-K9",
        end_of_sale=date(2011, 12, 20), end_of_support=date(2016, 12, 31), end_of_sw_maint=date(2013, 12, 19),
        replacement_sku="CISCO886VA-SEC-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "1801": EOLRecord(
        part_code="1801", vendor="Cisco", model="1801",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1801": EOLRecord(
        part_code="CISCO1801", vendor="Cisco", model="CISCO1801",
        end_of_sale=date(2023, 10, 31), end_of_support=date(2018, 3, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1841-SEC/K9": EOLRecord(
        part_code="CISCO1841-SEC/K9", vendor="Cisco", model="CISCO1841-SEC/K9",
        end_of_sale=date(2014, 5, 7), end_of_support=date(2023, 10, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO887-SEC-K9": EOLRecord(
        part_code="CISCO887-SEC-K9", vendor="Cisco", model="CISCO887-SEC-K9",
        end_of_sale=date(2011, 12, 20), end_of_support=date(2016, 12, 31), end_of_sw_maint=date(2013, 12, 19),
        replacement_sku="CISCO887VA-SEC-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C819G-4G-GA-K9": EOLRecord(
        part_code="C819G-4G-GA-K9", vendor="Cisco", model="C819G-4G-GA-K9",
        end_of_sale=date(2019, 7, 29), end_of_support=date(2024, 7, 31), end_of_sw_maint=date(2020, 7, 29),
        replacement_sku="C1111-4PLTEEA",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO 1801": EOLRecord(
        part_code="Cisco 1801", vendor="Cisco", model="Cisco 1801",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASA5510": EOLRecord(
        part_code="ASA5510", vendor="Cisco", model="ASA5510",
        end_of_sale=date(2013, 9, 16), end_of_support=date(2018, 9, 30), end_of_sw_maint=date(2014, 9, 16),
        replacement_sku="ASA5515VPN",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C819HG-4G-G-K9": EOLRecord(
        part_code="C819HG-4G-G-K9", vendor="Cisco", model="C819HG-4G-G-K9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MR36-HW": EOLRecord(
        part_code="MR36-HW", vendor="Cisco", model="MR36-HW",
        end_of_sale=date(2022, 7, 14), end_of_support=date(2026, 7, 21), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1803/K9": EOLRecord(
        part_code="CISCO1803/K9", vendor="Cisco", model="CISCO1803/K9",
        end_of_sale=date(2014, 5, 7), end_of_support=date(2023, 10, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "1760-V": EOLRecord(
        part_code="1760-V", vendor="Cisco", model="1760-V",
        end_of_sale=date(2007, 3, 27), end_of_support=date(2012, 3, 27), end_of_sw_maint=None,
        replacement_sku="no replacement available",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "871-K9": EOLRecord(
        part_code="871-K9", vendor="Cisco", model="871-K9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="881-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASR1001X-5G-K9": EOLRecord(
        part_code="ASR1001X-5G-K9", vendor="Cisco", model="ASR1001X-5G-K9",
        end_of_sale=date(2022, 8, 1), end_of_support=date(2027, 7, 31), end_of_sw_maint=date(2023, 1, 8),
        replacement_sku="C8500L-8S4X",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO877": EOLRecord(
        part_code="CISCO877", vendor="Cisco", model="CISCO877",
        end_of_sale=date(2012, 6, 15), end_of_support=date(2017, 6, 30), end_of_sw_maint=date(2013, 6, 15),
        replacement_sku="CISCO887VA",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2610XM": EOLRecord(
        part_code="CISCO2610XM", vendor="Cisco", model="CISCO2610XM",
        end_of_sale=None, end_of_support=date(2012, 3, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "2811-SHDSL-V3/K9": EOLRecord(
        part_code="2811-SHDSL-V3/K9", vendor="Cisco", model="2811-SHDSL-V3/K9",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1841-SHDSL-V3": EOLRecord(
        part_code="CISCO1841-SHDSL-V3", vendor="Cisco", model="CISCO1841-SHDSL-V3",
        end_of_sale=date(2014, 5, 7), end_of_support=date(2023, 10, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO891-K9-RF": EOLRecord(
        part_code="CISCO891-K9-RF", vendor="Cisco", model="CISCO891-K9-RF",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO891-K9": EOLRecord(
        part_code="CISCO891-K9", vendor="Cisco", model="CISCO891-K9",
        end_of_sale=date(2014, 8, 22), end_of_support=date(2019, 8, 31), end_of_sw_maint=date(2015, 8, 22),
        replacement_sku="C891F-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1811/K9": EOLRecord(
        part_code="CISCO1811/K9", vendor="Cisco", model="CISCO1811/K9",
        end_of_sale=date(2014, 5, 7), end_of_support=date(2023, 10, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MR 36": EOLRecord(
        part_code="MR 36", vendor="Cisco", model="MR 36",
        end_of_sale=date(2022, 7, 14), end_of_support=date(2026, 7, 21), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MR36": EOLRecord(
        part_code="MR36", vendor="Cisco", model="MR36",
        end_of_sale=date(2022, 7, 14), end_of_support=date(2026, 7, 21), end_of_sw_maint=None,
        replacement_sku="9162",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO C1111-8P": EOLRecord(
        part_code="Cisco C1111-8P", vendor="Cisco", model="Cisco C1111-8P",
        end_of_sale=date(2023, 5, 9), end_of_support=date(2028, 5, 31), end_of_sw_maint=date(2024, 8, 5),
        replacement_sku="ISR 1100 8P",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C1111_8P": EOLRecord(
        part_code="C1111_8P", vendor="Cisco", model="C1111_8P",
        end_of_sale=date(2023, 5, 9), end_of_support=date(2028, 5, 31), end_of_sw_maint=date(2024, 8, 5),
        replacement_sku="C1131-8PWA",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1111": EOLRecord(
        part_code="CISCO1111", vendor="Cisco", model="CISCO1111",
        end_of_sale=date(2023, 5, 9), end_of_support=date(2028, 5, 31), end_of_sw_maint=date(2024, 8, 5),
        replacement_sku="CISCO1131",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1111-8P": EOLRecord(
        part_code="CISCO1111-8P", vendor="Cisco", model="CISCO1111-8P",
        end_of_sale=date(2023, 5, 9), end_of_support=date(2028, 5, 31), end_of_sw_maint=date(2024, 8, 5),
        replacement_sku="C1131-8P",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MR33-HW": EOLRecord(
        part_code="MR33-HW", vendor="Cisco", model="MR33-HW",
        end_of_sale=date(2022, 7, 14), end_of_support=date(2026, 7, 21), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MR33": EOLRecord(
        part_code="MR33", vendor="Cisco", model="MR33",
        end_of_sale=date(2022, 7, 14), end_of_support=date(2026, 7, 21), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MR18": EOLRecord(
        part_code="MR18", vendor="Cisco", model="MR18",
        end_of_sale=date(2017, 2, 13), end_of_support=date(2024, 3, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MR18-HW": EOLRecord(
        part_code="MR18-HW", vendor="Cisco", model="MR18-HW",
        end_of_sale=date(2017, 2, 13), end_of_support=date(2024, 3, 31), end_of_sw_maint=None,
        replacement_sku="MR32-HW",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MG21E-HW-WW": EOLRecord(
        part_code="MG21E-HW-WW", vendor="Cisco", model="MG21E-HW-WW",
        end_of_sale=date(2024, 9, 18), end_of_support=date(2029, 9, 18), end_of_sw_maint=None,
        replacement_sku="MG41E-HW",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C1111": EOLRecord(
        part_code="C1111", vendor="Cisco", model="C1111",
        end_of_sale=date(2023, 5, 9), end_of_support=date(2028, 5, 31), end_of_sw_maint=date(2024, 8, 5),
        replacement_sku="C1131",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C1117-4P": EOLRecord(
        part_code="C1117-4P", vendor="Cisco", model="C1117-4P",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="C1131-8P",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MG21E-WW": EOLRecord(
        part_code="MG21E-WW", vendor="Cisco", model="MG21E-WW",
        end_of_sale=date(2024, 9, 18), end_of_support=date(2029, 9, 18), end_of_sw_maint=None,
        replacement_sku="MG41E-HW",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CBS350-8T-E-2G": EOLRecord(
        part_code="CBS350-8T-E-2G", vendor="Cisco", model="CBS350-8T-E-2G",
        end_of_sale=date(2024, 10, 29), end_of_support=date(2029, 10, 31), end_of_sw_maint=date(2025, 10, 29),
        replacement_sku="C1300-8T-E-2G",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASR1001X-20G-K9": EOLRecord(
        part_code="ASR1001X-20G-K9", vendor="Cisco", model="ASR1001X-20G-K9",
        end_of_sale=date(2022, 8, 1), end_of_support=date(2027, 7, 31), end_of_sw_maint=date(2023, 1, 8),
        replacement_sku="C8500L-8S4X",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2921/K9": EOLRecord(
        part_code="CISCO2921/K9", vendor="Cisco", model="CISCO2921/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4331/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3850-48T-E": EOLRecord(
        part_code="WS-C3850-48T-E", vendor="Cisco", model="WS-C3850-48T-E",
        end_of_sale=date(2020, 10, 30), end_of_support=date(2025, 10, 31), end_of_sw_maint=date(2021, 10, 30),
        replacement_sku="C9300-48T-A",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "VANCO RACK POSITION (1U)": EOLRecord(
        part_code="Vanco rack position (1U)", vendor="Cisco", model="Vanco rack position (1U)",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO 881": EOLRecord(
        part_code="Cisco 881", vendor="Cisco", model="Cisco 881",
        end_of_sale=date(2025, 10, 31), end_of_support=date(2025, 10, 31), end_of_sw_maint=date(2025, 10, 31),
        replacement_sku="C921-4P",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO891-K9-SEC/K9": EOLRecord(
        part_code="CISCO891-K9-SEC/K9", vendor="Cisco", model="CISCO891-K9-SEC/K9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO 891": EOLRecord(
        part_code="Cisco 891", vendor="Cisco", model="Cisco 891",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "4X AIR-ANT2524DW-R=": EOLRecord(
        part_code="4x AIR-ANT2524DW-R=", vendor="Cisco", model="4x AIR-ANT2524DW-R=",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ACS-890-RM-19=": EOLRecord(
        part_code="ACS-890-RM-19=", vendor="Cisco", model="ACS-890-RM-19=",
        end_of_sale=date(2023, 11, 21), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2024, 11, 20),
        replacement_sku="no replacement available",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "HWIC-1T": EOLRecord(
        part_code="HWIC-1T", vendor="Cisco", model="HWIC-1T",
        end_of_sale=date(2019, 2, 22), end_of_support=date(2024, 2, 29), end_of_sw_maint=date(2020, 2, 22),
        replacement_sku="NIM-1T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "HWIC-1T=": EOLRecord(
        part_code="HWIC-1T=", vendor="Cisco", model="HWIC-1T=",
        end_of_sale=date(2019, 2, 22), end_of_support=date(2024, 2, 29), end_of_sw_maint=date(2020, 2, 22),
        replacement_sku="NIM-1T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO C921-4P": EOLRecord(
        part_code="Cisco C921-4P", vendor="Cisco", model="Cisco C921-4P",
        end_of_sale=date(2022, 4, 30), end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C921": EOLRecord(
        part_code="C921", vendor="Cisco", model="C921",
        end_of_sale=date(2022, 4, 30), end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "SL-880-AIS=": EOLRecord(
        part_code="SL-880-AIS=", vendor="Cisco", model="SL-880-AIS=",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C921-4P-SEC/K9": EOLRecord(
        part_code="C921-4P-SEC/K9", vendor="Cisco", model="C921-4P-SEC/K9",
        end_of_sale=date(2022, 4, 30), end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "AIR-AP2802E-H-K9": EOLRecord(
        part_code="AIR-AP2802E-H-K9", vendor="Cisco", model="AIR-AP2802E-H-K9",
        end_of_sale=date(2022, 10, 31), end_of_support=date(2027, 10, 31), end_of_sw_maint=date(2024, 1, 5),
        replacement_sku="Cisco Catalyst 9120AX Series Access Points",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "C8200L-1N-4T": EOLRecord(
        part_code="C8200L-1N-4T", vendor="Cisco", model="C8200L-1N-4T",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C891F-K9-SEC/K9": EOLRecord(
        part_code="C891F-K9-SEC/K9", vendor="Cisco", model="C891F-K9-SEC/K9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data not found
    "FGL2148943Q": EOLRecord(
        part_code="FGL2148943Q", vendor="Cisco", model="FGL2148943Q",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="none",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C921-4PAS": EOLRecord(
        part_code="C921-4PAS", vendor="Cisco", model="C921-4PAS",
        end_of_sale=date(2022, 4, 30), end_of_support=None, end_of_sw_maint=None,
        replacement_sku="C921-4P",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "AIR-CT5508-50-K9": EOLRecord(
        part_code="AIR-CT5508-50-K9", vendor="Cisco", model="AIR-CT5508-50-K9",
        end_of_sale=date(2018, 5, 4), end_of_support=date(2023, 7, 31), end_of_sw_maint=date(2019, 1, 8),
        replacement_sku="AIR-CT3504-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "AIR-PWR-5500-AC=": EOLRecord(
        part_code="AIR-PWR-5500-AC=", vendor="Cisco", model="AIR-PWR-5500-AC=",
        end_of_sale=date(2018, 5, 4), end_of_support=date(2023, 7, 31), end_of_sw_maint=date(2019, 1, 8),
        replacement_sku="Cisco 5520 Wireless Controller",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "L-LIC-CT5508-5A": EOLRecord(
        part_code="L-LIC-CT5508-5A", vendor="Cisco", model="L-LIC-CT5508-5A",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "C9115AXI-S": EOLRecord(
        part_code="C9115AXI-S", vendor="Cisco", model="C9115AXI-S",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "GLC-LH-SMD=": EOLRecord(
        part_code="GLC-LH-SMD=", vendor="Cisco", model="GLC-LH-SMD=",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO C891F-K9": EOLRecord(
        part_code="Cisco C891F-K9", vendor="Cisco", model="Cisco C891F-K9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "AIR-SAP1602I-Q-K9": EOLRecord(
        part_code="AIR-SAP1602I-Q-K9", vendor="Cisco", model="AIR-SAP1602I-Q-K9",
        end_of_sale=None, end_of_support=date(2021, 12, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "AIR-SAP2602E-S-K9": EOLRecord(
        part_code="AIR-SAP2602E-S-K9", vendor="Cisco", model="AIR-SAP2602E-S-K9",
        end_of_sale=date(2016, 12, 29), end_of_support=date(2021, 12, 31), end_of_sw_maint=date(2017, 12, 29),
        replacement_sku="AIR-AP2802E-S-K9C",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO 7204VXR": EOLRecord(
        part_code="CISCO 7204VXR", vendor="Cisco", model="CISCO 7204VXR",
        end_of_sale=date(2012, 9, 29), end_of_support=date(2017, 9, 30), end_of_sw_maint=date(2015, 9, 29),
        replacement_sku="ASR1001",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO7206VXR": EOLRecord(
        part_code="CISCO7206VXR", vendor="Cisco", model="CISCO7206VXR",
        end_of_sale=date(2012, 9, 29), end_of_support=date(2017, 9, 30), end_of_sw_maint=date(2015, 9, 29),
        replacement_sku="CISCO7206VXR",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2651": EOLRecord(
        part_code="cisco2651", vendor="Cisco", model="cisco2651",
        end_of_sale=date(2003, 4, 26), end_of_support=date(2008, 4, 26), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2811-HSEC/K9": EOLRecord(
        part_code="CISCO2811-HSEC/K9", vendor="Cisco", model="CISCO2811-HSEC/K9",
        end_of_sale=None, end_of_support=date(2016, 10, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO3640": EOLRecord(
        part_code="CISCO3640", vendor="Cisco", model="CISCO3640",
        end_of_sale=date(2003, 12, 31), end_of_support=date(2008, 12, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO887VA-M-K9": EOLRecord(
        part_code="CISCO887VA-M-K9", vendor="Cisco", model="CISCO887VA-M-K9",
        end_of_sale=date(2014, 8, 22), end_of_support=date(2019, 8, 31), end_of_sw_maint=date(2015, 8, 22),
        replacement_sku="C887VAM-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2950SX-24": EOLRecord(
        part_code="WS-C2950SX-24", vendor="Cisco", model="WS-C2950SX-24",
        end_of_sale=date(2008, 10, 21), end_of_support=date(2013, 10, 20), end_of_sw_maint=date(2009, 10, 21),
        replacement_sku="WS-C2960-24TC-S",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2821": EOLRecord(
        part_code="CISCO2821", vendor="Cisco", model="CISCO2821",
        end_of_sale=date(2011, 11, 1), end_of_support=date(2016, 10, 31), end_of_sw_maint=date(2014, 10, 31),
        replacement_sku="CISCO2921/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2821-V/K9": EOLRecord(
        part_code="CISCO2821-V/K9", vendor="Cisco", model="CISCO2821-V/K9",
        end_of_sale=None, end_of_support=date(2016, 10, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C1921": EOLRecord(
        part_code="C1921", vendor="Cisco", model="C1921",
        end_of_sale=date(2018, 9, 29), end_of_support=date(2023, 9, 30), end_of_sw_maint=date(2019, 9, 29),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "2811": EOLRecord(
        part_code="2811", vendor="Cisco", model="2811",
        end_of_sale=date(2011, 11, 1), end_of_support=date(2016, 11, 1), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2801-HSEC/K9": EOLRecord(
        part_code="CISCO2801-HSEC/K9", vendor="Cisco", model="CISCO2801-HSEC/K9",
        end_of_sale=date(2011, 11, 1), end_of_support=date(2016, 10, 31), end_of_sw_maint=date(2014, 10, 31),
        replacement_sku="CISCO2901/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO3725": EOLRecord(
        part_code="CISCO3725", vendor="Cisco", model="CISCO3725",
        end_of_sale=date(2007, 3, 27), end_of_support=date(2012, 3, 27), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO 3640": EOLRecord(
        part_code="Cisco 3640", vendor="Cisco", model="Cisco 3640",
        end_of_sale=date(2003, 12, 31), end_of_support=date(2008, 12, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "3640": EOLRecord(
        part_code="3640", vendor="Cisco", model="3640",
        end_of_sale=date(2003, 12, 31), end_of_support=date(2008, 12, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C2621XM-2FE/VPN/K9": EOLRecord(
        part_code="C2621XM-2FE/VPN/K9", vendor="Cisco", model="C2621XM-2FE/VPN/K9",
        end_of_sale=None, end_of_support=date(2012, 3, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "3640MBUNDLE-4B-U": EOLRecord(
        part_code="3640MBUNDLE-4B-U", vendor="Cisco", model="3640MBUNDLE-4B-U",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1603-R=": EOLRecord(
        part_code="CISCO1603-R=", vendor="Cisco", model="CISCO1603-R=",
        end_of_sale=date(2016, 12, 29), end_of_support=date(2021, 12, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2611XM=": EOLRecord(
        part_code="CISCO2611XM=", vendor="Cisco", model="CISCO2611XM=",
        end_of_sale=None, end_of_support=date(2012, 3, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3550-24-EMI": EOLRecord(
        part_code="WS-C3550-24-EMI", vendor="Cisco", model="WS-C3550-24-EMI",
        end_of_sale=date(2006, 5, 2), end_of_support=date(2011, 5, 2), end_of_sw_maint=date(2007, 2, 5),
        replacement_sku="WS-C3750-24TS-E WS-C3560-24TS-E",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO3640=": EOLRecord(
        part_code="CISCO3640=", vendor="Cisco", model="CISCO3640=",
        end_of_sale=date(2003, 12, 31), end_of_support=date(2008, 12, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO3620=": EOLRecord(
        part_code="CISCO3620=", vendor="Cisco", model="CISCO3620=",
        end_of_sale=None, end_of_support=date(2008, 12, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C1841-T1SEC/K9-MS": EOLRecord(
        part_code="C1841-T1SEC/K9-MS", vendor="Cisco", model="C1841-T1SEC/K9-MS",
        end_of_sale=date(2011, 11, 1), end_of_support=date(2016, 10, 31), end_of_sw_maint=date(2014, 10, 31),
        replacement_sku="no replacement available",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "1603": EOLRecord(
        part_code="1603", vendor="Cisco", model="1603",
        end_of_sale=date(2016, 12, 29), end_of_support=date(2021, 12, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2811-SEC/K9": EOLRecord(
        part_code="CISCO2811-SEC/K9", vendor="Cisco", model="CISCO2811-SEC/K9",
        end_of_sale=date(2011, 11, 1), end_of_support=date(2016, 10, 31), end_of_sw_maint=date(2014, 10, 31),
        replacement_sku="CISCO2911-SEC/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO ISR4221/K9": EOLRecord(
        part_code="Cisco ISR4221/K9", vendor="Cisco", model="Cisco ISR4221/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200L-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO1941-SECK9-RF": EOLRecord(
        part_code="CISCO1941-SECK9-RF", vendor="Cisco", model="CISCO1941-SECK9-RF",
        end_of_sale=date(2018, 9, 29), end_of_support=date(2023, 9, 30), end_of_sw_maint=date(2019, 9, 29),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO ISR 4221 K9": EOLRecord(
        part_code="Cisco ISR 4221 K9", vendor="Cisco", model="Cisco ISR 4221 K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200L-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO ISR4221": EOLRecord(
        part_code="Cisco ISR4221", vendor="Cisco", model="Cisco ISR4221",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200L-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2901-16TS/K9": EOLRecord(
        part_code="CISCO2901-16TS/K9", vendor="Cisco", model="CISCO2901-16TS/K9",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4321/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C1-CISCO4221/K9": EOLRecord(
        part_code="C1-CISCO4221/K9", vendor="Cisco", model="C1-CISCO4221/K9",
        end_of_sale=date(2022, 10, 28), end_of_support=date(2027, 10, 31), end_of_sw_maint=date(2023, 10, 28),
        replacement_sku="ISR4221/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4221/K9-RF": EOLRecord(
        part_code="ISR4221/K9-RF", vendor="Cisco", model="ISR4221/K9-RF",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200L-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO ISR 4221 / K9": EOLRecord(
        part_code="Cisco ISR 4221 / K9", vendor="Cisco", model="Cisco ISR 4221 / K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200L-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR 4221/SEC K9": EOLRecord(
        part_code="ISR 4221/Sec K9", vendor="Cisco", model="ISR 4221/Sec K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200L-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASR1001X-10G-VPN": EOLRecord(
        part_code="ASR1001X-10G-VPN", vendor="Cisco", model="ASR1001X-10G-VPN",
        end_of_sale=date(2022, 8, 1), end_of_support=date(2027, 7, 31), end_of_sw_maint=date(2023, 1, 8),
        replacement_sku="C8500L-8S4X",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "FP8120-K9": EOLRecord(
        part_code="FP8120-K9", vendor="Cisco", model="FP8120-K9",
        end_of_sale=date(2017, 12, 15), end_of_support=date(2022, 12, 31), end_of_sw_maint=None,
        replacement_sku="FPR 4100 NGIPS",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "FPNM-4CU-1G-BP=": EOLRecord(
        part_code="FPNM-4CU-1G-BP=", vendor="Cisco", model="FPNM-4CU-1G-BP=",
        end_of_sale=date(2019, 6, 10), end_of_support=date(2024, 6, 30), end_of_sw_maint=None,
        replacement_sku="no replacement available",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "AMP8350-K9": EOLRecord(
        part_code="AMP8350-K9", vendor="Cisco", model="AMP8350-K9",
        end_of_sale=date(2019, 6, 10), end_of_support=date(2024, 6, 30), end_of_sw_maint=None,
        replacement_sku="Firepower 9300 Series",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "FP8350-K9": EOLRecord(
        part_code="FP8350-K9", vendor="Cisco", model="FP8350-K9",
        end_of_sale=date(2019, 6, 10), end_of_support=date(2024, 6, 30), end_of_sw_maint=None,
        replacement_sku="Firepower 9300 Series",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "FP7125-K9": EOLRecord(
        part_code="FP7125-K9", vendor="Cisco", model="FP7125-K9",
        end_of_sale=date(2019, 6, 10), end_of_support=date(2024, 6, 30), end_of_sw_maint=None,
        replacement_sku="Firepower 2100 Series",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4221/K9-WS": EOLRecord(
        part_code="ISR4221/K9-WS", vendor="Cisco", model="ISR4221/K9-WS",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200L-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data not found
    "NIM-ES2-4=": EOLRecord(
        part_code="NIM-ES2-4=", vendor="Cisco", model="NIM-ES2-4=",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="none",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C891FJ-K9": EOLRecord(
        part_code="C891FJ-K9", vendor="Cisco", model="C891FJ-K9",
        end_of_sale=date(2019, 10, 29), end_of_support=date(2024, 10, 31), end_of_sw_maint=date(2020, 10, 28),
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2651XM": EOLRecord(
        part_code="CISCO2651XM", vendor="Cisco", model="CISCO2651XM",
        end_of_sale=date(2007, 3, 27), end_of_support=date(2012, 3, 27), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASR1001-2.5G-SECK9": EOLRecord(
        part_code="ASR1001-2.5G-SECK9", vendor="Cisco", model="ASR1001-2.5G-SECK9",
        end_of_sale=date(2013, 11, 29), end_of_support=date(2018, 11, 30), end_of_sw_maint=date(2014, 11, 29),
        replacement_sku="Cisco ASR 1002",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ISR4431-VSEC/K9": EOLRecord(
        part_code="ISR4431-VSEC/K9", vendor="Cisco", model="ISR4431-VSEC/K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8300-1N1S-4T2X",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO3945ESECK9-WS": EOLRecord(
        part_code="CISCO3945ESECK9-WS", vendor="Cisco", model="CISCO3945ESECK9-WS",
        end_of_sale=date(2017, 12, 9), end_of_support=date(2022, 12, 31), end_of_sw_maint=date(2020, 9, 12),
        replacement_sku="ISR4431-SEC/K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2951-SECK9-WS": EOLRecord(
        part_code="CISCO2951-SECK9-WS", vendor="Cisco", model="CISCO2951-SECK9-WS",
        end_of_sale=None, end_of_support=date(2022, 12, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Non Cisco
    "MX480": EOLRecord(
        part_code="MX480", vendor="Juniper", model="MX480",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="none",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "C2811-SHDSL-V3/K9": EOLRecord(
        part_code="C2811-SHDSL-V3/K9", vendor="Cisco", model="C2811-SHDSL-V3/K9",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO7206VXR=": EOLRecord(
        part_code="CISCO7206VXR=", vendor="Cisco", model="CISCO7206VXR=",
        end_of_sale=date(2012, 9, 29), end_of_support=date(2017, 9, 30), end_of_sw_maint=date(2015, 9, 29),
        replacement_sku="CISCO7206VXR=",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C2691-VPN/K9": EOLRecord(
        part_code="C2691-VPN/K9", vendor="Cisco", model="C2691-VPN/K9",
        end_of_sale=None, end_of_support=date(2012, 3, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO2621XM=": EOLRecord(
        part_code="CISCO2621XM=", vendor="Cisco", model="CISCO2621XM=",
        end_of_sale=date(2007, 3, 27), end_of_support=date(2012, 3, 27), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MR12 CLOUD MANAGED AP": EOLRecord(
        part_code="MR12 CLOUD MANAGED AP", vendor="Cisco", model="MR12 CLOUD MANAGED AP",
        end_of_sale=date(2015, 10, 24), end_of_support=date(2022, 10, 24), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MERAKI MR18": EOLRecord(
        part_code="Meraki MR18", vendor="Cisco", model="Meraki MR18",
        end_of_sale=date(2017, 2, 13), end_of_support=date(2024, 3, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MERAKI MR66": EOLRecord(
        part_code="Meraki MR66", vendor="Cisco", model="Meraki MR66",
        end_of_sale=date(2017, 6, 9), end_of_support=date(2024, 6, 9), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ASA5555": EOLRecord(
        part_code="ASA5555", vendor="Cisco", model="ASA5555",
        end_of_sale=date(2020, 9, 4), end_of_support=date(2025, 9, 30), end_of_sw_maint=date(2021, 4, 9),
        replacement_sku="Cisco Firepower 2100 Series",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "BE7H-M5-K9": EOLRecord(
        part_code="BE7H-M5-K9", vendor="Cisco", model="BE7H-M5-K9",
        end_of_sale=date(2023, 3, 2), end_of_support=date(2028, 2, 29), end_of_sw_maint=None,
        replacement_sku="BE7H-M6-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C240 - PAIX-UCS01 - PAIX-ESX01": EOLRecord(
        part_code="C240 - PAIX-UCS01 - PAIX-ESX01", vendor="Cisco", model="C240 - PAIX-UCS01 - PAIX-ESX01",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "UCS-C260M2-VCD2": EOLRecord(
        part_code="UCS-C260M2-VCD2", vendor="Cisco", model="UCS-C260M2-VCD2",
        end_of_sale=None, end_of_support=date(2019, 7, 27), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C260 - PATH2-UCS03 - PATH2-ESX03": EOLRecord(
        part_code="C260 - PATH2-UCS03 - PATH2-ESX03", vendor="Cisco", model="C260 - PATH2-UCS03 - PATH2-ESX03",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C240 - PATH2-UCS02 - PATH2-ESX02": EOLRecord(
        part_code="C240 - PATH2-UCS02 - PATH2-ESX02", vendor="Cisco", model="C240 - PATH2-UCS02 - PATH2-ESX02",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "SNS-3415-K9": EOLRecord(
        part_code="SNS-3415-K9", vendor="Cisco", model="SNS-3415-K9",
        end_of_sale=date(2023, 11, 7), end_of_support=date(2028, 11, 30), end_of_sw_maint=date(2025, 8, 31),
        replacement_sku="C8200-1N-4T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "3415-K9": EOLRecord(
        part_code="3415-K9", vendor="Cisco", model="3415-K9",
        end_of_sale=date(2016, 10, 7), end_of_support=date(2019, 10, 31), end_of_sw_maint=date(2017, 7, 10),
        replacement_sku="Cisco Secure Network Server (SNS) 3515 or 3595 Appliance",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "SRW224G4-K9-EU": EOLRecord(
        part_code="SRW224G4-K9-EU", vendor="Cisco", model="SRW224G4-K9-EU",
        end_of_sale=date(2018, 10, 4), end_of_support=date(2023, 10, 31), end_of_sw_maint=date(2019, 4, 10),
        replacement_sku="SF350-24-K9-EU",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ATA186": EOLRecord(
        part_code="ATA186", vendor="Cisco", model="ATA186",
        end_of_sale=date(2010, 9, 28), end_of_support=date(2015, 9, 30), end_of_sw_maint=None,
        replacement_sku="Cisco ATA 187",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO ATA 186": EOLRecord(
        part_code="Cisco ATA 186", vendor="Cisco", model="Cisco ATA 186",
        end_of_sale=date(2010, 9, 28), end_of_support=date(2015, 9, 30), end_of_sw_maint=None,
        replacement_sku="Cisco ATA 187",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO ATA 186I228": EOLRecord(
        part_code="CISCO ATA 186I228", vendor="Cisco", model="CISCO ATA 186I228",
        end_of_sale=date(2010, 9, 28), end_of_support=date(2015, 9, 30), end_of_sw_maint=None,
        replacement_sku="Cisco ATA 187",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ATA186-I2-A=": EOLRecord(
        part_code="ATA186-I2-A=", vendor="Cisco", model="ATA186-I2-A=",
        end_of_sale=date(2010, 9, 28), end_of_support=date(2015, 9, 30), end_of_sw_maint=None,
        replacement_sku="Cisco ATA 187",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO ATA 191": EOLRecord(
        part_code="Cisco ATA 191", vendor="Cisco", model="Cisco ATA 191",
        end_of_sale=date(2019, 3, 15), end_of_support=date(2024, 3, 31), end_of_sw_maint=date(2020, 3, 14),
        replacement_sku="ATA191-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO ATA186I2": EOLRecord(
        part_code="Cisco ATA186I2", vendor="Cisco", model="Cisco ATA186I2",
        end_of_sale=date(2010, 9, 28), end_of_support=date(2015, 9, 30), end_of_sw_maint=None,
        replacement_sku="Cisco ATA 187",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "SRW224G4-K9-NA-WS": EOLRecord(
        part_code="SRW224G4-K9-NA-WS", vendor="Cisco", model="SRW224G4-K9-NA-WS",
        end_of_sale=date(2018, 10, 4), end_of_support=date(2023, 10, 31), end_of_sw_maint=date(2019, 4, 10),
        replacement_sku="SF350-24-K9-NA",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO ATA 186I187": EOLRecord(
        part_code="CISCO ATA 186I187", vendor="Cisco", model="CISCO ATA 186I187",
        end_of_sale=date(2010, 9, 28), end_of_support=date(2015, 9, 30), end_of_sw_maint=None,
        replacement_sku="Cisco ATA 187",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO ATA 186I235": EOLRecord(
        part_code="CISCO ATA 186I235", vendor="Cisco", model="CISCO ATA 186I235",
        end_of_sale=date(2010, 9, 28), end_of_support=date(2015, 9, 30), end_of_sw_maint=None,
        replacement_sku="Cisco ATA 187",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO ATA 186I257": EOLRecord(
        part_code="CISCO ATA 186I257", vendor="Cisco", model="CISCO ATA 186I257",
        end_of_sale=date(2010, 9, 28), end_of_support=date(2015, 9, 30), end_of_sw_maint=None,
        replacement_sku="Cisco ATA 187",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO ATA 186I324": EOLRecord(
        part_code="CISCO ATA 186I324", vendor="Cisco", model="CISCO ATA 186I324",
        end_of_sale=date(2010, 9, 28), end_of_support=date(2015, 9, 30), end_of_sw_maint=None,
        replacement_sku="Cisco ATA 187",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO ATA 186I340": EOLRecord(
        part_code="CISCO ATA 186I340", vendor="Cisco", model="CISCO ATA 186I340",
        end_of_sale=date(2010, 9, 28), end_of_support=date(2015, 9, 30), end_of_sw_maint=None,
        replacement_sku="Cisco ATA 187",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960X-48TS-L": EOLRecord(
        part_code="WS-C2960X-48TS-L", vendor="Cisco", model="WS-C2960X-48TS-L",
        end_of_sale=date(2022, 10, 31), end_of_support=date(2027, 10, 31), end_of_sw_maint=date(2023, 10, 31),
        replacement_sku="C9200L-48T-4G",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3850-24S-S": EOLRecord(
        part_code="WS-C3850-24S-S", vendor="Cisco", model="WS-C3850-24S-S",
        end_of_sale=date(2022, 4, 30), end_of_support=date(2027, 4, 30), end_of_sw_maint=date(2023, 4, 30),
        replacement_sku="C9300-24S",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3850-12XS-E": EOLRecord(
        part_code="WS-C3850-12XS-E", vendor="Cisco", model="WS-C3850-12XS-E",
        end_of_sale=date(2022, 4, 30), end_of_support=date(2027, 4, 30), end_of_sw_maint=date(2023, 4, 30),
        replacement_sku="C9300X-12Y",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960X-24PS-L": EOLRecord(
        part_code="WS-C2960X-24PS-L", vendor="Cisco", model="WS-C2960X-24PS-L",
        end_of_sale=date(2022, 10, 31), end_of_support=date(2027, 10, 31), end_of_sw_maint=date(2023, 10, 31),
        replacement_sku="C9200L-24P-4G",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3650-24TS-E": EOLRecord(
        part_code="WS-C3650-24TS-E", vendor="Cisco", model="WS-C3650-24TS-E",
        end_of_sale=date(2021, 10, 31), end_of_support=date(2026, 10, 31), end_of_sw_maint=date(2022, 10, 31),
        replacement_sku="C9300L-24T-4G-A",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "24-PORT 10/100 POE MANAGED SWITCH": EOLRecord(
        part_code="24-Port 10/100 PoE Managed Switch", vendor="Cisco", model="24-Port 10/100 PoE Managed Switch",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "SRW224G4P-K9-EU": EOLRecord(
        part_code="SRW224G4P-K9-EU", vendor="Cisco", model="SRW224G4P-K9-EU",
        end_of_sale=date(2015, 4, 27), end_of_support=date(2020, 4, 30), end_of_sw_maint=date(2015, 4, 27),
        replacement_sku="SF300-24PP-K9-EU",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960-48PST-L": EOLRecord(
        part_code="WS-C2960-48PST-L", vendor="Cisco", model="WS-C2960-48PST-L",
        end_of_sale=date(2014, 10, 31), end_of_support=date(2019, 10, 31), end_of_sw_maint=date(2015, 10, 31),
        replacement_sku="WS-C2960-48PST-L",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "SF300-24PP-K9-UK": EOLRecord(
        part_code="SF300-24PP-K9-UK", vendor="Cisco", model="SF300-24PP-K9-UK",
        end_of_sale=date(2018, 10, 4), end_of_support=date(2019, 10, 4), end_of_sw_maint=date(2019, 4, 10),
        replacement_sku="SF350-24P-K9-UK",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "SF300-24PP-K9": EOLRecord(
        part_code="SF300-24PP-K9", vendor="Cisco", model="SF300-24PP-K9",
        end_of_sale=date(2018, 10, 4), end_of_support=date(2023, 10, 31), end_of_sw_maint=date(2019, 4, 10),
        replacement_sku="SF350-24P-K9",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data not found
    "DNI204604PK": EOLRecord(
        part_code="DNI204604PK", vendor="Cisco", model="DNI204604PK",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="none",
        source_url="master_assest_data.xlsx"),
    # Data found
    "SF300-24PP-K9-EU": EOLRecord(
        part_code="SF300-24PP-K9-EU", vendor="Cisco", model="SF300-24PP-K9-EU",
        end_of_sale=date(2018, 10, 4), end_of_support=date(2023, 10, 31), end_of_sw_maint=date(2019, 4, 10),
        replacement_sku="SF350-24P-K9-EU",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "SF-300": EOLRecord(
        part_code="SF-300", vendor="Cisco", model="SF-300",
        end_of_sale=None, end_of_support=date(2023, 10, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CBS350-24P-4G-UK": EOLRecord(
        part_code="CBS350-24P-4G-UK", vendor="Cisco", model="CBS350-24P-4G-UK",
        end_of_sale=date(2024, 10, 29), end_of_support=date(2029, 10, 31), end_of_sw_maint=date(2025, 10, 29),
        replacement_sku="C1300-24P-4G",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CBS350-24P-4G": EOLRecord(
        part_code="CBS350-24P-4G", vendor="Cisco", model="CBS350-24P-4G",
        end_of_sale=date(2024, 10, 29), end_of_support=date(2029, 10, 31), end_of_sw_maint=date(2025, 10, 29),
        replacement_sku="C1300-24P-4G",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960XR-24PS-I": EOLRecord(
        part_code="WS-C2960XR-24PS-I", vendor="Cisco", model="WS-C2960XR-24PS-I",
        end_of_sale=date(2022, 10, 31), end_of_support=date(2027, 10, 31), end_of_sw_maint=date(2023, 10, 31),
        replacement_sku="C9200-24P",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3850-12S-E": EOLRecord(
        part_code="WS-C3850-12S-E", vendor="Cisco", model="WS-C3850-12S-E",
        end_of_sale=date(2022, 4, 30), end_of_support=date(2027, 4, 30), end_of_sw_maint=date(2023, 4, 30),
        replacement_sku="C9300-24S",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3650-24PD-E": EOLRecord(
        part_code="WS-C3650-24PD-E", vendor="Cisco", model="WS-C3650-24PD-E",
        end_of_sale=date(2021, 10, 31), end_of_support=date(2026, 10, 31), end_of_sw_maint=date(2022, 10, 31),
        replacement_sku="C9300L-24P-4X-A",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "SF350-24P-K9-EU": EOLRecord(
        part_code="SF350-24P-K9-EU", vendor="Cisco", model="SF350-24P-K9-EU",
        end_of_sale=date(2023, 1, 29), end_of_support=date(2028, 1, 31), end_of_sw_maint=date(2024, 1, 29),
        replacement_sku="CBS350-24P-4G-EU",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960CX-8TC-L": EOLRecord(
        part_code="WS-C2960CX-8TC-L", vendor="Cisco", model="WS-C2960CX-8TC-L",
        end_of_sale=date(2024, 4, 30), end_of_support=date(2029, 4, 30), end_of_sw_maint=date(2025, 4, 30),
        replacement_sku="C9200CX-12T-2X2G-E",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960L-8TS-LL": EOLRecord(
        part_code="WS-C2960L-8TS-LL", vendor="Cisco", model="WS-C2960L-8TS-LL",
        end_of_sale=date(2021, 10, 31), end_of_support=date(2026, 10, 31), end_of_sw_maint=date(2022, 10, 31),
        replacement_sku="C1000-8T-2G-L",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960L-8TS-JP": EOLRecord(
        part_code="WS-C2960L-8TS-JP", vendor="Cisco", model="WS-C2960L-8TS-JP",
        end_of_sale=date(2022, 10, 31), end_of_support=date(2027, 10, 31), end_of_sw_maint=date(2023, 10, 31),
        replacement_sku="C1000-8T-2G-L",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960-8TC-L": EOLRecord(
        part_code="WS-C2960-8TC-L", vendor="Cisco", model="WS-C2960-8TC-L",
        end_of_sale=date(2013, 7, 29), end_of_support=date(2018, 7, 31), end_of_sw_maint=date(2014, 7, 29),
        replacement_sku="WS-C2960C-8TC-L",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO WS-C3560V2-24TS": EOLRecord(
        part_code="Cisco WS-C3560V2-24TS", vendor="Cisco", model="Cisco WS-C3560V2-24TS",
        end_of_sale=date(2016, 5, 14), end_of_support=date(2021, 5, 31), end_of_sw_maint=date(2017, 5, 14),
        replacement_sku="WS-C3650-24TS",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960CG-8TC-L": EOLRecord(
        part_code="WS-C2960CG-8TC-L", vendor="Cisco", model="WS-C2960CG-8TC-L",
        end_of_sale=None, end_of_support=date(2021, 10, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C1000-16T-2G-L": EOLRecord(
        part_code="C1000-16T-2G-L", vendor="Cisco", model="C1000-16T-2G-L",
        end_of_sale=date(2024, 10, 29), end_of_support=date(2029, 10, 31), end_of_sw_maint=date(2025, 10, 29),
        replacement_sku="C1300-16T-2G",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "C9300X-24Y": EOLRecord(
        part_code="C9300X-24Y", vendor="Cisco", model="C9300X-24Y",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CBS350-8T-E-2G-NA": EOLRecord(
        part_code="CBS350-8T-E-2G-NA", vendor="Cisco", model="CBS350-8T-E-2G-NA",
        end_of_sale=date(2024, 10, 29), end_of_support=date(2029, 10, 31), end_of_sw_maint=date(2025, 1, 27),
        replacement_sku="C1300-8T-E-2G",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CBS350-8T-E-2G-AU": EOLRecord(
        part_code="CBS350-8T-E-2G-AU", vendor="Cisco", model="CBS350-8T-E-2G-AU",
        end_of_sale=date(2024, 10, 29), end_of_support=date(2029, 10, 31), end_of_sw_maint=date(2025, 10, 29),
        replacement_sku="C1300-8T-E-2G",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CBS350-8T-E-2G-EU": EOLRecord(
        part_code="CBS350-8T-E-2G-EU", vendor="Cisco", model="CBS350-8T-E-2G-EU",
        end_of_sale=date(2024, 10, 29), end_of_support=date(2029, 10, 31), end_of_sw_maint=date(2025, 10, 29),
        replacement_sku="C1300-8T-E-2G",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CBS350-8T-E-2G-UK": EOLRecord(
        part_code="CBS350-8T-E-2G-UK", vendor="Cisco", model="CBS350-8T-E-2G-UK",
        end_of_sale=date(2024, 10, 29), end_of_support=date(2029, 10, 31), end_of_sw_maint=date(2025, 10, 29),
        replacement_sku="C1300-8T-E-2G",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO CBS 350-8T-E-2G": EOLRecord(
        part_code="CISCO CBS 350-8T-E-2G", vendor="Cisco", model="CISCO CBS 350-8T-E-2G",
        end_of_sale=date(2024, 10, 29), end_of_support=date(2029, 10, 31), end_of_sw_maint=date(2025, 10, 29),
        replacement_sku="C1300-8T-E-2G",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "CBS350-8T-E-2G-BR": EOLRecord(
        part_code="CBS350-8T-E-2G-BR", vendor="Cisco", model="CBS350-8T-E-2G-BR",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960G-24TC-L": EOLRecord(
        part_code="WS-C2960G-24TC-L", vendor="Cisco", model="WS-C2960G-24TC-L",
        end_of_sale=date(2012, 7, 31), end_of_support=date(2017, 7, 31), end_of_sw_maint=date(2015, 7, 31),
        replacement_sku="WS-C2960S-24TS-L",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960L-16TS-LL": EOLRecord(
        part_code="WS-C2960L-16TS-LL", vendor="Cisco", model="WS-C2960L-16TS-LL",
        end_of_sale=date(2021, 10, 31), end_of_support=date(2026, 10, 31), end_of_sw_maint=date(2022, 10, 31),
        replacement_sku="C1000-16T-2G-L",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960-24TC-L": EOLRecord(
        part_code="WS-C2960-24TC-L", vendor="Cisco", model="WS-C2960-24TC-L",
        end_of_sale=date(2022, 10, 31), end_of_support=date(2027, 10, 31), end_of_sw_maint=date(2023, 10, 31),
        replacement_sku="C1000-24T-4G-L",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "MS250-48LP-HW": EOLRecord(
        part_code="MS250-48LP-HW", vendor="Cisco", model="MS250-48LP-HW",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MR53-HW": EOLRecord(
        part_code="MR53-HW", vendor="Cisco", model="MR53-HW",
        end_of_sale=date(2022, 7, 14), end_of_support=date(2026, 7, 21), end_of_sw_maint=None,
        replacement_sku="MR56-HW",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "MS350-24P-HW": EOLRecord(
        part_code="MS350-24P-HW", vendor="Cisco", model="MS350-24P-HW",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "C9200L-48P-4G-E": EOLRecord(
        part_code="C9200L-48P-4G-E", vendor="Cisco", model="C9200L-48P-4G-E",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "C9300-48P-E": EOLRecord(
        part_code="C9300-48P-E", vendor="Cisco", model="C9300-48P-E",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960X-24TS-L": EOLRecord(
        part_code="WS-C2960X-24TS-L", vendor="Cisco", model="WS-C2960X-24TS-L",
        end_of_sale=date(2022, 10, 31), end_of_support=date(2027, 10, 31), end_of_sw_maint=date(2023, 10, 31),
        replacement_sku="C9200L-24T-4G",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3750G-24T-E": EOLRecord(
        part_code="WS-C3750G-24T-E", vendor="Cisco", model="WS-C3750G-24T-E",
        end_of_sale=date(2013, 1, 30), end_of_support=date(2018, 1, 31), end_of_sw_maint=date(2014, 1, 30),
        replacement_sku="WS-C3750X-24T-E",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960S-24TS-L": EOLRecord(
        part_code="WS-C2960S-24TS-L", vendor="Cisco", model="WS-C2960S-24TS-L",
        end_of_sale=date(2015, 11, 6), end_of_support=date(2020, 11, 30), end_of_sw_maint=date(2016, 5, 11),
        replacement_sku="WS-C2960X-24TS-L",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960-24TC-S": EOLRecord(
        part_code="WS-C2960-24TC-S", vendor="Cisco", model="WS-C2960-24TC-S",
        end_of_sale=date(2022, 10, 31), end_of_support=date(2027, 10, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960X-24TS-LL": EOLRecord(
        part_code="WS-C2960X-24TS-LL", vendor="Cisco", model="WS-C2960X-24TS-LL",
        end_of_sale=date(2022, 10, 31), end_of_support=date(2027, 10, 31), end_of_sw_maint=date(2023, 10, 31),
        replacement_sku="C9200L-24T-4G",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MS220-24-HW": EOLRecord(
        part_code="MS220-24-HW", vendor="Cisco", model="MS220-24-HW",
        end_of_sale=date(2017, 7, 29), end_of_support=date(2024, 7, 29), end_of_sw_maint=None,
        replacement_sku="MS120-24-HW",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MS220-24": EOLRecord(
        part_code="MS220-24", vendor="Cisco", model="MS220-24",
        end_of_sale=date(2024, 7, 29), end_of_support=date(2024, 7, 29), end_of_sw_maint=date(2024, 7, 29),
        replacement_sku="MS120-24",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MS120-24P-HW": EOLRecord(
        part_code="MS120-24P-HW", vendor="Cisco", model="MS120-24P-HW",
        end_of_sale=date(2025, 3, 28), end_of_support=date(2030, 3, 28), end_of_sw_maint=None,
        replacement_sku="MS130-24P-HW",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2950-12": EOLRecord(
        part_code="WS-C2950-12", vendor="Cisco", model="WS-C2950-12",
        end_of_sale=date(2008, 10, 21), end_of_support=date(2013, 10, 20), end_of_sw_maint=date(2009, 10, 21),
        replacement_sku="WS-C2960-24-S",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MS 120-24P": EOLRecord(
        part_code="MS 120-24P", vendor="Cisco", model="MS 120-24P",
        end_of_sale=date(2025, 3, 28), end_of_support=date(2030, 3, 28), end_of_sw_maint=None,
        replacement_sku="MS 130-24P",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MS120-24P": EOLRecord(
        part_code="MS120-24P", vendor="Cisco", model="MS120-24P",
        end_of_sale=date(2025, 3, 28), end_of_support=date(2030, 3, 28), end_of_sw_maint=None,
        replacement_sku="MS130-24P",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "MS250-24P-HW": EOLRecord(
        part_code="MS250-24P-HW", vendor="Cisco", model="MS250-24P-HW",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MS120-24-HW": EOLRecord(
        part_code="MS120-24-HW", vendor="Cisco", model="MS120-24-HW",
        end_of_sale=date(2025, 3, 28), end_of_support=date(2030, 3, 28), end_of_sw_maint=None,
        replacement_sku="MS130-24-HW",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "MS210-24P-HW": EOLRecord(
        part_code="MS210-24P-HW", vendor="Cisco", model="MS210-24P-HW",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "MS250-24P": EOLRecord(
        part_code="MS250-24P", vendor="Cisco", model="MS250-24P",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MERAKI": EOLRecord(
        part_code="MERAKI", vendor="Cisco", model="MERAKI",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "MR42-HW": EOLRecord(
        part_code="MR42-HW", vendor="Cisco", model="MR42-HW",
        end_of_sale=date(2022, 7, 14), end_of_support=date(2026, 7, 21), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "MS250-4P": EOLRecord(
        part_code="MS250-4P", vendor="Cisco", model="MS250-4P",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CBS350-8T-E-2G 8-PORT GIGABIT MANAGED SWITCH": EOLRecord(
        part_code="CBS350-8T-E-2G 8-Port Gigabit Managed Switch", vendor="Cisco", model="CBS350-8T-E-2G 8-Port Gigabit Managed Switch",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3650-24TS": EOLRecord(
        part_code="WS-C3650-24TS", vendor="Cisco", model="WS-C3650-24TS",
        end_of_sale=date(2022, 10, 31), end_of_support=date(2027, 10, 31), end_of_sw_maint=date(2023, 10, 31),
        replacement_sku="C9300L-24T-4G",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3850-24T-E": EOLRecord(
        part_code="WS-C3850-24T-E", vendor="Cisco", model="WS-C3850-24T-E",
        end_of_sale=date(2020, 10, 30), end_of_support=date(2025, 10, 31), end_of_sw_maint=date(2021, 10, 30),
        replacement_sku="C9300-24T-A",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3560CX-12PC-S": EOLRecord(
        part_code="WS-C3560CX-12PC-S", vendor="Cisco", model="WS-C3560CX-12PC-S",
        end_of_sale=date(2024, 4, 30), end_of_support=date(2029, 4, 30), end_of_sw_maint=date(2025, 4, 30),
        replacement_sku="C9200CX-12P-2X2G-A",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960X-48FPS-L": EOLRecord(
        part_code="WS-C2960X-48FPS-L", vendor="Cisco", model="WS-C2960X-48FPS-L",
        end_of_sale=date(2022, 10, 31), end_of_support=date(2027, 10, 31), end_of_sw_maint=date(2023, 10, 31),
        replacement_sku="C9200L-48P-4G",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "GLC-LH-SMD": EOLRecord(
        part_code="GLC-LH-SMD", vendor="Cisco", model="GLC-LH-SMD",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960+24LC-L": EOLRecord(
        part_code="WS-C2960+24LC-L", vendor="Cisco", model="WS-C2960+24LC-L",
        end_of_sale=date(2021, 10, 31), end_of_support=date(2026, 10, 31), end_of_sw_maint=date(2022, 10, 31),
        replacement_sku="C1000-24P-4G-L",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2950-24": EOLRecord(
        part_code="WS-C2950-24", vendor="Cisco", model="WS-C2950-24",
        end_of_sale=date(2008, 10, 21), end_of_support=date(2013, 10, 20), end_of_sw_maint=date(2009, 10, 21),
        replacement_sku="WS-C2960-24-S",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960C-8TC-S": EOLRecord(
        part_code="WS-C2960C-8TC-S", vendor="Cisco", model="WS-C2960C-8TC-S",
        end_of_sale=date(2020, 10, 30), end_of_support=date(2025, 10, 31), end_of_sw_maint=date(2021, 10, 30),
        replacement_sku="WS-C2960C-8TC-S",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3750G-48PS-E": EOLRecord(
        part_code="WS-C3750G-48PS-E", vendor="Cisco", model="WS-C3750G-48PS-E",
        end_of_sale=date(2013, 1, 30), end_of_support=date(2018, 1, 31), end_of_sw_maint=date(2014, 1, 30),
        replacement_sku="WS-C3750X-48P-E",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3750-48PS-S": EOLRecord(
        part_code="WS-C3750-48PS-S", vendor="Cisco", model="WS-C3750-48PS-S",
        end_of_sale=date(2010, 7, 5), end_of_support=date(2015, 7, 31), end_of_sw_maint=date(2013, 4, 7),
        replacement_sku="WS-C3750V2-48PS-S",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C4948": EOLRecord(
        part_code="WS-C4948", vendor="Cisco", model="WS-C4948",
        end_of_sale=date(2013, 8, 1), end_of_support=date(2018, 7, 31), end_of_sw_maint=date(2014, 1, 8),
        replacement_sku="WS-C4948",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2924-XL-EN": EOLRecord(
        part_code="WS-C2924-XL-EN", vendor="Cisco", model="WS-C2924-XL-EN",
        end_of_sale=date(2001, 11, 1), end_of_support=date(2006, 11, 1), end_of_sw_maint=None,
        replacement_sku="WS-C2950-24",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2924C-XL-EN": EOLRecord(
        part_code="WS-C2924C-XL-EN", vendor="Cisco", model="WS-C2924C-XL-EN",
        end_of_sale=None, end_of_support=date(2006, 1, 11), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2950T-24": EOLRecord(
        part_code="WS-C2950T-24", vendor="Cisco", model="WS-C2950T-24",
        end_of_sale=None, end_of_support=date(2011, 12, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3750-24TS-S": EOLRecord(
        part_code="WS-C3750-24TS-S", vendor="Cisco", model="WS-C3750-24TS-S",
        end_of_sale=date(2010, 7, 5), end_of_support=date(2015, 7, 31), end_of_sw_maint=date(2013, 4, 7),
        replacement_sku="WS-C3750V2-24TS-S",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3524-PWR-XL-EN": EOLRecord(
        part_code="WS-C3524-PWR-XL-EN", vendor="Cisco", model="WS-C3524-PWR-XL-EN",
        end_of_sale=None, end_of_support=date(2008, 12, 8), end_of_sw_maint=None,
        replacement_sku="WS-C3550-24PWR-SMI",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "WS-X4012": EOLRecord(
        part_code="WS-X4012", vendor="Cisco", model="WS-X4012",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "WS-C2950G-24-EI": EOLRecord(
        part_code="WS-C2950G-24-EI", vendor="Cisco", model="WS-C2950G-24-EI",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "WS-C2980": EOLRecord(
        part_code="WS-C2980", vendor="Cisco", model="WS-C2980",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-X6K-SUP1A-MSFC": EOLRecord(
        part_code="WS-X6K-SUP1A-MSFC", vendor="Cisco", model="WS-X6K-SUP1A-MSFC",
        end_of_sale=date(2002, 2, 28), end_of_support=date(2007, 2, 28), end_of_sw_maint=None,
        replacement_sku="WS-X6K-S1A-MSFC2",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-X6K-S1A-MSFC/2": EOLRecord(
        part_code="WS-X6K-S1A-MSFC/2", vendor="Cisco", model="WS-X6K-S1A-MSFC/2",
        end_of_sale=date(2002, 2, 28), end_of_support=date(2007, 2, 28), end_of_sw_maint=None,
        replacement_sku="MSFC2,",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "WS-F6K-PFC2": EOLRecord(
        part_code="WS-F6K-PFC2", vendor="Cisco", model="WS-F6K-PFC2",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-X6348-RJ-45=": EOLRecord(
        part_code="WS-X6348-RJ-45=", vendor="Cisco", model="WS-X6348-RJ-45=",
        end_of_sale=date(2006, 1, 13), end_of_support=date(2011, 1, 31), end_of_sw_maint=date(2007, 1, 13),
        replacement_sku="WS-X6148-RJ-45=",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-X6416-GBIC=": EOLRecord(
        part_code="WS-X6416-GBIC=", vendor="Cisco", model="WS-X6416-GBIC=",
        end_of_sale=date(2006, 1, 13), end_of_support=date(2011, 1, 31), end_of_sw_maint=date(2007, 1, 13),
        replacement_sku="WS-X6516A-GBIC=",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-X6348-RJ45V=": EOLRecord(
        part_code="WS-X6348-RJ45V=", vendor="Cisco", model="WS-X6348-RJ45V=",
        end_of_sale=date(2006, 1, 13), end_of_support=date(2011, 1, 31), end_of_sw_maint=date(2007, 1, 13),
        replacement_sku="Cisco Catalyst 650010/100 Line Cards",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-CAC-1300W": EOLRecord(
        part_code="WS-CAC-1300W", vendor="Cisco", model="WS-CAC-1300W",
        end_of_sale=date(2004, 5, 31), end_of_support=date(2009, 5, 31), end_of_sw_maint=date(2005, 5, 31),
        replacement_sku="WS-CAC-3000W",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-X6408A-GBIC=": EOLRecord(
        part_code="WS-X6408A-GBIC=", vendor="Cisco", model="WS-X6408A-GBIC=",
        end_of_sale=date(2009, 5, 18), end_of_support=date(2014, 5, 31), end_of_sw_maint=date(2010, 5, 18),
        replacement_sku="WS-X6408A-GBIC=",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "WS-F6K-MSFC2=": EOLRecord(
        part_code="WS-F6K-MSFC2=", vendor="Cisco", model="WS-F6K-MSFC2=",
        end_of_sale=date(2007, 3, 1), end_of_support=date(2012, 2, 28), end_of_sw_maint=date(2008, 2, 29),
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-CAC-1300W=": EOLRecord(
        part_code="WS-CAC-1300W=", vendor="Cisco", model="WS-CAC-1300W=",
        end_of_sale=date(2004, 12, 31), end_of_support=date(2009, 12, 31), end_of_sw_maint=None,
        replacement_sku="WS-CAC-3000W(=)",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3650-48TQ-L": EOLRecord(
        part_code="WS-C3650-48TQ-L", vendor="Cisco", model="WS-C3650-48TQ-L",
        end_of_sale=date(2021, 10, 31), end_of_support=date(2026, 10, 31), end_of_sw_maint=date(2022, 10, 31),
        replacement_sku="C9300L-48T-4X-E",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C6509-1300AC=": EOLRecord(
        part_code="WS-C6509-1300AC=", vendor="Cisco", model="WS-C6509-1300AC=",
        end_of_sale=date(2020, 10, 30), end_of_support=date(2025, 10, 31), end_of_sw_maint=date(2021, 10, 30),
        replacement_sku="no replacement available",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C4500X-16SFP+": EOLRecord(
        part_code="WS-C4500X-16SFP+", vendor="Cisco", model="WS-C4500X-16SFP+",
        end_of_sale=date(2020, 10, 30), end_of_support=date(2025, 10, 31), end_of_sw_maint=date(2021, 10, 30),
        replacement_sku="C9500-16X",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3550-24-SMI": EOLRecord(
        part_code="WS-C3550-24-SMI", vendor="Cisco", model="WS-C3550-24-SMI",
        end_of_sale=date(2006, 5, 2), end_of_support=date(2011, 5, 2), end_of_sw_maint=date(2007, 2, 5),
        replacement_sku="WS-C3750-24TS-S WS-C3560-24TS-S",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2950G-48-EI": EOLRecord(
        part_code="WS-C2950G-48-EI", vendor="Cisco", model="WS-C2950G-48-EI",
        end_of_sale=None, end_of_support=date(2011, 12, 31), end_of_sw_maint=None,
        replacement_sku="2960-X series",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3750-24PS-E": EOLRecord(
        part_code="WS-C3750-24PS-E", vendor="Cisco", model="WS-C3750-24PS-E",
        end_of_sale=date(2010, 7, 5), end_of_support=date(2015, 7, 31), end_of_sw_maint=date(2013, 4, 7),
        replacement_sku="WS-C3750-24PS-E",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3560-24PS-S": EOLRecord(
        part_code="WS-C3560-24PS-S", vendor="Cisco", model="WS-C3560-24PS-S",
        end_of_sale=date(2010, 7, 5), end_of_support=date(2015, 7, 31), end_of_sw_maint=date(2013, 4, 7),
        replacement_sku="WS-C3560V2-24PS-S",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "AIR-CT5508-K9": EOLRecord(
        part_code="AIR-CT5508-K9", vendor="Cisco", model="AIR-CT5508-K9",
        end_of_sale=date(2018, 5, 4), end_of_support=date(2023, 7, 31), end_of_sw_maint=date(2019, 1, 8),
        replacement_sku="Cisco 5520 Wireless Controller.",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C4507R+E": EOLRecord(
        part_code="WS-C4507R+E", vendor="Cisco", model="WS-C4507R+E",
        end_of_sale=date(2020, 10, 30), end_of_support=date(2025, 10, 31), end_of_sw_maint=date(2021, 10, 30),
        replacement_sku="C9407R",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3750-24PS-S": EOLRecord(
        part_code="WS-C3750-24PS-S", vendor="Cisco", model="WS-C3750-24PS-S",
        end_of_sale=date(2010, 7, 5), end_of_support=date(2015, 7, 31), end_of_sw_maint=date(2013, 4, 7),
        replacement_sku="WS-C3750V2-24PS-S",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3560-48PS-S": EOLRecord(
        part_code="WS-C3560-48PS-S", vendor="Cisco", model="WS-C3560-48PS-S",
        end_of_sale=date(2010, 7, 5), end_of_support=date(2015, 7, 31), end_of_sw_maint=date(2013, 4, 7),
        replacement_sku="WS-C3560V2-48PS-S",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960-48TT-L": EOLRecord(
        part_code="WS-C2960-48TT-L", vendor="Cisco", model="WS-C2960-48TT-L",
        end_of_sale=date(2014, 10, 31), end_of_support=date(2019, 10, 31), end_of_sw_maint=date(2015, 10, 31),
        replacement_sku="WS-C2960+48TC-L",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2912-XL-EN": EOLRecord(
        part_code="WS-C2912-XL-EN", vendor="Cisco", model="WS-C2912-XL-EN",
        end_of_sale=None, end_of_support=date(2006, 1, 11), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3560G-24TS-S": EOLRecord(
        part_code="WS-C3560G-24TS-S", vendor="Cisco", model="WS-C3560G-24TS-S",
        end_of_sale=date(2013, 1, 30), end_of_support=date(2018, 1, 31), end_of_sw_maint=date(2014, 1, 30),
        replacement_sku="WS-C3560X-24T-S",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3560V2-48TS-S": EOLRecord(
        part_code="WS-C3560V2-48TS-S", vendor="Cisco", model="WS-C3560V2-48TS-S",
        end_of_sale=date(2016, 5, 14), end_of_support=date(2021, 5, 31), end_of_sw_maint=date(2017, 5, 14),
        replacement_sku="WS-C3650-48TS-S",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960-48TC-L": EOLRecord(
        part_code="WS-C2960-48TC-L", vendor="Cisco", model="WS-C2960-48TC-L",
        end_of_sale=date(2014, 10, 31), end_of_support=date(2019, 10, 31), end_of_sw_maint=date(2015, 10, 31),
        replacement_sku="WS-C2960+48TC-L",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2948G": EOLRecord(
        part_code="WS-C2948G", vendor="Cisco", model="WS-C2948G",
        end_of_sale=None, end_of_support=date(2009, 11, 3), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2950G-12-EI": EOLRecord(
        part_code="WS-C2950G-12-EI", vendor="Cisco", model="WS-C2950G-12-EI",
        end_of_sale=date(2006, 12, 31), end_of_support=date(2011, 12, 30), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3750-48TS-E": EOLRecord(
        part_code="WS-C3750-48TS-E", vendor="Cisco", model="WS-C3750-48TS-E",
        end_of_sale=date(2010, 7, 5), end_of_support=date(2015, 7, 31), end_of_sw_maint=date(2013, 4, 7),
        replacement_sku="WS-C3750V2-48TS-E",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3560-48PS-E": EOLRecord(
        part_code="WS-C3560-48PS-E", vendor="Cisco", model="WS-C3560-48PS-E",
        end_of_sale=date(2010, 7, 5), end_of_support=date(2015, 7, 31), end_of_sw_maint=date(2013, 4, 7),
        replacement_sku="WS-C3560V2-48PS-E",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C4506": EOLRecord(
        part_code="WS-C4506", vendor="Cisco", model="WS-C4506",
        end_of_sale=None, end_of_support=date(2025, 10, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2924-XL-EN-BU": EOLRecord(
        part_code="WS-C2924-XL-EN-BU", vendor="Cisco", model="WS-C2924-XL-EN-BU",
        end_of_sale=date(2001, 11, 1), end_of_support=date(2006, 11, 1), end_of_sw_maint=None,
        replacement_sku="WS-C2950-24",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2950-24-BU": EOLRecord(
        part_code="WS-C2950-24-BU", vendor="Cisco", model="WS-C2950-24-BU",
        end_of_sale=None, end_of_support=date(2013, 10, 20), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3560X-48PF-S": EOLRecord(
        part_code="WS-C3560X-48PF-S", vendor="Cisco", model="WS-C3560X-48PF-S",
        end_of_sale=date(2016, 10, 30), end_of_support=date(2021, 10, 31), end_of_sw_maint=date(2017, 10, 30),
        replacement_sku="WS-C3650-48FD-S",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3550-48-SMI": EOLRecord(
        part_code="WS-C3550-48-SMI", vendor="Cisco", model="WS-C3550-48-SMI",
        end_of_sale=date(2006, 5, 2), end_of_support=date(2011, 5, 2), end_of_sw_maint=date(2007, 2, 5),
        replacement_sku="WS-C3750-48TS-S WS-C3560-48TS-S",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "C9300X-12Y": EOLRecord(
        part_code="C9300X-12Y", vendor="Cisco", model="C9300X-12Y",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "C9200L-24T-4X": EOLRecord(
        part_code="C9200L-24T-4X", vendor="Cisco", model="C9200L-24T-4X",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960C-8TC-L": EOLRecord(
        part_code="WS-C2960C-8TC-L", vendor="Cisco", model="WS-C2960C-8TC-L",
        end_of_sale=date(2020, 10, 30), end_of_support=date(2025, 10, 31), end_of_sw_maint=date(2021, 10, 30),
        replacement_sku="WS-C2960CX-8TC-L",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "C1000-24T-4X-L": EOLRecord(
        part_code="C1000-24T-4X-L", vendor="Cisco", model="C1000-24T-4X-L",
        end_of_sale=date(2025, 4, 30), end_of_support=date(2030, 4, 30), end_of_sw_maint=date(2026, 4, 30),
        replacement_sku="C1300-24T-4X",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "CISCO WS-C2960XR-24TS-I": EOLRecord(
        part_code="Cisco WS-C2960XR-24TS-I", vendor="Cisco", model="Cisco WS-C2960XR-24TS-I",
        end_of_sale=date(2022, 10, 31), end_of_support=date(2027, 10, 31), end_of_sw_maint=date(2023, 10, 31),
        replacement_sku="C9200-24T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960XR-24TD-I": EOLRecord(
        part_code="WS-C2960XR-24TD-I", vendor="Cisco", model="WS-C2960XR-24TD-I",
        end_of_sale=date(2022, 10, 31), end_of_support=date(2027, 10, 31), end_of_sw_maint=date(2023, 10, 31),
        replacement_sku="C9200-24T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3850-24XS-S": EOLRecord(
        part_code="WS-C3850-24XS-S", vendor="Cisco", model="WS-C3850-24XS-S",
        end_of_sale=date(2022, 4, 30), end_of_support=date(2027, 4, 30), end_of_sw_maint=date(2023, 4, 30),
        replacement_sku="C9300X-24Y",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960XR-24TS-I": EOLRecord(
        part_code="WS-C2960XR-24TS-I", vendor="Cisco", model="WS-C2960XR-24TS-I",
        end_of_sale=date(2022, 10, 31), end_of_support=date(2027, 10, 31), end_of_sw_maint=date(2023, 10, 31),
        replacement_sku="C9200-24T",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "C9200L-24T-4X-E": EOLRecord(
        part_code="C9200L-24T-4X-E", vendor="Cisco", model="C9200L-24T-4X-E",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data not found
    "CBS350-8T-E-2G-IN": EOLRecord(
        part_code="CBS350-8T-E-2G-IN", vendor="Cisco", model="CBS350-8T-E-2G-IN",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="none",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "FSP150CC-GE112": EOLRecord(
        part_code="FSP150CC-GE112", vendor="Cisco", model="FSP150CC-GE112",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "C9200L-24T-4G-E": EOLRecord(
        part_code="C9200L-24T-4G-E", vendor="Cisco", model="C9200L-24T-4G-E",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "ME-3600X-24TS-M=": EOLRecord(
        part_code="ME-3600X-24TS-M=", vendor="Cisco", model="ME-3600X-24TS-M=",
        end_of_sale=date(2017, 10, 15), end_of_support=date(2022, 10, 31), end_of_sw_maint=None,
        replacement_sku="",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Date not published
    "2948": EOLRecord(
        part_code="2948", vendor="Cisco", model="2948",
        end_of_sale=None, end_of_support=None, end_of_sw_maint=None,
        replacement_sku="",
        confidence="low",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C2960-24TT-L": EOLRecord(
        part_code="WS-C2960-24TT-L", vendor="Cisco", model="WS-C2960-24TT-L",
        end_of_sale=date(2014, 10, 31), end_of_support=date(2019, 10, 31), end_of_sw_maint=date(2015, 10, 31),
        replacement_sku="WS-C2960+24TC-L",
        confidence="high",
        source_url="master_assest_data.xlsx"),
    # Data found
    "WS-C3750X-24T-E": EOLRecord(
        part_code="WS-C3750X-24T-E", vendor="Cisco", model="WS-C3750X-24T-E",
        end_of_sale=date(2016, 10, 30), end_of_support=date(2021, 10, 31), end_of_sw_maint=date(2017, 10, 30),
        replacement_sku="WS-C3850-24T-E",
        confidence="high",
        source_url="master_assest_data.xlsx"),
}


def lookup_master(part_code: str):
    """Exact match then normalised prefix match against MASTER_EOL_DB."""
    key = part_code.strip().upper()
    if key in MASTER_EOL_DB:
        return MASTER_EOL_DB[key]
    # Normalise common variants: strip spaces, dashes
    key_norm = key.replace(" ", "").replace("-", "")
    for k, v in MASTER_EOL_DB.items():
        k_norm = k.replace(" ", "").replace("-", "")
        if key_norm == k_norm:
            return v
    # Prefix match
    for k, v in MASTER_EOL_DB.items():
        if key.startswith(k) or k.startswith(key):
            return v
    return None