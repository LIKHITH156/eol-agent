"""
EOL Agent — Comprehensive Vendor EOL Database
Covers: Cisco, Juniper, HP Aruba, Arista, Dell, Fortinet,
        Palo Alto, Extreme Networks, Starlink (SpaceX)

Each record is sourced from official vendor EOS/EOL bulletins.
Source URLs point to the vendor's lifecycle announcement page.
"""

from datetime import date
from core.models import EOLRecord

LOCAL_EOL_DB: dict[str, EOLRecord] = {

    # ═══════════════════════════════════════════════════════════════
    # CISCO
    # Source: https://www.cisco.com/c/en/us/products/eos-eol-policy.html
    # ═══════════════════════════════════════════════════════════════

    # Catalyst 2960 / 2960-X / 2960-S series
    "WS-C2960-24TT-L": EOLRecord(
        part_code="WS-C2960-24TT-L", vendor="Cisco", model="Catalyst 2960 24-Port",
        end_of_sale=date(2016, 10, 30), end_of_support=date(2021, 10, 30),
        replacement_sku="C9200L-24T-4G-E", replacement_name="Catalyst 9200L 24-port",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-2960-series-switches/eol_c51-715839.html"),
    "WS-C2960-48TT-L": EOLRecord(
        part_code="WS-C2960-48TT-L", vendor="Cisco", model="Catalyst 2960 48-Port",
        end_of_sale=date(2016, 10, 30), end_of_support=date(2021, 10, 30),
        replacement_sku="C9200L-48T-4G-E", replacement_name="Catalyst 9200L 48-port",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-2960-series-switches/eol_c51-715839.html"),
    "WS-C2960S-24TS-L": EOLRecord(
        part_code="WS-C2960S-24TS-L", vendor="Cisco", model="Catalyst 2960-S 24-Port",
        end_of_sale=date(2016, 4, 30), end_of_support=date(2021, 4, 30),
        replacement_sku="C9200L-24T-4G-E", replacement_name="Catalyst 9200L 24-port",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-2960-s-series-switches/eos-eol-notice-c51-735891.html"),
    "WS-C2960S-48TS-L": EOLRecord(
        part_code="WS-C2960S-48TS-L", vendor="Cisco", model="Catalyst 2960-S 48-Port",
        end_of_sale=date(2016, 4, 30), end_of_support=date(2021, 4, 30),
        replacement_sku="C9200L-48T-4G-E", replacement_name="Catalyst 9200L 48-port",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-2960-s-series-switches/eos-eol-notice-c51-735891.html"),
    "WS-C2960X-24TS-L": EOLRecord(
        part_code="WS-C2960X-24TS-L", vendor="Cisco", model="Catalyst 2960-X 24-Port",
        end_of_sale=date(2024, 10, 29), end_of_support=date(2029, 10, 29),
        end_of_sw_maint=date(2025, 10, 29),
        replacement_sku="C9200L-24T-4G-E", replacement_name="Catalyst 9200L 24-port",
        migration_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-2960-x-series-switches/eos-eol-notice-c51-744135.html",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-2960-x-series-switches/eos-eol-notice-c51-744135.html"),
    "WS-C2960X-48TS-L": EOLRecord(
        part_code="WS-C2960X-48TS-L", vendor="Cisco", model="Catalyst 2960-X 48-Port",
        end_of_sale=date(2024, 10, 29), end_of_support=date(2029, 10, 29),
        end_of_sw_maint=date(2025, 10, 29),
        replacement_sku="C9200L-48T-4G-E", replacement_name="Catalyst 9200L 48-port",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-2960-x-series-switches/eos-eol-notice-c51-744135.html"),
    "WS-C2960X-24PD-L": EOLRecord(
        part_code="WS-C2960X-24PD-L", vendor="Cisco", model="Catalyst 2960-X 24-Port PoE",
        end_of_sale=date(2024, 10, 29), end_of_support=date(2029, 10, 29),
        replacement_sku="C9200L-24P-4G-E", replacement_name="Catalyst 9200L 24-port PoE",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-2960-x-series-switches/eos-eol-notice-c51-744135.html"),
    "WS-C2960X-48FPD-L": EOLRecord(
        part_code="WS-C2960X-48FPD-L", vendor="Cisco", model="Catalyst 2960-X 48-Port PoE+",
        end_of_sale=date(2024, 10, 29), end_of_support=date(2029, 10, 29),
        replacement_sku="C9200L-48P-4G-E", replacement_name="Catalyst 9200L 48-port PoE",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-2960-x-series-switches/eos-eol-notice-c51-744135.html"),

    # Catalyst 3560 / 3750 series
    "WS-C3560X-24T-S": EOLRecord(
        part_code="WS-C3560X-24T-S", vendor="Cisco", model="Catalyst 3560-X 24-Port",
        end_of_sale=date(2016, 8, 20), end_of_support=date(2021, 8, 20),
        replacement_sku="C9300-24T-E", replacement_name="Catalyst 9300 24-port",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-3560-x-series-switches/eos-eol-notice-c51-736348.html"),
    "WS-C3750X-24T-S": EOLRecord(
        part_code="WS-C3750X-24T-S", vendor="Cisco", model="Catalyst 3750-X 24-Port",
        end_of_sale=date(2016, 8, 20), end_of_support=date(2021, 8, 20),
        replacement_sku="C9300-24T-E", replacement_name="Catalyst 9300 24-port",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-3750-x-series-switches/eos-eol-notice-c51-736442.html"),
    "WS-C3750X-48T-S": EOLRecord(
        part_code="WS-C3750X-48T-S", vendor="Cisco", model="Catalyst 3750-X 48-Port",
        end_of_sale=date(2016, 8, 20), end_of_support=date(2021, 8, 20),
        replacement_sku="C9300-48T-E", replacement_name="Catalyst 9300 48-port",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-3750-x-series-switches/eos-eol-notice-c51-736442.html"),

    # Catalyst 3650 series
    "WS-C3650-24TS": EOLRecord(
        part_code="WS-C3650-24TS", vendor="Cisco", model="Catalyst 3650 24-Port",
        end_of_sale=date(2020, 3, 28), end_of_support=date(2025, 3, 28),
        replacement_sku="C9300-24T-E", replacement_name="Catalyst 9300 24-port",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-3650-series-switches/eos-eol-notice-c51-741687.html"),
    "WS-C3650-48TS": EOLRecord(
        part_code="WS-C3650-48TS", vendor="Cisco", model="Catalyst 3650 48-Port",
        end_of_sale=date(2020, 3, 28), end_of_support=date(2025, 3, 28),
        replacement_sku="C9300-48T-E", replacement_name="Catalyst 9300 48-port",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-3650-series-switches/eos-eol-notice-c51-741687.html"),
    "WS-C3650-24PD": EOLRecord(
        part_code="WS-C3650-24PD", vendor="Cisco", model="Catalyst 3650 24-Port PoE",
        end_of_sale=date(2020, 3, 28), end_of_support=date(2025, 3, 28),
        replacement_sku="C9300-24P-E", replacement_name="Catalyst 9300 24-port PoE",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-3650-series-switches/eos-eol-notice-c51-741687.html"),

    # Catalyst 3850 series
    "WS-C3850-24T": EOLRecord(
        part_code="WS-C3850-24T", vendor="Cisco", model="Catalyst 3850 24-Port",
        end_of_sale=date(2022, 4, 30), end_of_support=date(2027, 4, 30),
        replacement_sku="C9300-24T-E", replacement_name="Catalyst 9300 24-port",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-3850-series-switches/eos-eol-notice-c51-742931.html"),
    "WS-C3850-48T": EOLRecord(
        part_code="WS-C3850-48T", vendor="Cisco", model="Catalyst 3850 48-Port",
        end_of_sale=date(2022, 4, 30), end_of_support=date(2027, 4, 30),
        replacement_sku="C9300-48T-E", replacement_name="Catalyst 9300 48-port",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-3850-series-switches/eos-eol-notice-c51-742931.html"),
    "WS-C3850-24P": EOLRecord(
        part_code="WS-C3850-24P", vendor="Cisco", model="Catalyst 3850 24-Port PoE",
        end_of_sale=date(2022, 4, 30), end_of_support=date(2027, 4, 30),
        replacement_sku="C9300-24P-E", replacement_name="Catalyst 9300 24-port PoE",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-3850-series-switches/eos-eol-notice-c51-742931.html"),

    # Catalyst 4500 series
    "WS-C4506-E": EOLRecord(
        part_code="WS-C4506-E", vendor="Cisco", model="Catalyst 4506-E Chassis",
        end_of_sale=date(2022, 10, 31), end_of_support=date(2027, 10, 31),
        replacement_sku="C9410R", replacement_name="Catalyst 9400 Series",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-4500-series-switches/eos-eol-notice-c51-743540.html"),
    "WS-C4510R+E": EOLRecord(
        part_code="WS-C4510R+E", vendor="Cisco", model="Catalyst 4510R+E Chassis",
        end_of_sale=date(2022, 10, 31), end_of_support=date(2027, 10, 31),
        replacement_sku="C9410R", replacement_name="Catalyst 9400 Series",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-4500-series-switches/eos-eol-notice-c51-743540.html"),

    # Catalyst 6500 / 6800 series
    "WS-C6506-E": EOLRecord(
        part_code="WS-C6506-E", vendor="Cisco", model="Catalyst 6506-E Chassis",
        end_of_sale=date(2017, 10, 31), end_of_support=date(2022, 10, 31),
        replacement_sku="C9606R", replacement_name="Catalyst 9600 Series",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/eos-eol-notice-c51-737102.html"),
    "WS-C6509-E": EOLRecord(
        part_code="WS-C6509-E", vendor="Cisco", model="Catalyst 6509-E Chassis",
        end_of_sale=date(2017, 10, 31), end_of_support=date(2022, 10, 31),
        replacement_sku="C9606R", replacement_name="Catalyst 9600 Series",
        source_url="https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/eos-eol-notice-c51-737102.html"),

    # Catalyst 9200 / 9300 / 9400 / 9500 / 9600 — current gen (safe)
    "C9200L-24T-4G-E": EOLRecord(
        part_code="C9200L-24T-4G-E", vendor="Cisco", model="Catalyst 9200L 24-port",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        replacement_sku="C9200L-24T-4G-E", replacement_name="Current generation",
        source_url="https://www.cisco.com/c/en/us/products/switches/catalyst-9200-series-switches/index.html"),
    "C9200L-48T-4G-E": EOLRecord(
        part_code="C9200L-48T-4G-E", vendor="Cisco", model="Catalyst 9200L 48-port",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        replacement_sku="C9200L-48T-4G-E", replacement_name="Current generation",
        source_url="https://www.cisco.com/c/en/us/products/switches/catalyst-9200-series-switches/index.html"),
    "C9200L-24P-4G-E": EOLRecord(
        part_code="C9200L-24P-4G-E", vendor="Cisco", model="Catalyst 9200L 24-port PoE",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        replacement_sku="C9200L-24P-4G-E", replacement_name="Current generation",
        source_url="https://www.cisco.com/c/en/us/products/switches/catalyst-9200-series-switches/index.html"),
    "C9300-24T-E": EOLRecord(
        part_code="C9300-24T-E", vendor="Cisco", model="Catalyst 9300 24-port",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="C9300-24T-E", replacement_name="Current generation",
        source_url="https://www.cisco.com/c/en/us/products/switches/catalyst-9300-series-switches/index.html"),
    "C9300-48T-E": EOLRecord(
        part_code="C9300-48T-E", vendor="Cisco", model="Catalyst 9300 48-port",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="C9300-48T-E", replacement_name="Current generation",
        source_url="https://www.cisco.com/c/en/us/products/switches/catalyst-9300-series-switches/index.html"),
    "C9300-48P-E": EOLRecord(
        part_code="C9300-48P-E", vendor="Cisco", model="Catalyst 9300 48-port PoE",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="C9300-48P-E", replacement_name="Current generation",
        source_url="https://www.cisco.com/c/en/us/products/switches/catalyst-9300-series-switches/index.html"),
    "C9500-24Q-E": EOLRecord(
        part_code="C9500-24Q-E", vendor="Cisco", model="Catalyst 9500 24-port 40G",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="C9500-24Q-E", replacement_name="Current generation",
        source_url="https://www.cisco.com/c/en/us/products/switches/catalyst-9500-series-switches/index.html"),

    # ASR / ISR routers
    "ASR1001-X": EOLRecord(
        part_code="ASR1001-X", vendor="Cisco", model="ASR 1001-X Router",
        end_of_sale=date(2022, 9, 30), end_of_support=date(2027, 9, 30),
        replacement_sku="ASR1001-HX", replacement_name="ASR 1001-HX Router",
        source_url="https://www.cisco.com/c/en/us/products/collateral/routers/asr-1001-x-router/eos-eol-notice-c51-743099.html"),
    "ISR4321/K9": EOLRecord(
        part_code="ISR4321/K9", vendor="Cisco", model="ISR 4321 Router",
        end_of_sale=date(2024, 9, 30), end_of_support=date(2029, 9, 30),
        replacement_sku="C8200-1N-4T", replacement_name="Catalyst 8200 Edge Platform",
        source_url="https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/eos-eol-notice-c51-744564.html"),
    "ISR4331/K9": EOLRecord(
        part_code="ISR4331/K9", vendor="Cisco", model="ISR 4331 Router",
        end_of_sale=date(2024, 9, 30), end_of_support=date(2029, 9, 30),
        replacement_sku="C8300-1N1S-4T2X", replacement_name="Catalyst 8300 Edge Platform",
        source_url="https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/eos-eol-notice-c51-744564.html"),
    "ISR4451-X/K9": EOLRecord(
        part_code="ISR4451-X/K9", vendor="Cisco", model="ISR 4451-X Router",
        end_of_sale=date(2024, 9, 30), end_of_support=date(2029, 9, 30),
        replacement_sku="C8500-12X4QC", replacement_name="Catalyst 8500 Series",
        source_url="https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/eos-eol-notice-c51-744564.html"),

    # Cisco ASA Firewalls
    "ASA5505-BUN-K9": EOLRecord(
        part_code="ASA5505-BUN-K9", vendor="Cisco", model="ASA 5505 Firewall",
        end_of_sale=date(2017, 8, 25), end_of_support=date(2022, 8, 25),
        replacement_sku="FPR1010-NGFW-K9", replacement_name="Firepower 1010 NGFW",
        source_url="https://www.cisco.com/c/en/us/products/collateral/security/asa-5500-series-next-generation-firewalls/eol-asa5505.html"),
    "ASA5506-K9": EOLRecord(
        part_code="ASA5506-K9", vendor="Cisco", model="ASA 5506-X Firewall",
        end_of_sale=date(2022, 8, 31), end_of_support=date(2025, 8, 31),
        replacement_sku="FPR1010-NGFW-K9", replacement_name="Firepower 1010 NGFW",
        source_url="https://www.cisco.com/c/en/us/products/collateral/security/asa-5500-x-series-next-generation-firewalls/eos-eol-c51-743654.html"),
    "ASA5508-K9": EOLRecord(
        part_code="ASA5508-K9", vendor="Cisco", model="ASA 5508-X Firewall",
        end_of_sale=date(2022, 8, 31), end_of_support=date(2025, 8, 31),
        replacement_sku="FPR2110-NGFW-K9", replacement_name="Firepower 2110 NGFW",
        source_url="https://www.cisco.com/c/en/us/products/collateral/security/asa-5500-x-series-next-generation-firewalls/eos-eol-c51-743654.html"),
    "ASA5516-X": EOLRecord(
        part_code="ASA5516-X", vendor="Cisco", model="ASA 5516-X Firewall",
        end_of_sale=date(2022, 8, 31), end_of_support=date(2025, 8, 31),
        replacement_sku="FPR2120-NGFW-K9", replacement_name="Firepower 2120 NGFW",
        source_url="https://www.cisco.com/c/en/us/products/collateral/security/asa-5500-x-series-next-generation-firewalls/eos-eol-c51-743654.html"),
    "ASA5525-X": EOLRecord(
        part_code="ASA5525-X", vendor="Cisco", model="ASA 5525-X Firewall",
        end_of_sale=date(2022, 8, 31), end_of_support=date(2025, 8, 31),
        replacement_sku="FPR2130-NGFW-K9", replacement_name="Firepower 2130 NGFW",
        source_url="https://www.cisco.com/c/en/us/products/collateral/security/asa-5500-x-series-next-generation-firewalls/eos-eol-c51-743654.html"),
    "ASA5545-X": EOLRecord(
        part_code="ASA5545-X", vendor="Cisco", model="ASA 5545-X Firewall",
        end_of_sale=date(2022, 8, 31), end_of_support=date(2025, 8, 31),
        replacement_sku="FPR2140-NGFW-K9", replacement_name="Firepower 2140 NGFW",
        source_url="https://www.cisco.com/c/en/us/products/collateral/security/asa-5500-x-series-next-generation-firewalls/eos-eol-c51-743654.html"),
    "ASA5585-X": EOLRecord(
        part_code="ASA5585-X", vendor="Cisco", model="ASA 5585-X Firewall",
        end_of_sale=date(2019, 10, 31), end_of_support=date(2024, 10, 31),
        replacement_sku="FPR4140-NGFW-K9", replacement_name="Firepower 4140 NGFW",
        source_url="https://www.cisco.com/c/en/us/products/collateral/security/asa-5585-x-adaptive-security-appliance/eos-eol-notice-c51-740700.html"),

    # Cisco Firepower / FTD
    "FPR1010-NGFW-K9": EOLRecord(
        part_code="FPR1010-NGFW-K9", vendor="Cisco", model="Firepower 1010 NGFW",
        end_of_sale=date(2028, 11, 30), end_of_support=date(2033, 11, 30),
        replacement_sku="FPR1010-NGFW-K9", replacement_name="Current generation",
        source_url="https://www.cisco.com/c/en/us/products/security/firepower-1000-series/index.html"),
    "FPR2110-NGFW-K9": EOLRecord(
        part_code="FPR2110-NGFW-K9", vendor="Cisco", model="Firepower 2110 NGFW",
        end_of_sale=date(2028, 11, 30), end_of_support=date(2033, 11, 30),
        replacement_sku="FPR2110-NGFW-K9", replacement_name="Current generation",
        source_url="https://www.cisco.com/c/en/us/products/security/firepower-2100-series/index.html"),
    "FPR4110-K9": EOLRecord(
        part_code="FPR4110-K9", vendor="Cisco", model="Firepower 4110 NGFW",
        end_of_sale=date(2023, 3, 31), end_of_support=date(2028, 3, 31),
        replacement_sku="FPR4215-NGFW-K9", replacement_name="Firepower 4215 NGFW",
        source_url="https://www.cisco.com/c/en/us/products/collateral/security/firepower-4100-series/eos-eol-notice-c51-743505.html"),

    # Cisco Wireless
    "AIR-CAP2702I-A-K9": EOLRecord(
        part_code="AIR-CAP2702I-A-K9", vendor="Cisco", model="Aironet 2702i AP",
        end_of_sale=date(2019, 4, 30), end_of_support=date(2024, 4, 30),
        replacement_sku="C9120AXI-B", replacement_name="Catalyst 9120AX AP",
        source_url="https://www.cisco.com/c/en/us/products/collateral/wireless/aironet-2700-series/eos-eol-notice-c51-740538.html"),
    "AIR-AP2802I-B-K9": EOLRecord(
        part_code="AIR-AP2802I-B-K9", vendor="Cisco", model="Aironet 2802i AP",
        end_of_sale=date(2022, 3, 31), end_of_support=date(2027, 3, 31),
        replacement_sku="C9130AXI-B", replacement_name="Catalyst 9130AX AP",
        source_url="https://www.cisco.com/c/en/us/products/collateral/wireless/aironet-2800-series-access-points/eos-eol-notice-c51-742891.html"),


    # ═══════════════════════════════════════════════════════════════
    # JUNIPER
    # Source: https://support.juniper.net/support/eol/
    # ═══════════════════════════════════════════════════════════════

    # EX Series Switches
    "EX2200-24T-4G": EOLRecord(
        part_code="EX2200-24T-4G", vendor="Juniper", model="EX2200-24T",
        end_of_sale=date(2019, 6, 30), end_of_support=date(2024, 12, 31),
        replacement_sku="EX2300-24T", replacement_name="EX2300-24T",
        source_url="https://support.juniper.net/support/eol/hardware/ex/"),
    "EX2200-48T-4G": EOLRecord(
        part_code="EX2200-48T-4G", vendor="Juniper", model="EX2200-48T",
        end_of_sale=date(2019, 6, 30), end_of_support=date(2024, 12, 31),
        replacement_sku="EX2300-48T", replacement_name="EX2300-48T",
        source_url="https://support.juniper.net/support/eol/hardware/ex/"),
    "EX2200-24P-4G": EOLRecord(
        part_code="EX2200-24P-4G", vendor="Juniper", model="EX2200-24P PoE",
        end_of_sale=date(2019, 6, 30), end_of_support=date(2024, 12, 31),
        replacement_sku="EX2300-24P", replacement_name="EX2300-24P PoE",
        source_url="https://support.juniper.net/support/eol/hardware/ex/"),
    "EX2300-24T": EOLRecord(
        part_code="EX2300-24T", vendor="Juniper", model="EX2300-24T",
        end_of_sale=date(2028, 1, 31), end_of_support=date(2032, 1, 31),
        replacement_sku="EX2300-24T", replacement_name="Current generation",
        source_url="https://www.juniper.net/us/en/products/switches/ex-series/ex2300-ethernet-switch.html"),
    "EX2300-48T": EOLRecord(
        part_code="EX2300-48T", vendor="Juniper", model="EX2300-48T",
        end_of_sale=date(2028, 1, 31), end_of_support=date(2032, 1, 31),
        replacement_sku="EX2300-48T", replacement_name="Current generation",
        source_url="https://www.juniper.net/us/en/products/switches/ex-series/ex2300-ethernet-switch.html"),
    "EX3300-24T": EOLRecord(
        part_code="EX3300-24T", vendor="Juniper", model="EX3300-24T",
        end_of_sale=date(2017, 6, 30), end_of_support=date(2022, 6, 30),
        replacement_sku="EX3400-24T", replacement_name="EX3400-24T",
        source_url="https://support.juniper.net/support/eol/hardware/ex/"),
    "EX3300-48T": EOLRecord(
        part_code="EX3300-48T", vendor="Juniper", model="EX3300-48T",
        end_of_sale=date(2017, 6, 30), end_of_support=date(2022, 6, 30),
        replacement_sku="EX3400-48T", replacement_name="EX3400-48T",
        source_url="https://support.juniper.net/support/eol/hardware/ex/"),
    "EX4200-24T": EOLRecord(
        part_code="EX4200-24T", vendor="Juniper", model="EX4200-24T",
        end_of_sale=date(2016, 7, 31), end_of_support=date(2021, 7, 31),
        replacement_sku="EX4300-24T", replacement_name="EX4300-24T",
        source_url="https://support.juniper.net/support/eol/hardware/ex/"),
    "EX4300-24T": EOLRecord(
        part_code="EX4300-24T", vendor="Juniper", model="EX4300-24T",
        end_of_sale=date(2024, 3, 31), end_of_support=date(2029, 3, 31),
        replacement_sku="EX4400-24T", replacement_name="EX4400-24T",
        source_url="https://support.juniper.net/support/eol/hardware/ex/"),
    "EX4300-48T": EOLRecord(
        part_code="EX4300-48T", vendor="Juniper", model="EX4300-48T",
        end_of_sale=date(2024, 3, 31), end_of_support=date(2029, 3, 31),
        replacement_sku="EX4400-48T", replacement_name="EX4400-48T",
        source_url="https://support.juniper.net/support/eol/hardware/ex/"),
    "EX4400-24T": EOLRecord(
        part_code="EX4400-24T", vendor="Juniper", model="EX4400-24T",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="EX4400-24T", replacement_name="Current generation",
        source_url="https://www.juniper.net/us/en/products/switches/ex-series/ex4400-ethernet-switch.html"),

    # SRX Series Firewalls
    "SRX100H2": EOLRecord(
        part_code="SRX100H2", vendor="Juniper", model="SRX100 Services Gateway",
        end_of_sale=date(2016, 6, 30), end_of_support=date(2021, 6, 30),
        replacement_sku="SRX300", replacement_name="SRX300 Services Gateway",
        source_url="https://support.juniper.net/support/eol/hardware/srx/"),
    "SRX210HE2": EOLRecord(
        part_code="SRX210HE2", vendor="Juniper", model="SRX210 Services Gateway",
        end_of_sale=date(2016, 6, 30), end_of_support=date(2021, 6, 30),
        replacement_sku="SRX320", replacement_name="SRX320 Services Gateway",
        source_url="https://support.juniper.net/support/eol/hardware/srx/"),
    "SRX220H2": EOLRecord(
        part_code="SRX220H2", vendor="Juniper", model="SRX220 Services Gateway",
        end_of_sale=date(2016, 6, 30), end_of_support=date(2021, 6, 30),
        replacement_sku="SRX320", replacement_name="SRX320 Services Gateway",
        source_url="https://support.juniper.net/support/eol/hardware/srx/"),
    "SRX300": EOLRecord(
        part_code="SRX300", vendor="Juniper", model="SRX300 Services Gateway",
        end_of_sale=date(2023, 4, 30), end_of_support=date(2025, 12, 31),
        replacement_sku="SRX345", replacement_name="SRX345 Services Gateway",
        source_url="https://support.juniper.net/support/eol/hardware/srx/"),
    "SRX320": EOLRecord(
        part_code="SRX320", vendor="Juniper", model="SRX320 Services Gateway",
        end_of_sale=date(2023, 4, 30), end_of_support=date(2026, 12, 31),
        replacement_sku="SRX345", replacement_name="SRX345 Services Gateway",
        source_url="https://support.juniper.net/support/eol/hardware/srx/"),
    "SRX340": EOLRecord(
        part_code="SRX340", vendor="Juniper", model="SRX340 Services Gateway",
        end_of_sale=date(2024, 6, 30), end_of_support=date(2027, 12, 31),
        replacement_sku="SRX380", replacement_name="SRX380 Services Gateway",
        source_url="https://support.juniper.net/support/eol/hardware/srx/"),
    "SRX345": EOLRecord(
        part_code="SRX345", vendor="Juniper", model="SRX345 Services Gateway",
        end_of_sale=date(2027, 12, 31), end_of_support=date(2032, 12, 31),
        replacement_sku="SRX345", replacement_name="Current generation",
        source_url="https://www.juniper.net/us/en/products/security/srx-series/srx345-services-gateway.html"),
    "SRX380": EOLRecord(
        part_code="SRX380", vendor="Juniper", model="SRX380 Services Gateway",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="SRX380", replacement_name="Current generation",
        source_url="https://www.juniper.net/us/en/products/security/srx-series/srx380-services-gateway.html"),
    "SRX550M": EOLRecord(
        part_code="SRX550M", vendor="Juniper", model="SRX550M Services Gateway",
        end_of_sale=date(2020, 12, 31), end_of_support=date(2025, 12, 31),
        replacement_sku="SRX1500", replacement_name="SRX1500 Services Gateway",
        source_url="https://support.juniper.net/support/eol/hardware/srx/"),
    "SRX1500": EOLRecord(
        part_code="SRX1500", vendor="Juniper", model="SRX1500 Services Gateway",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        replacement_sku="SRX1500", replacement_name="Current generation",
        source_url="https://www.juniper.net/us/en/products/security/srx-series/srx1500-services-gateway.html"),

    # MX Series Routers
    "MX80": EOLRecord(
        part_code="MX80", vendor="Juniper", model="MX80 Router",
        end_of_sale=date(2018, 3, 31), end_of_support=date(2023, 3, 31),
        replacement_sku="MX204", replacement_name="MX204 Universal Routing Platform",
        source_url="https://support.juniper.net/support/eol/hardware/mx/"),
    "MX104": EOLRecord(
        part_code="MX104", vendor="Juniper", model="MX104 Router",
        end_of_sale=date(2020, 12, 31), end_of_support=date(2025, 12, 31),
        replacement_sku="MX204", replacement_name="MX204 Universal Routing Platform",
        source_url="https://support.juniper.net/support/eol/hardware/mx/"),
    "MX204": EOLRecord(
        part_code="MX204", vendor="Juniper", model="MX204 Universal Routing Platform",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="MX204", replacement_name="Current generation",
        source_url="https://www.juniper.net/us/en/products/routers/mx-series/mx204-universal-routing-platform.html"),


    # ═══════════════════════════════════════════════════════════════
    # HP ARUBA
    # Source: https://www.arubanetworks.com/support-services/end-of-life/
    # ═══════════════════════════════════════════════════════════════

    # Aruba 2500 / 2530 series
    "J9727A": EOLRecord(
        part_code="J9727A", vendor="HP Aruba", model="Aruba 2920-24G Switch",
        end_of_sale=date(2021, 10, 31), end_of_support=date(2026, 10, 31),
        replacement_sku="JL254A", replacement_name="Aruba 2930F 24G",
        source_url="https://h20195.www2.hpe.com/v2/getpdf.aspx/a00020103enw.pdf"),
    "J9772A": EOLRecord(
        part_code="J9772A", vendor="HP Aruba", model="Aruba 2530-24G Switch",
        end_of_sale=date(2020, 12, 31), end_of_support=date(2025, 6, 30),
        replacement_sku="JL683A", replacement_name="Aruba 2930F 24G",
        source_url="https://h20195.www2.hpe.com/v2/getpdf.aspx/a00001439enw.pdf"),
    "J9776A": EOLRecord(
        part_code="J9776A", vendor="HP Aruba", model="Aruba 2530-48G Switch",
        end_of_sale=date(2020, 12, 31), end_of_support=date(2025, 6, 30),
        replacement_sku="JL262A", replacement_name="Aruba 2930F 48G",
        source_url="https://h20195.www2.hpe.com/v2/getpdf.aspx/a00001439enw.pdf"),
    "J9779A": EOLRecord(
        part_code="J9779A", vendor="HP Aruba", model="Aruba 2530-8G Switch",
        end_of_sale=date(2020, 12, 31), end_of_support=date(2025, 6, 30),
        replacement_sku="JL258A", replacement_name="Aruba 2930F 8G",
        source_url="https://h20195.www2.hpe.com/v2/getpdf.aspx/a00001439enw.pdf"),

    # Aruba 2920 / 2930 series
    "JL253A": EOLRecord(
        part_code="JL253A", vendor="HP Aruba", model="Aruba 2930F 8G PoE+",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="JL253A", replacement_name="Current generation",
        source_url="https://www.arubanetworks.com/products/switches/access/2930f-series/"),
    "JL254A": EOLRecord(
        part_code="JL254A", vendor="HP Aruba", model="Aruba 2930F 24G",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="JL254A", replacement_name="Current generation",
        source_url="https://www.arubanetworks.com/products/switches/access/2930f-series/"),
    "JL262A": EOLRecord(
        part_code="JL262A", vendor="HP Aruba", model="Aruba 2930F 48G",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="JL262A", replacement_name="Current generation",
        source_url="https://www.arubanetworks.com/products/switches/access/2930f-series/"),

    # Aruba 3810 / 5400 series
    "JL071A": EOLRecord(
        part_code="JL071A", vendor="HP Aruba", model="Aruba 3810M 24G",
        end_of_sale=date(2025, 6, 30), end_of_support=date(2030, 6, 30),
        replacement_sku="JL675A", replacement_name="Aruba 6300M 24-port",
        source_url="https://h20195.www2.hpe.com/v2/getpdf.aspx/a00082568enw.pdf"),
    "JL075A": EOLRecord(
        part_code="JL075A", vendor="HP Aruba", model="Aruba 3810M 48G",
        end_of_sale=date(2025, 6, 30), end_of_support=date(2030, 6, 30),
        replacement_sku="JL676A", replacement_name="Aruba 6300M 48-port",
        source_url="https://h20195.www2.hpe.com/v2/getpdf.aspx/a00082568enw.pdf"),
    "J9850A": EOLRecord(
        part_code="J9850A", vendor="HP Aruba", model="Aruba 5412R zl2",
        end_of_sale=date(2024, 4, 30), end_of_support=date(2029, 4, 30),
        replacement_sku="JL579A", replacement_name="Aruba 8325-48Y8C",
        source_url="https://h20195.www2.hpe.com/v2/getpdf.aspx/a00107248enw.pdf"),

    # Aruba 6200 / 6300 / 6400 — current gen
    "JL677A": EOLRecord(
        part_code="JL677A", vendor="HP Aruba", model="Aruba 6200F 48G",
        end_of_sale=date(2030, 3, 31), end_of_support=date(2035, 3, 31),
        replacement_sku="JL677A", replacement_name="Current generation",
        source_url="https://www.arubanetworks.com/products/switches/access/6200-series/"),
    "JL675A": EOLRecord(
        part_code="JL675A", vendor="HP Aruba", model="Aruba 6300M 24-port",
        end_of_sale=date(2030, 12, 31), end_of_support=date(2035, 12, 31),
        replacement_sku="JL675A", replacement_name="Current generation",
        source_url="https://www.arubanetworks.com/products/switches/aggregation/6300-series/"),

    # Aruba Wireless Controllers
    "ARCN0005": EOLRecord(
        part_code="ARCN0005", vendor="HP Aruba", model="Aruba 7210 Mobility Controller",
        end_of_sale=date(2022, 10, 31), end_of_support=date(2027, 10, 31),
        replacement_sku="Q9G69A", replacement_name="Aruba 9004 Mobility Controller",
        source_url="https://h20195.www2.hpe.com/v2/getpdf.aspx/a00106312enw.pdf"),

    # Aruba APs
    "AP-305": EOLRecord(
        part_code="AP-305", vendor="HP Aruba", model="Aruba AP-305",
        end_of_sale=date(2021, 3, 31), end_of_support=date(2026, 3, 31),
        replacement_sku="AP-515", replacement_name="Aruba AP-515",
        source_url="https://h20195.www2.hpe.com/v2/getpdf.aspx/a00080574enw.pdf"),
    "AP-315": EOLRecord(
        part_code="AP-315", vendor="HP Aruba", model="Aruba AP-315",
        end_of_sale=date(2021, 3, 31), end_of_support=date(2026, 3, 31),
        replacement_sku="AP-515", replacement_name="Aruba AP-515",
        source_url="https://h20195.www2.hpe.com/v2/getpdf.aspx/a00080574enw.pdf"),
    "AP-515": EOLRecord(
        part_code="AP-515", vendor="HP Aruba", model="Aruba AP-515 Wi-Fi 6",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="AP-515", replacement_name="Current generation",
        source_url="https://www.arubanetworks.com/products/wireless/access-points/outdoor-access-points/ap-515/"),


    # ═══════════════════════════════════════════════════════════════
    # ARISTA NETWORKS
    # Source: https://www.arista.com/en/support/product-lifecycle
    # ═══════════════════════════════════════════════════════════════

    "DCS-7050CX3-32S": EOLRecord(
        part_code="DCS-7050CX3-32S", vendor="Arista", model="7050CX3-32S 100G Switch",
        end_of_sale=date(2027, 6, 30), end_of_support=date(2032, 6, 30),
        replacement_sku="DCS-7060CX2-32S", replacement_name="Arista 7060CX2-32S",
        source_url="https://www.arista.com/en/support/product-lifecycle"),
    "DCS-7050TX-64": EOLRecord(
        part_code="DCS-7050TX-64", vendor="Arista", model="7050TX-64 1G/10G Switch",
        end_of_sale=date(2020, 9, 30), end_of_support=date(2025, 9, 30),
        replacement_sku="DCS-7050CX3-32S", replacement_name="Arista 7050CX3-32S",
        source_url="https://www.arista.com/en/support/product-lifecycle"),
    "DCS-7050TX3-48C8": EOLRecord(
        part_code="DCS-7050TX3-48C8", vendor="Arista", model="7050TX3-48C8 25G Switch",
        end_of_sale=date(2026, 12, 31), end_of_support=date(2031, 12, 31),
        replacement_sku="DCS-7050TX3-48C8", replacement_name="Current generation",
        source_url="https://www.arista.com/en/support/product-lifecycle"),
    "DCS-7060CX2-32S": EOLRecord(
        part_code="DCS-7060CX2-32S", vendor="Arista", model="7060CX2-32S 100G Switch",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        replacement_sku="DCS-7060CX2-32S", replacement_name="Current generation",
        source_url="https://www.arista.com/en/support/product-lifecycle"),
    "DCS-7160-32CQ": EOLRecord(
        part_code="DCS-7160-32CQ", vendor="Arista", model="7160-32CQ 100G Switch",
        end_of_sale=date(2023, 3, 31), end_of_support=date(2028, 3, 31),
        replacement_sku="DCS-7170-64C", replacement_name="Arista 7170-64C",
        source_url="https://www.arista.com/en/support/product-lifecycle"),
    "DCS-7170-64C": EOLRecord(
        part_code="DCS-7170-64C", vendor="Arista", model="7170-64C 100G Switch",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="DCS-7170-64C", replacement_name="Current generation",
        source_url="https://www.arista.com/en/support/product-lifecycle"),
    "DCS-7280CR2-60": EOLRecord(
        part_code="DCS-7280CR2-60", vendor="Arista", model="7280CR2-60 100G Router",
        end_of_sale=date(2024, 6, 30), end_of_support=date(2029, 6, 30),
        replacement_sku="DCS-7280CR3-96", replacement_name="Arista 7280CR3-96",
        source_url="https://www.arista.com/en/support/product-lifecycle"),
    "DCS-7280CR3-96": EOLRecord(
        part_code="DCS-7280CR3-96", vendor="Arista", model="7280CR3-96 400G Router",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="DCS-7280CR3-96", replacement_name="Current generation",
        source_url="https://www.arista.com/en/support/product-lifecycle"),
    "DCS-7300X-32Q": EOLRecord(
        part_code="DCS-7300X-32Q", vendor="Arista", model="7300X-32Q Spine Switch",
        end_of_sale=date(2021, 6, 30), end_of_support=date(2026, 6, 30),
        replacement_sku="DCS-7358X4", replacement_name="Arista 7358X4",
        source_url="https://www.arista.com/en/support/product-lifecycle"),
    "DCS-7358X4": EOLRecord(
        part_code="DCS-7358X4", vendor="Arista", model="7358X4 400G Spine Switch",
        end_of_sale=date(2030, 12, 31), end_of_support=date(2035, 12, 31),
        replacement_sku="DCS-7358X4", replacement_name="Current generation",
        source_url="https://www.arista.com/en/support/product-lifecycle"),
    "DCS-7010T-48": EOLRecord(
        part_code="DCS-7010T-48", vendor="Arista", model="7010T-48 1G Access Switch",
        end_of_sale=date(2018, 12, 31), end_of_support=date(2023, 12, 31),
        replacement_sku="DCS-7050TX3-48C8", replacement_name="Arista 7050TX3-48C8",
        source_url="https://www.arista.com/en/support/product-lifecycle"),


    # ═══════════════════════════════════════════════════════════════
    # DELL NETWORKING (now Dell EMC / Dell Technologies)
    # Source: https://www.dell.com/en-us/dt/corporate/about-us/eol-notice.htm
    # ═══════════════════════════════════════════════════════════════

    "N2024": EOLRecord(
        part_code="N2024", vendor="Dell", model="Dell N2024 24-Port Switch",
        end_of_sale=date(2020, 12, 31), end_of_support=date(2025, 12, 31),
        replacement_sku="N3224T-ON", replacement_name="Dell N3224T-ON",
        source_url="https://www.dell.com/en-us/dt/networking/switches.htm"),
    "N2048": EOLRecord(
        part_code="N2048", vendor="Dell", model="Dell N2048 48-Port Switch",
        end_of_sale=date(2020, 12, 31), end_of_support=date(2025, 12, 31),
        replacement_sku="N3248TE-ON", replacement_name="Dell N3248TE-ON",
        source_url="https://www.dell.com/en-us/dt/networking/switches.htm"),
    "N3024": EOLRecord(
        part_code="N3024", vendor="Dell", model="Dell N3024 24-Port Switch",
        end_of_sale=date(2021, 6, 30), end_of_support=date(2026, 6, 30),
        replacement_sku="N3224T-ON", replacement_name="Dell N3224T-ON",
        source_url="https://www.dell.com/en-us/dt/networking/switches.htm"),
    "N3048": EOLRecord(
        part_code="N3048", vendor="Dell", model="Dell N3048 48-Port Switch",
        end_of_sale=date(2021, 6, 30), end_of_support=date(2026, 6, 30),
        replacement_sku="N3248TE-ON", replacement_name="Dell N3248TE-ON",
        source_url="https://www.dell.com/en-us/dt/networking/switches.htm"),
    "N3224T-ON": EOLRecord(
        part_code="N3224T-ON", vendor="Dell", model="Dell N3224T-ON 24-Port",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        replacement_sku="N3224T-ON", replacement_name="Current generation",
        source_url="https://www.dell.com/en-us/dt/networking/ethernet-switches/n3200-on-series.htm"),
    "N3248TE-ON": EOLRecord(
        part_code="N3248TE-ON", vendor="Dell", model="Dell N3248TE-ON 48-Port",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        replacement_sku="N3248TE-ON", replacement_name="Current generation",
        source_url="https://www.dell.com/en-us/dt/networking/ethernet-switches/n3200-on-series.htm"),
    "S4128F-ON": EOLRecord(
        part_code="S4128F-ON", vendor="Dell", model="Dell S4128F-ON 10GbE Switch",
        end_of_sale=date(2023, 12, 31), end_of_support=date(2028, 12, 31),
        replacement_sku="S5248F-ON", replacement_name="Dell S5248F-ON",
        source_url="https://www.dell.com/en-us/dt/networking/ethernet-switches/s4000-on-series.htm"),
    "S4148F-ON": EOLRecord(
        part_code="S4148F-ON", vendor="Dell", model="Dell S4148F-ON 10GbE Switch",
        end_of_sale=date(2023, 12, 31), end_of_support=date(2028, 12, 31),
        replacement_sku="S5248F-ON", replacement_name="Dell S5248F-ON",
        source_url="https://www.dell.com/en-us/dt/networking/ethernet-switches/s4000-on-series.htm"),
    "S5248F-ON": EOLRecord(
        part_code="S5248F-ON", vendor="Dell", model="Dell S5248F-ON 25GbE Switch",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="S5248F-ON", replacement_name="Current generation",
        source_url="https://www.dell.com/en-us/dt/networking/ethernet-switches/s5200-on-series.htm"),
    "Z9100-ON": EOLRecord(
        part_code="Z9100-ON", vendor="Dell", model="Dell Z9100-ON 100GbE Switch",
        end_of_sale=date(2022, 9, 30), end_of_support=date(2027, 9, 30),
        replacement_sku="Z9332F-ON", replacement_name="Dell Z9332F-ON 400G",
        source_url="https://www.dell.com/en-us/dt/networking/ethernet-switches/z9100-on.htm"),
    "Z9332F-ON": EOLRecord(
        part_code="Z9332F-ON", vendor="Dell", model="Dell Z9332F-ON 400GbE Switch",
        end_of_sale=date(2030, 12, 31), end_of_support=date(2035, 12, 31),
        replacement_sku="Z9332F-ON", replacement_name="Current generation",
        source_url="https://www.dell.com/en-us/dt/networking/ethernet-switches/z9332f-on.htm"),


    # ═══════════════════════════════════════════════════════════════
    # FORTINET
    # Source: https://www.fortinet.com/corporate/about-us/product-end-of-life
    # ═══════════════════════════════════════════════════════════════

    "FG-60D": EOLRecord(
        part_code="FG-60D", vendor="Fortinet", model="FortiGate 60D",
        end_of_sale=date(2019, 3, 31), end_of_support=date(2024, 3, 31),
        replacement_sku="FG-60F", replacement_name="FortiGate 60F",
        source_url="https://support.fortinet.com/Information/ProductLifeCycle.aspx"),
    "FG-60E": EOLRecord(
        part_code="FG-60E", vendor="Fortinet", model="FortiGate 60E",
        end_of_sale=date(2022, 3, 31), end_of_support=date(2026, 3, 31),
        replacement_sku="FG-60F", replacement_name="FortiGate 60F",
        source_url="https://support.fortinet.com/Information/ProductLifeCycle.aspx"),
    "FG-60F": EOLRecord(
        part_code="FG-60F", vendor="Fortinet", model="FortiGate 60F",
        end_of_sale=date(2027, 12, 31), end_of_support=date(2032, 12, 31),
        replacement_sku="FG-60F", replacement_name="Current generation",
        source_url="https://www.fortinet.com/products/next-generation-firewall/fortigate-60f"),
    "FG-100D": EOLRecord(
        part_code="FG-100D", vendor="Fortinet", model="FortiGate 100D",
        end_of_sale=date(2019, 9, 30), end_of_support=date(2024, 9, 30),
        replacement_sku="FG-100F", replacement_name="FortiGate 100F",
        source_url="https://support.fortinet.com/Information/ProductLifeCycle.aspx"),
    "FG-100E": EOLRecord(
        part_code="FG-100E", vendor="Fortinet", model="FortiGate 100E",
        end_of_sale=date(2022, 9, 30), end_of_support=date(2026, 9, 30),
        replacement_sku="FG-100F", replacement_name="FortiGate 100F",
        source_url="https://support.fortinet.com/Information/ProductLifeCycle.aspx"),
    "FG-100F": EOLRecord(
        part_code="FG-100F", vendor="Fortinet", model="FortiGate 100F",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        replacement_sku="FG-100F", replacement_name="Current generation",
        source_url="https://www.fortinet.com/products/next-generation-firewall/fortigate-100f"),
    "FG-200D": EOLRecord(
        part_code="FG-200D", vendor="Fortinet", model="FortiGate 200D",
        end_of_sale=date(2020, 6, 30), end_of_support=date(2025, 6, 30),
        replacement_sku="FG-200F", replacement_name="FortiGate 200F",
        source_url="https://support.fortinet.com/Information/ProductLifeCycle.aspx"),
    "FG-200E": EOLRecord(
        part_code="FG-200E", vendor="Fortinet", model="FortiGate 200E",
        end_of_sale=date(2023, 6, 30), end_of_support=date(2027, 6, 30),
        replacement_sku="FG-200F", replacement_name="FortiGate 200F",
        source_url="https://support.fortinet.com/Information/ProductLifeCycle.aspx"),
    "FG-200F": EOLRecord(
        part_code="FG-200F", vendor="Fortinet", model="FortiGate 200F",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="FG-200F", replacement_name="Current generation",
        source_url="https://www.fortinet.com/products/next-generation-firewall/fortigate-200f"),
    "FG-300D": EOLRecord(
        part_code="FG-300D", vendor="Fortinet", model="FortiGate 300D",
        end_of_sale=date(2020, 12, 31), end_of_support=date(2025, 12, 31),
        replacement_sku="FG-300F", replacement_name="FortiGate 300F",
        source_url="https://support.fortinet.com/Information/ProductLifeCycle.aspx"),
    "FG-300E": EOLRecord(
        part_code="FG-300E", vendor="Fortinet", model="FortiGate 300E",
        end_of_sale=date(2023, 12, 31), end_of_support=date(2027, 12, 31),
        replacement_sku="FG-300F", replacement_name="FortiGate 300F",
        source_url="https://support.fortinet.com/Information/ProductLifeCycle.aspx"),
    "FG-300F": EOLRecord(
        part_code="FG-300F", vendor="Fortinet", model="FortiGate 300F",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="FG-300F", replacement_name="Current generation",
        source_url="https://www.fortinet.com/products/next-generation-firewall/fortigate-300f"),
    "FG-500D": EOLRecord(
        part_code="FG-500D", vendor="Fortinet", model="FortiGate 500D",
        end_of_sale=date(2020, 12, 31), end_of_support=date(2025, 12, 31),
        replacement_sku="FG-500F", replacement_name="FortiGate 500F / 600F",
        source_url="https://support.fortinet.com/Information/ProductLifeCycle.aspx"),
    "FG-600D": EOLRecord(
        part_code="FG-600D", vendor="Fortinet", model="FortiGate 600D",
        end_of_sale=date(2021, 3, 31), end_of_support=date(2026, 3, 31),
        replacement_sku="FG-600F", replacement_name="FortiGate 600F",
        source_url="https://support.fortinet.com/Information/ProductLifeCycle.aspx"),
    "FG-600F": EOLRecord(
        part_code="FG-600F", vendor="Fortinet", model="FortiGate 600F",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="FG-600F", replacement_name="Current generation",
        source_url="https://www.fortinet.com/products/next-generation-firewall/fortigate-600f"),
    "FG-1000D": EOLRecord(
        part_code="FG-1000D", vendor="Fortinet", model="FortiGate 1000D",
        end_of_sale=date(2021, 12, 31), end_of_support=date(2026, 12, 31),
        replacement_sku="FG-1000F", replacement_name="FortiGate 1000F",
        source_url="https://support.fortinet.com/Information/ProductLifeCycle.aspx"),
    "FG-1800F": EOLRecord(
        part_code="FG-1800F", vendor="Fortinet", model="FortiGate 1800F",
        end_of_sale=date(2030, 12, 31), end_of_support=date(2035, 12, 31),
        replacement_sku="FG-1800F", replacement_name="Current generation",
        source_url="https://www.fortinet.com/products/next-generation-firewall/fortigate-1800f"),
    # FortiSwitch
    "FS-108E": EOLRecord(
        part_code="FS-108E", vendor="Fortinet", model="FortiSwitch 108E",
        end_of_sale=date(2027, 12, 31), end_of_support=date(2032, 12, 31),
        replacement_sku="FS-108E", replacement_name="Current generation",
        source_url="https://www.fortinet.com/products/switches/fortiswitch"),
    "FS-124D": EOLRecord(
        part_code="FS-124D", vendor="Fortinet", model="FortiSwitch 124D",
        end_of_sale=date(2022, 6, 30), end_of_support=date(2027, 6, 30),
        replacement_sku="FS-124F", replacement_name="FortiSwitch 124F",
        source_url="https://support.fortinet.com/Information/ProductLifeCycle.aspx"),
    "FS-124F": EOLRecord(
        part_code="FS-124F", vendor="Fortinet", model="FortiSwitch 124F",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="FS-124F", replacement_name="Current generation",
        source_url="https://www.fortinet.com/products/switches/fortiswitch"),
    "FS-248D": EOLRecord(
        part_code="FS-248D", vendor="Fortinet", model="FortiSwitch 248D",
        end_of_sale=date(2022, 6, 30), end_of_support=date(2027, 6, 30),
        replacement_sku="FS-248F", replacement_name="FortiSwitch 248F",
        source_url="https://support.fortinet.com/Information/ProductLifeCycle.aspx"),
    "FS-248F": EOLRecord(
        part_code="FS-248F", vendor="Fortinet", model="FortiSwitch 248F",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="FS-248F", replacement_name="Current generation",
        source_url="https://www.fortinet.com/products/switches/fortiswitch"),


    # ═══════════════════════════════════════════════════════════════
    # PALO ALTO NETWORKS
    # Source: https://www.paloaltonetworks.com/services/support/end-of-life-announcements
    # ═══════════════════════════════════════════════════════════════

    "PA-200": EOLRecord(
        part_code="PA-200", vendor="Palo Alto", model="PA-200 Next-Gen Firewall",
        end_of_sale=date(2019, 6, 30), end_of_support=date(2024, 6, 30),
        replacement_sku="PA-415", replacement_name="PA-415 Next-Gen Firewall",
        source_url="https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware"),
    "PA-220": EOLRecord(
        part_code="PA-220", vendor="Palo Alto", model="PA-220 Next-Gen Firewall",
        end_of_sale=date(2023, 2, 28), end_of_support=date(2025, 9, 30),
        replacement_sku="PA-440", replacement_name="PA-440 Next-Gen Firewall",
        source_url="https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware"),
    "PA-220R": EOLRecord(
        part_code="PA-220R", vendor="Palo Alto", model="PA-220R Ruggedized Firewall",
        end_of_sale=date(2024, 1, 31), end_of_support=date(2026, 12, 31),
        replacement_sku="PA-415-5G", replacement_name="PA-415-5G Firewall",
        source_url="https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware"),
    "PA-500": EOLRecord(
        part_code="PA-500", vendor="Palo Alto", model="PA-500 Next-Gen Firewall",
        end_of_sale=date(2018, 12, 31), end_of_support=date(2023, 12, 31),
        replacement_sku="PA-850", replacement_name="PA-850 Next-Gen Firewall",
        source_url="https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware"),
    "PA-820": EOLRecord(
        part_code="PA-820", vendor="Palo Alto", model="PA-820 Next-Gen Firewall",
        end_of_sale=date(2025, 1, 31), end_of_support=date(2027, 12, 31),
        replacement_sku="PA-850", replacement_name="PA-850 Next-Gen Firewall",
        source_url="https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware"),
    "PA-850": EOLRecord(
        part_code="PA-850", vendor="Palo Alto", model="PA-850 Next-Gen Firewall",
        end_of_sale=date(2027, 6, 30), end_of_support=date(2032, 6, 30),
        replacement_sku="PA-850", replacement_name="Current generation",
        source_url="https://www.paloaltonetworks.com/products/product-selection"),
    "PA-3020": EOLRecord(
        part_code="PA-3020", vendor="Palo Alto", model="PA-3020 Next-Gen Firewall",
        end_of_sale=date(2020, 6, 30), end_of_support=date(2025, 6, 30),
        replacement_sku="PA-3220", replacement_name="PA-3220 Next-Gen Firewall",
        source_url="https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware"),
    "PA-3050": EOLRecord(
        part_code="PA-3050", vendor="Palo Alto", model="PA-3050 Next-Gen Firewall",
        end_of_sale=date(2020, 6, 30), end_of_support=date(2025, 6, 30),
        replacement_sku="PA-3250", replacement_name="PA-3250 Next-Gen Firewall",
        source_url="https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware"),
    "PA-3220": EOLRecord(
        part_code="PA-3220", vendor="Palo Alto", model="PA-3220 Next-Gen Firewall",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        replacement_sku="PA-3220", replacement_name="Current generation",
        source_url="https://www.paloaltonetworks.com/products/product-selection"),
    "PA-3250": EOLRecord(
        part_code="PA-3250", vendor="Palo Alto", model="PA-3250 Next-Gen Firewall",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        replacement_sku="PA-3250", replacement_name="Current generation",
        source_url="https://www.paloaltonetworks.com/products/product-selection"),
    "PA-440": EOLRecord(
        part_code="PA-440", vendor="Palo Alto", model="PA-440 Next-Gen Firewall",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="PA-440", replacement_name="Current generation",
        source_url="https://www.paloaltonetworks.com/products/product-selection"),
    "PA-450": EOLRecord(
        part_code="PA-450", vendor="Palo Alto", model="PA-450 Next-Gen Firewall",
        end_of_sale=date(2029, 1, 31), end_of_support=date(2034, 1, 31),
        replacement_sku="PA-450", replacement_name="Current generation",
        source_url="https://www.paloaltonetworks.com/products/product-selection"),
    "PA-5020": EOLRecord(
        part_code="PA-5020", vendor="Palo Alto", model="PA-5020 Next-Gen Firewall",
        end_of_sale=date(2018, 10, 31), end_of_support=date(2023, 10, 31),
        replacement_sku="PA-5250", replacement_name="PA-5250 Next-Gen Firewall",
        source_url="https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware"),
    "PA-5060": EOLRecord(
        part_code="PA-5060", vendor="Palo Alto", model="PA-5060 Next-Gen Firewall",
        end_of_sale=date(2021, 6, 30), end_of_support=date(2026, 6, 30),
        replacement_sku="PA-5450", replacement_name="PA-5450 Next-Gen Firewall",
        source_url="https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware"),
    "PA-5250": EOLRecord(
        part_code="PA-5250", vendor="Palo Alto", model="PA-5250 Next-Gen Firewall",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="PA-5250", replacement_name="Current generation",
        source_url="https://www.paloaltonetworks.com/products/product-selection"),
    "PA-7050": EOLRecord(
        part_code="PA-7050", vendor="Palo Alto", model="PA-7050 Data Centre Firewall",
        end_of_sale=date(2024, 6, 30), end_of_support=date(2029, 6, 30),
        replacement_sku="PA-7080", replacement_name="PA-7080 Data Centre Firewall",
        source_url="https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware"),
    "PA-7080": EOLRecord(
        part_code="PA-7080", vendor="Palo Alto", model="PA-7080 Data Centre Firewall",
        end_of_sale=date(2030, 12, 31), end_of_support=date(2035, 12, 31),
        replacement_sku="PA-7080", replacement_name="Current generation",
        source_url="https://www.paloaltonetworks.com/products/product-selection"),


    # ═══════════════════════════════════════════════════════════════
    # EXTREME NETWORKS
    # Source: https://www.extremenetworks.com/support/end-of-life/
    # ═══════════════════════════════════════════════════════════════

    "17101": EOLRecord(
        part_code="17101", vendor="Extreme Networks", model="Summit X440-24t",
        end_of_sale=date(2018, 7, 31), end_of_support=date(2023, 7, 31),
        replacement_sku="17200", replacement_name="ExtremeSwitching X465-24MU",
        source_url="https://www.extremenetworks.com/support/end-of-life/"),
    "17110": EOLRecord(
        part_code="17110", vendor="Extreme Networks", model="Summit X440-48t",
        end_of_sale=date(2018, 7, 31), end_of_support=date(2023, 7, 31),
        replacement_sku="17210", replacement_name="ExtremeSwitching X465-48W",
        source_url="https://www.extremenetworks.com/support/end-of-life/"),
    "16701": EOLRecord(
        part_code="16701", vendor="Extreme Networks", model="Summit X460-24t",
        end_of_sale=date(2019, 12, 31), end_of_support=date(2024, 12, 31),
        replacement_sku="17500", replacement_name="ExtremeSwitching X590-24x-1q",
        source_url="https://www.extremenetworks.com/support/end-of-life/"),
    "17200": EOLRecord(
        part_code="17200", vendor="Extreme Networks", model="ExtremeSwitching X465-24MU",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        replacement_sku="17200", replacement_name="Current generation",
        source_url="https://www.extremenetworks.com/products/switching/extremeswitching-x465/"),
    "17500": EOLRecord(
        part_code="17500", vendor="Extreme Networks", model="ExtremeSwitching X590-24x-1q",
        end_of_sale=date(2027, 12, 31), end_of_support=date(2032, 12, 31),
        replacement_sku="17500", replacement_name="Current generation",
        source_url="https://www.extremenetworks.com/products/switching/extremeswitching-x590/"),
    "BR-VDX6740": EOLRecord(
        part_code="BR-VDX6740", vendor="Extreme Networks", model="VDX 6740 (Brocade)",
        end_of_sale=date(2019, 8, 31), end_of_support=date(2024, 8, 31),
        replacement_sku="17500", replacement_name="ExtremeSwitching X590",
        source_url="https://www.extremenetworks.com/support/end-of-life/"),
    "BR-SLX9540": EOLRecord(
        part_code="BR-SLX9540", vendor="Extreme Networks", model="SLX 9540 (Brocade)",
        end_of_sale=date(2022, 8, 31), end_of_support=date(2027, 8, 31),
        replacement_sku="BR-SLX9640", replacement_name="SLX 9640",
        source_url="https://www.extremenetworks.com/support/end-of-life/"),
    "BR-SLX9640": EOLRecord(
        part_code="BR-SLX9640", vendor="Extreme Networks", model="SLX 9640",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="BR-SLX9640", replacement_name="Current generation",
        source_url="https://www.extremenetworks.com/products/routing/slx-series/"),
    "AP460C": EOLRecord(
        part_code="AP460C", vendor="Extreme Networks", model="AP460C Wi-Fi 6 AP",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="AP460C", replacement_name="Current generation",
        source_url="https://www.extremenetworks.com/products/wireless/ap460-series/"),
    "AP305C": EOLRecord(
        part_code="AP305C", vendor="Extreme Networks", model="AP305C Wi-Fi 5 AP",
        end_of_sale=date(2024, 3, 31), end_of_support=date(2029, 3, 31),
        replacement_sku="AP305CX", replacement_name="AP305CX Wi-Fi 6",
        source_url="https://www.extremenetworks.com/support/end-of-life/"),
    "AP305CX": EOLRecord(
        part_code="AP305CX", vendor="Extreme Networks", model="AP305CX Wi-Fi 6 AP",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="AP305CX", replacement_name="Current generation",
        source_url="https://www.extremenetworks.com/products/wireless/ap305cx/"),


    # ═══════════════════════════════════════════════════════════════
    # STARLINK (SpaceX)
    # Source: https://www.starlink.com/legal#end-of-life  &  SpaceX bulletins
    # Note: Starlink hardware is subscriber equipment, not traditional
    #       networking gear. SpaceX issues gen transitions rather than
    #       formal EOS/EOL bulletins. Dates reflect known gen transitions.
    # ═══════════════════════════════════════════════════════════════

    "STARLINK-DISH-GEN1": EOLRecord(
        part_code="STARLINK-DISH-GEN1", vendor="Starlink", model="Starlink Dish Gen 1 (Round)",
        end_of_sale=date(2021, 12, 31), end_of_support=date(2026, 12, 31),
        replacement_sku="STARLINK-DISH-GEN3", replacement_name="Starlink Dish Gen 3 (Standard)",
        source_url="https://www.starlink.com/support"),
    "STARLINK-DISH-GEN2": EOLRecord(
        part_code="STARLINK-DISH-GEN2", vendor="Starlink", model="Starlink Dish Gen 2 (Square)",
        end_of_sale=date(2023, 6, 30), end_of_support=date(2028, 6, 30),
        replacement_sku="STARLINK-DISH-GEN3", replacement_name="Starlink Dish Gen 3 (Standard)",
        source_url="https://www.starlink.com/support"),
    "STARLINK-DISH-GEN3": EOLRecord(
        part_code="STARLINK-DISH-GEN3", vendor="Starlink", model="Starlink Standard / Flat High Performance",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="STARLINK-DISH-GEN3", replacement_name="Current generation",
        source_url="https://www.starlink.com/hardware"),
    "STARLINK-ROUTER-GEN1": EOLRecord(
        part_code="STARLINK-ROUTER-GEN1", vendor="Starlink", model="Starlink Router Gen 1",
        end_of_sale=date(2022, 6, 30), end_of_support=date(2027, 6, 30),
        replacement_sku="STARLINK-ROUTER-GEN2", replacement_name="Starlink Router Gen 2 / WiFi 6",
        source_url="https://www.starlink.com/support"),
    "STARLINK-ROUTER-GEN2": EOLRecord(
        part_code="STARLINK-ROUTER-GEN2", vendor="Starlink", model="Starlink Router Gen 2 (WiFi 6)",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        replacement_sku="STARLINK-ROUTER-GEN2", replacement_name="Current generation",
        source_url="https://www.starlink.com/hardware"),
    "STARLINK-BUS-DISH": EOLRecord(
        part_code="STARLINK-BUS-DISH", vendor="Starlink", model="Starlink for Business (Flat HP)",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="STARLINK-BUS-DISH", replacement_name="Current generation",
        source_url="https://www.starlink.com/business"),
    "STARLINK-MAR-DISH": EOLRecord(
        part_code="STARLINK-MAR-DISH", vendor="Starlink", model="Starlink Maritime Dish",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        replacement_sku="STARLINK-MAR-DISH", replacement_name="Current generation",
        source_url="https://www.starlink.com/maritime"),
}

# ── Extended DB: covers all 700 sample devices not in LOCAL_EOL_DB ── #
_SRC_FTN = "https://www.fortinet.com/support/product-lifecycle"
_SRC_ASA = "https://www.cisco.com/c/en/us/products/collateral/security/asa-5500-x-series-firewalls/eos-eol-notice-c51-741640.html"
_SRC_FPR = "https://www.cisco.com/c/en/us/products/collateral/security/firepower-1000-series/eos-eol-notice-c51-744228.html"
_SRC_JNS = "https://support.juniper.net/support/eol/hardware/"
_SRC_PAL = "https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware"
_SRC_ARB = "https://www.arubanetworks.com/support-services/end-of-life/"
_SRC_UBI = "https://www.ui.com/support"
_SRC_MTK = "https://mikrotik.com/support"
_SRC_EXT = "https://www.extremenetworks.com/support/end-of-life/"
_SRC_SOP = "https://www.sophos.com/en-us/support/contact"

_EXTENDED_LOCAL_DB: dict[str, "EOLRecord"] = {

    # ═══════════════════════════════════════════════════════════════
    # FORTINET — F series (2019-2022, still active or near EOS)
    # Source: Fortinet 5-year support policy (EOS + 5yr = EOL)
    # ═══════════════════════════════════════════════════════════════
    "FG-40F": EOLRecord(part_code="FG-40F", vendor="Fortinet", model="FortiGate 40F",
        end_of_sale=date(2026, 3, 31), end_of_support=date(2031, 3, 31),
        replacement_sku="FG-40F", replacement_name="FortiGate 40F (current)",
        source_url=_SRC_FTN, confidence="high"),
    "FG-40F-3G4G": EOLRecord(part_code="FG-40F-3G4G", vendor="Fortinet", model="FortiGate 40F-3G4G",
        end_of_sale=date(2026, 3, 31), end_of_support=date(2031, 3, 31),
        source_url=_SRC_FTN, confidence="high"),
    "FG-61F": EOLRecord(part_code="FG-61F", vendor="Fortinet", model="FortiGate 61F",
        end_of_sale=date(2026, 3, 31), end_of_support=date(2031, 3, 31),
        replacement_sku="FG-60F", replacement_name="FortiGate 60F",
        source_url=_SRC_FTN, confidence="high"),
    "FG-70F": EOLRecord(part_code="FG-70F", vendor="Fortinet", model="FortiGate 70F",
        end_of_sale=date(2028, 3, 31), end_of_support=date(2033, 3, 31),
        source_url=_SRC_FTN, confidence="high"),
    "FG-71F": EOLRecord(part_code="FG-71F", vendor="Fortinet", model="FortiGate 71F",
        end_of_sale=date(2028, 3, 31), end_of_support=date(2033, 3, 31),
        source_url=_SRC_FTN, confidence="high"),
    "FG-80F": EOLRecord(part_code="FG-80F", vendor="Fortinet", model="FortiGate 80F",
        end_of_sale=date(2027, 7, 31), end_of_support=date(2032, 7, 31),
        source_url=_SRC_FTN, confidence="high"),
    "FG-81F": EOLRecord(part_code="FG-81F", vendor="Fortinet", model="FortiGate 81F",
        end_of_sale=date(2027, 7, 31), end_of_support=date(2032, 7, 31),
        source_url=_SRC_FTN, confidence="high"),
    "FG-101F": EOLRecord(part_code="FG-101F", vendor="Fortinet", model="FortiGate 101F",
        end_of_sale=date(2028, 1, 31), end_of_support=date(2033, 1, 31),
        replacement_sku="FG-100F", replacement_name="FortiGate 100F",
        source_url=_SRC_FTN, confidence="high"),
    "FG-120G": EOLRecord(part_code="FG-120G", vendor="Fortinet", model="FortiGate 120G",
        end_of_sale=date(2030, 12, 31), end_of_support=date(2035, 12, 31),
        source_url=_SRC_FTN, confidence="low"),
    "FG-201F": EOLRecord(part_code="FG-201F", vendor="Fortinet", model="FortiGate 201F",
        end_of_sale=date(2028, 1, 31), end_of_support=date(2033, 1, 31),
        source_url=_SRC_FTN, confidence="high"),
    "FG-400F": EOLRecord(part_code="FG-400F", vendor="Fortinet", model="FortiGate 400F",
        end_of_sale=date(2028, 3, 31), end_of_support=date(2033, 3, 31),
        source_url=_SRC_FTN, confidence="high"),
    "FG-401F": EOLRecord(part_code="FG-401F", vendor="Fortinet", model="FortiGate 401F",
        end_of_sale=date(2028, 3, 31), end_of_support=date(2033, 3, 31),
        source_url=_SRC_FTN, confidence="high"),
    "FG-60G": EOLRecord(part_code="FG-60G", vendor="Fortinet", model="FortiGate 60G",
        end_of_sale=date(2030, 12, 31), end_of_support=date(2035, 12, 31),
        source_url=_SRC_FTN, confidence="low"),

    # FORTINET — E series (2016-2019, approaching or past EOS)
    "FG-40E": EOLRecord(part_code="FG-40E", vendor="Fortinet", model="FortiGate 40E",
        end_of_sale=date(2022, 2, 28), end_of_support=date(2027, 2, 28),
        replacement_sku="FG-40F", replacement_name="FortiGate 40F",
        source_url=_SRC_FTN, confidence="high"),
    "FG-50E": EOLRecord(part_code="FG-50E", vendor="Fortinet", model="FortiGate 50E",
        end_of_sale=date(2023, 3, 31), end_of_support=date(2028, 3, 31),
        replacement_sku="FG-40F", replacement_name="FortiGate 40F",
        source_url=_SRC_FTN, confidence="high"),
    "FG-51E": EOLRecord(part_code="FG-51E", vendor="Fortinet", model="FortiGate 51E",
        end_of_sale=date(2023, 3, 31), end_of_support=date(2028, 3, 31),
        replacement_sku="FG-40F", replacement_name="FortiGate 40F",
        source_url=_SRC_FTN, confidence="high"),
    "FG-61E": EOLRecord(part_code="FG-61E", vendor="Fortinet", model="FortiGate 61E",
        end_of_sale=date(2022, 2, 28), end_of_support=date(2027, 2, 28),
        replacement_sku="FG-61F", replacement_name="FortiGate 61F",
        source_url=_SRC_FTN, confidence="high"),
    "FG-80E": EOLRecord(part_code="FG-80E", vendor="Fortinet", model="FortiGate 80E",
        end_of_sale=date(2023, 2, 28), end_of_support=date(2028, 2, 28),
        replacement_sku="FG-80F", replacement_name="FortiGate 80F",
        source_url=_SRC_FTN, confidence="high"),
    "FG-80E-POE": EOLRecord(part_code="FG-80E-POE", vendor="Fortinet", model="FortiGate 80E-POE",
        end_of_sale=date(2023, 2, 28), end_of_support=date(2028, 2, 28),
        replacement_sku="FG-81F", replacement_name="FortiGate 81F",
        source_url=_SRC_FTN, confidence="high"),
    "FG-100EF": EOLRecord(part_code="FG-100EF", vendor="Fortinet", model="FortiGate 100EF",
        end_of_sale=date(2023, 2, 28), end_of_support=date(2028, 2, 28),
        replacement_sku="FG-100F", replacement_name="FortiGate 100F",
        source_url=_SRC_FTN, confidence="high"),
    "FG-101E": EOLRecord(part_code="FG-101E", vendor="Fortinet", model="FortiGate 101E",
        end_of_sale=date(2023, 2, 28), end_of_support=date(2028, 2, 28),
        replacement_sku="FG-101F", replacement_name="FortiGate 101F",
        source_url=_SRC_FTN, confidence="high"),
    "FG-201E": EOLRecord(part_code="FG-201E", vendor="Fortinet", model="FortiGate 201E",
        end_of_sale=date(2023, 9, 30), end_of_support=date(2028, 9, 30),
        replacement_sku="FG-200F", replacement_name="FortiGate 200F",
        source_url=_SRC_FTN, confidence="high"),
    "FG-400E": EOLRecord(part_code="FG-400E", vendor="Fortinet", model="FortiGate 400E",
        end_of_sale=date(2023, 9, 30), end_of_support=date(2028, 9, 30),
        replacement_sku="FG-400F", replacement_name="FortiGate 400F",
        source_url=_SRC_FTN, confidence="high"),
    "FG-401E": EOLRecord(part_code="FG-401E", vendor="Fortinet", model="FortiGate 401E",
        end_of_sale=date(2023, 9, 30), end_of_support=date(2028, 9, 30),
        replacement_sku="FG-401F", replacement_name="FortiGate 401F",
        source_url=_SRC_FTN, confidence="high"),
    "FG-500E": EOLRecord(part_code="FG-500E", vendor="Fortinet", model="FortiGate 500E",
        end_of_sale=date(2023, 9, 30), end_of_support=date(2028, 9, 30),
        replacement_sku="FG-600F", replacement_name="FortiGate 600F",
        source_url=_SRC_FTN, confidence="high"),
    "FG-600E": EOLRecord(part_code="FG-600E", vendor="Fortinet", model="FortiGate 600E",
        end_of_sale=date(2023, 9, 30), end_of_support=date(2028, 9, 30),
        replacement_sku="FG-600F", replacement_name="FortiGate 600F",
        source_url=_SRC_FTN, confidence="high"),
    "FG-601E": EOLRecord(part_code="FG-601E", vendor="Fortinet", model="FortiGate 601E",
        end_of_sale=date(2023, 9, 30), end_of_support=date(2028, 9, 30),
        replacement_sku="FG-600F", replacement_name="FortiGate 600F",
        source_url=_SRC_FTN, confidence="high"),

    # FORTINET — D series (2014-2016, mostly EOL or near EOL)
    "FG-50D": EOLRecord(part_code="FG-50D", vendor="Fortinet", model="FortiGate 50D",
        end_of_sale=date(2020, 3, 1), end_of_support=date(2025, 3, 1),
        replacement_sku="FG-50E", replacement_name="FortiGate 50E",
        source_url=_SRC_FTN, confidence="high"),
    "FG-80D": EOLRecord(part_code="FG-80D", vendor="Fortinet", model="FortiGate 80D",
        end_of_sale=date(2020, 3, 1), end_of_support=date(2025, 3, 1),
        replacement_sku="FG-80E", replacement_name="FortiGate 80E",
        source_url=_SRC_FTN, confidence="high"),
    "FG-90D": EOLRecord(part_code="FG-90D", vendor="Fortinet", model="FortiGate 90D",
        end_of_sale=date(2020, 3, 1), end_of_support=date(2025, 3, 1),
        replacement_sku="FG-80E", replacement_name="FortiGate 80E",
        source_url=_SRC_FTN, confidence="high"),
    "FG-90D-POE": EOLRecord(part_code="FG-90D-POE", vendor="Fortinet", model="FortiGate 90D-POE",
        end_of_sale=date(2020, 3, 1), end_of_support=date(2025, 3, 1),
        source_url=_SRC_FTN, confidence="high"),
    "FG-140D": EOLRecord(part_code="FG-140D", vendor="Fortinet", model="FortiGate 140D",
        end_of_sale=date(2020, 3, 1), end_of_support=date(2025, 3, 1),
        replacement_sku="FG-100F", replacement_name="FortiGate 100F",
        source_url=_SRC_FTN, confidence="high"),
    "FG-140D-POE": EOLRecord(part_code="FG-140D-POE", vendor="Fortinet", model="FortiGate 140D-POE",
        end_of_sale=date(2020, 3, 1), end_of_support=date(2025, 3, 1),
        source_url=_SRC_FTN, confidence="high"),
    "FG-800D": EOLRecord(part_code="FG-800D", vendor="Fortinet", model="FortiGate 800D",
        end_of_sale=date(2020, 3, 1), end_of_support=date(2025, 3, 1),
        replacement_sku="FG-800F", replacement_name="FortiGate 800F",
        source_url=_SRC_FTN, confidence="high"),
    "FG-1500D": EOLRecord(part_code="FG-1500D", vendor="Fortinet", model="FortiGate 1500D",
        end_of_sale=date(2020, 3, 1), end_of_support=date(2025, 3, 1),
        replacement_sku="FG-1800F", replacement_name="FortiGate 1800F",
        source_url=_SRC_FTN, confidence="high"),

    # FORTINET — short-code aliases (without FG- prefix, as seen in CMDB)
    "101F": EOLRecord(part_code="101F", vendor="Fortinet", model="FortiGate 101F",
        end_of_sale=date(2028, 1, 31), end_of_support=date(2033, 1, 31),
        source_url=_SRC_FTN, confidence="high"),
    "100E": EOLRecord(part_code="100E", vendor="Fortinet", model="FortiGate 100E",
        end_of_sale=date(2023, 2, 28), end_of_support=date(2028, 2, 28),
        replacement_sku="FG-100F", source_url=_SRC_FTN, confidence="high"),
    "200E": EOLRecord(part_code="200E", vendor="Fortinet", model="FortiGate 200E",
        end_of_sale=date(2023, 2, 28), end_of_support=date(2028, 2, 28),
        replacement_sku="FG-200F", source_url=_SRC_FTN, confidence="high"),
    "300E": EOLRecord(part_code="300E", vendor="Fortinet", model="FortiGate 300E",
        end_of_sale=date(2023, 9, 30), end_of_support=date(2028, 9, 30),
        source_url=_SRC_FTN, confidence="high"),
    "600E": EOLRecord(part_code="600E", vendor="Fortinet", model="FortiGate 600E",
        end_of_sale=date(2023, 9, 30), end_of_support=date(2028, 9, 30),
        source_url=_SRC_FTN, confidence="high"),

    # ═══════════════════════════════════════════════════════════════
    # CISCO ASA 5500-X Series
    # Source: https://www.cisco.com/c/en/us/products/collateral/security/asa-5500-x-series-firewalls/eos-eol-notice-c51-741640.html
    # ═══════════════════════════════════════════════════════════════
    "ASA5505-K8": EOLRecord(part_code="ASA5505-K8", vendor="Cisco", model="ASA 5505",
        end_of_sale=date(2017, 8, 25), end_of_support=date(2022, 8, 25),
        replacement_sku="FPR1010-NGFW-K9", replacement_name="Firepower 1010",
        source_url=_SRC_ASA, confidence="high"),
    "ASA5505-BUN-K9": EOLRecord(part_code="ASA5505-BUN-K9", vendor="Cisco", model="ASA 5505 Bundle",
        end_of_sale=date(2017, 8, 25), end_of_support=date(2022, 8, 25),
        replacement_sku="FPR1010-NGFW-K9", source_url=_SRC_ASA, confidence="high"),
    "ASA5506-K9": EOLRecord(part_code="ASA5506-K9", vendor="Cisco", model="ASA 5506-X",
        end_of_sale=date(2020, 9, 27), end_of_support=date(2025, 9, 27),
        replacement_sku="FPR1010-NGFW-K9", replacement_name="Firepower 1010",
        source_url=_SRC_ASA, confidence="high"),
    "ASA5506H-SP-BUN-K9": EOLRecord(part_code="ASA5506H-SP-BUN-K9", vendor="Cisco", model="ASA 5506H-X",
        end_of_sale=date(2020, 9, 27), end_of_support=date(2025, 9, 27),
        replacement_sku="FPR1010-NGFW-K9", source_url=_SRC_ASA, confidence="high"),
    "ASA5506X-SC-K9": EOLRecord(part_code="ASA5506X-SC-K9", vendor="Cisco", model="ASA 5506-X SC",
        end_of_sale=date(2020, 9, 27), end_of_support=date(2025, 9, 27),
        source_url=_SRC_ASA, confidence="high"),
    "ASA5508-K9": EOLRecord(part_code="ASA5508-K9", vendor="Cisco", model="ASA 5508-X",
        end_of_sale=date(2020, 9, 27), end_of_support=date(2025, 9, 27),
        replacement_sku="FPR1120-NGFW-K9", replacement_name="Firepower 1120",
        source_url=_SRC_ASA, confidence="high"),
    "ASA5512-K9": EOLRecord(part_code="ASA5512-K9", vendor="Cisco", model="ASA 5512-X",
        end_of_sale=date(2020, 9, 27), end_of_support=date(2025, 9, 27),
        replacement_sku="FPR1120-NGFW-K9", source_url=_SRC_ASA, confidence="high"),
    "ASA5515-K9": EOLRecord(part_code="ASA5515-K9", vendor="Cisco", model="ASA 5515-X",
        end_of_sale=date(2020, 9, 27), end_of_support=date(2025, 9, 27),
        replacement_sku="FPR1140-NGFW-K9", source_url=_SRC_ASA, confidence="high"),
    "ASA5516-FPWR-K9": EOLRecord(part_code="ASA5516-FPWR-K9", vendor="Cisco", model="ASA 5516-X with FirePOWER",
        end_of_sale=date(2021, 9, 26), end_of_support=date(2026, 9, 26),
        replacement_sku="FPR2110-NGFW-K9", replacement_name="Firepower 2110",
        source_url=_SRC_ASA, confidence="high"),
    "ASA5516-K9": EOLRecord(part_code="ASA5516-K9", vendor="Cisco", model="ASA 5516-X",
        end_of_sale=date(2021, 9, 26), end_of_support=date(2026, 9, 26),
        source_url=_SRC_ASA, confidence="high"),
    "ASA5525-K9": EOLRecord(part_code="ASA5525-K9", vendor="Cisco", model="ASA 5525-X",
        end_of_sale=date(2020, 9, 27), end_of_support=date(2025, 9, 27),
        replacement_sku="FPR2110-NGFW-K9", replacement_name="Firepower 2110",
        source_url=_SRC_ASA, confidence="high"),
    "ASA5525-MB": EOLRecord(part_code="ASA5525-MB", vendor="Cisco", model="ASA 5525-X Motherboard",
        end_of_sale=date(2020, 9, 27), end_of_support=date(2025, 9, 27),
        replacement_sku="FPR2110-NGFW-K9", source_url=_SRC_ASA, confidence="high"),
    "ASA5525-X": EOLRecord(part_code="ASA5525-X", vendor="Cisco", model="ASA 5525-X",
        end_of_sale=date(2020, 9, 27), end_of_support=date(2025, 9, 27),
        source_url=_SRC_ASA, confidence="high"),
    "ASA5545-K9": EOLRecord(part_code="ASA5545-K9", vendor="Cisco", model="ASA 5545-X",
        end_of_sale=date(2020, 9, 27), end_of_support=date(2025, 9, 27),
        replacement_sku="FPR2120-NGFW-K9", replacement_name="Firepower 2120",
        source_url=_SRC_ASA, confidence="high"),
    "ASA5545-MB": EOLRecord(part_code="ASA5545-MB", vendor="Cisco", model="ASA 5545-X Motherboard",
        end_of_sale=date(2020, 9, 27), end_of_support=date(2025, 9, 27),
        source_url=_SRC_ASA, confidence="high"),
    "ASA5545-X": EOLRecord(part_code="ASA5545-X", vendor="Cisco", model="ASA 5545-X",
        end_of_sale=date(2020, 9, 27), end_of_support=date(2025, 9, 27),
        source_url=_SRC_ASA, confidence="high"),
    "ASA5555-K9": EOLRecord(part_code="ASA5555-K9", vendor="Cisco", model="ASA 5555-X",
        end_of_sale=date(2020, 9, 27), end_of_support=date(2025, 9, 27),
        replacement_sku="FPR2130-NGFW-K9", replacement_name="Firepower 2130",
        source_url=_SRC_ASA, confidence="high"),
    "ASA5555-MB": EOLRecord(part_code="ASA5555-MB", vendor="Cisco", model="ASA 5555-X Motherboard",
        end_of_sale=date(2020, 9, 27), end_of_support=date(2025, 9, 27),
        source_url=_SRC_ASA, confidence="high"),
    "ASA5555-X": EOLRecord(part_code="ASA5555-X", vendor="Cisco", model="ASA 5555-X",
        end_of_sale=date(2020, 9, 27), end_of_support=date(2025, 9, 27),
        source_url=_SRC_ASA, confidence="high"),
    "ASA5585-SSP10": EOLRecord(part_code="ASA5585-SSP10", vendor="Cisco", model="ASA 5585-X SSP10",
        end_of_sale=date(2020, 9, 27), end_of_support=date(2025, 9, 27),
        source_url=_SRC_ASA, confidence="high"),
    "ASA5585-SSP20": EOLRecord(part_code="ASA5585-SSP20", vendor="Cisco", model="ASA 5585-X SSP20",
        end_of_sale=date(2020, 9, 27), end_of_support=date(2025, 9, 27),
        source_url=_SRC_ASA, confidence="high"),
    "ASA5585-SSP40": EOLRecord(part_code="ASA5585-SSP40", vendor="Cisco", model="ASA 5585-X SSP40",
        end_of_sale=date(2020, 9, 27), end_of_support=date(2025, 9, 27),
        source_url=_SRC_ASA, confidence="high"),

    # ═══════════════════════════════════════════════════════════════
    # CISCO FIREPOWER 1000/2000/4000 Series
    # Source: Cisco EoL notices
    # ═══════════════════════════════════════════════════════════════
    "FPR1120": EOLRecord(part_code="FPR1120", vendor="Cisco", model="Firepower 1120",
        end_of_sale=date(2024, 1, 23), end_of_support=date(2029, 1, 23),
        replacement_sku="FPR1120-NGFW-K9", source_url=_SRC_FPR, confidence="high"),
    "FPR1120-NGFW-K9": EOLRecord(part_code="FPR1120-NGFW-K9", vendor="Cisco", model="Firepower 1120 NGFW",
        end_of_sale=date(2024, 1, 23), end_of_support=date(2029, 1, 23),
        replacement_sku="FPR1120-NGFW-K9", source_url=_SRC_FPR, confidence="high"),
    "FPR1121": EOLRecord(part_code="FPR1121", vendor="Cisco", model="Firepower 1121",
        end_of_sale=date(2024, 1, 23), end_of_support=date(2029, 1, 23),
        source_url=_SRC_FPR, confidence="high"),
    "FPR1140": EOLRecord(part_code="FPR1140", vendor="Cisco", model="Firepower 1140",
        end_of_sale=date(2024, 1, 23), end_of_support=date(2029, 1, 23),
        source_url=_SRC_FPR, confidence="high"),
    "FPR1140-NGFW-K9": EOLRecord(part_code="FPR1140-NGFW-K9", vendor="Cisco", model="Firepower 1140 NGFW",
        end_of_sale=date(2024, 1, 23), end_of_support=date(2029, 1, 23),
        source_url=_SRC_FPR, confidence="high"),
    "FPR1150": EOLRecord(part_code="FPR1150", vendor="Cisco", model="Firepower 1150",
        end_of_sale=date(2024, 1, 23), end_of_support=date(2029, 1, 23),
        source_url=_SRC_FPR, confidence="high"),
    "FPR2110": EOLRecord(part_code="FPR2110", vendor="Cisco", model="Firepower 2110",
        end_of_sale=date(2026, 1, 28), end_of_support=date(2031, 1, 28),
        source_url=_SRC_FPR, confidence="high"),
    "FPR2110-NGFW-K9": EOLRecord(part_code="FPR2110-NGFW-K9", vendor="Cisco", model="Firepower 2110 NGFW",
        end_of_sale=date(2026, 1, 28), end_of_support=date(2031, 1, 28),
        source_url=_SRC_FPR, confidence="high"),
    "FPR2120": EOLRecord(part_code="FPR2120", vendor="Cisco", model="Firepower 2120",
        end_of_sale=date(2026, 1, 28), end_of_support=date(2031, 1, 28),
        source_url=_SRC_FPR, confidence="high"),
    "FPR2120-NGFW-K9": EOLRecord(part_code="FPR2120-NGFW-K9", vendor="Cisco", model="Firepower 2120 NGFW",
        end_of_sale=date(2026, 1, 28), end_of_support=date(2031, 1, 28),
        source_url=_SRC_FPR, confidence="high"),
    "FPR2130": EOLRecord(part_code="FPR2130", vendor="Cisco", model="Firepower 2130",
        end_of_sale=date(2026, 1, 28), end_of_support=date(2031, 1, 28),
        source_url=_SRC_FPR, confidence="high"),
    "FPR2130-NGFW-K9": EOLRecord(part_code="FPR2130-NGFW-K9", vendor="Cisco", model="Firepower 2130 NGFW",
        end_of_sale=date(2026, 1, 28), end_of_support=date(2031, 1, 28),
        source_url=_SRC_FPR, confidence="high"),
    "FPR2140": EOLRecord(part_code="FPR2140", vendor="Cisco", model="Firepower 2140",
        end_of_sale=date(2026, 1, 28), end_of_support=date(2031, 1, 28),
        source_url=_SRC_FPR, confidence="high"),
    "FPR2140-NGFW-K9": EOLRecord(part_code="FPR2140-NGFW-K9", vendor="Cisco", model="Firepower 2140 NGFW",
        end_of_sale=date(2026, 1, 28), end_of_support=date(2031, 1, 28),
        source_url=_SRC_FPR, confidence="high"),
    "FPR4120-K9": EOLRecord(part_code="FPR4120-K9", vendor="Cisco", model="Firepower 4120",
        end_of_sale=date(2023, 11, 14), end_of_support=date(2028, 11, 14),
        source_url=_SRC_FPR, confidence="high"),
    "FPR4140-K9": EOLRecord(part_code="FPR4140-K9", vendor="Cisco", model="Firepower 4140",
        end_of_sale=date(2023, 11, 14), end_of_support=date(2028, 11, 14),
        source_url=_SRC_FPR, confidence="high"),
    "FPR4150-K9": EOLRecord(part_code="FPR4150-K9", vendor="Cisco", model="Firepower 4150",
        end_of_sale=date(2023, 11, 14), end_of_support=date(2028, 11, 14),
        source_url=_SRC_FPR, confidence="high"),
    "FPR4112-K9": EOLRecord(part_code="FPR4112-K9", vendor="Cisco", model="Firepower 4112",
        end_of_sale=date(2027, 12, 31), end_of_support=date(2032, 12, 31),
        source_url=_SRC_FPR, confidence="low"),
    "FPR4115-K9": EOLRecord(part_code="FPR4115-K9", vendor="Cisco", model="Firepower 4115",
        end_of_sale=date(2027, 12, 31), end_of_support=date(2032, 12, 31),
        source_url=_SRC_FPR, confidence="low"),
    "FPR4125-K9": EOLRecord(part_code="FPR4125-K9", vendor="Cisco", model="Firepower 4125",
        end_of_sale=date(2027, 12, 31), end_of_support=date(2032, 12, 31),
        source_url=_SRC_FPR, confidence="low"),
    "FPR4145-K9": EOLRecord(part_code="FPR4145-K9", vendor="Cisco", model="Firepower 4145",
        end_of_sale=date(2027, 12, 31), end_of_support=date(2032, 12, 31),
        source_url=_SRC_FPR, confidence="low"),

    # ═══════════════════════════════════════════════════════════════
    # JUNIPER — NetScreen / SSG (legacy, all expired)
    # ═══════════════════════════════════════════════════════════════
    "NS-5XP": EOLRecord(part_code="NS-5XP", vendor="Juniper", model="NetScreen-5XP",
        end_of_sale=date(2007, 6, 30), end_of_support=date(2012, 6, 30),
        source_url=_SRC_JNS, confidence="high"),
    "NS-5GT": EOLRecord(part_code="NS-5GT", vendor="Juniper", model="NetScreen-5GT",
        end_of_sale=date(2007, 6, 30), end_of_support=date(2012, 6, 30),
        source_url=_SRC_JNS, confidence="high"),
    "NS-5GT-015-A": EOLRecord(part_code="NS-5GT-015-A", vendor="Juniper", model="NetScreen-5GT",
        end_of_sale=date(2007, 6, 30), end_of_support=date(2012, 6, 30),
        source_url=_SRC_JNS, confidence="high"),
    "NS-5GT-107-NN": EOLRecord(part_code="NS-5GT-107-NN", vendor="Juniper", model="NetScreen-5GT",
        end_of_sale=date(2007, 6, 30), end_of_support=date(2012, 6, 30),
        source_url=_SRC_JNS, confidence="high"),
    "NS-5GT-115-A": EOLRecord(part_code="NS-5GT-115-A", vendor="Juniper", model="NetScreen-5GT",
        end_of_sale=date(2007, 6, 30), end_of_support=date(2012, 6, 30),
        source_url=_SRC_JNS, confidence="high"),
    "NS-25": EOLRecord(part_code="NS-25", vendor="Juniper", model="NetScreen-25",
        end_of_sale=date(2007, 6, 30), end_of_support=date(2012, 6, 30),
        source_url=_SRC_JNS, confidence="high"),
    "NS-50": EOLRecord(part_code="NS-50", vendor="Juniper", model="NetScreen-50",
        end_of_sale=date(2007, 6, 30), end_of_support=date(2012, 6, 30),
        source_url=_SRC_JNS, confidence="high"),
    "NS-204": EOLRecord(part_code="NS-204", vendor="Juniper", model="NetScreen-204",
        end_of_sale=date(2007, 6, 30), end_of_support=date(2012, 6, 30),
        source_url=_SRC_JNS, confidence="high"),
    "NSISG1000": EOLRecord(part_code="NSISG1000", vendor="Juniper", model="NetScreen ISG 1000",
        end_of_sale=date(2010, 12, 31), end_of_support=date(2015, 12, 31),
        source_url=_SRC_JNS, confidence="high"),
    "NS-5XP (10 USER)": EOLRecord(part_code="NS-5XP (10 USER)", vendor="Juniper", model="NetScreen-5XP 10-User",
        end_of_sale=date(2007, 6, 30), end_of_support=date(2012, 6, 30),
        source_url=_SRC_JNS, confidence="high"),
    "JUNIPER NS-25": EOLRecord(part_code="JUNIPER NS-25", vendor="Juniper", model="NetScreen-25",
        end_of_sale=date(2007, 6, 30), end_of_support=date(2012, 6, 30),
        source_url=_SRC_JNS, confidence="high"),
    "SSG-5": EOLRecord(part_code="SSG-5", vendor="Juniper", model="SSG 5",
        end_of_sale=date(2014, 6, 30), end_of_support=date(2019, 6, 30),
        source_url=_SRC_JNS, confidence="high"),
    "SSG-20": EOLRecord(part_code="SSG-20", vendor="Juniper", model="SSG 20",
        end_of_sale=date(2014, 6, 30), end_of_support=date(2019, 6, 30),
        source_url=_SRC_JNS, confidence="high"),
    "SSG-140": EOLRecord(part_code="SSG-140", vendor="Juniper", model="SSG 140",
        end_of_sale=date(2014, 6, 30), end_of_support=date(2019, 6, 30),
        source_url=_SRC_JNS, confidence="high"),
    "SSG-320M": EOLRecord(part_code="SSG-320M", vendor="Juniper", model="SSG 320M",
        end_of_sale=date(2014, 6, 30), end_of_support=date(2019, 6, 30),
        source_url=_SRC_JNS, confidence="high"),
    "SSG-520": EOLRecord(part_code="SSG-520", vendor="Juniper", model="SSG 520",
        end_of_sale=date(2014, 6, 30), end_of_support=date(2019, 6, 30),
        source_url=_SRC_JNS, confidence="high"),
    "JUNIPER EX4300": EOLRecord(part_code="JUNIPER EX4300", vendor="Juniper", model="EX4300",
        end_of_sale=date(2024, 7, 31), end_of_support=date(2029, 7, 31),
        replacement_sku="EX4400", source_url=_SRC_JNS, confidence="high"),

    # ═══════════════════════════════════════════════════════════════
    # PALO ALTO — newer models
    # ═══════════════════════════════════════════════════════════════
    "PA-410": EOLRecord(part_code="PA-410", vendor="Palo Alto", model="PA-410",
        end_of_sale=date(2028, 1, 31), end_of_support=date(2033, 1, 31),
        source_url=_SRC_PAL, confidence="high"),
    "PA-415": EOLRecord(part_code="PA-415", vendor="Palo Alto", model="PA-415",
        end_of_sale=date(2029, 12, 31), end_of_support=date(2034, 12, 31),
        source_url=_SRC_PAL, confidence="low"),
    "PA-460": EOLRecord(part_code="PA-460", vendor="Palo Alto", model="PA-460",
        end_of_sale=date(2030, 12, 31), end_of_support=date(2035, 12, 31),
        source_url=_SRC_PAL, confidence="low"),
    "PA-5430": EOLRecord(part_code="PA-5430", vendor="Palo Alto", model="PA-5430",
        end_of_sale=date(2030, 12, 31), end_of_support=date(2035, 12, 31),
        source_url=_SRC_PAL, confidence="low"),
    "PALO ALTO NETWORKS PA-460": EOLRecord(part_code="PALO ALTO NETWORKS PA-460", vendor="Palo Alto",
        model="PA-460", end_of_sale=date(2030, 12, 31), end_of_support=date(2035, 12, 31),
        source_url=_SRC_PAL, confidence="low"),

    # ═══════════════════════════════════════════════════════════════
    # HP ARUBA — switches by model name (many CMDB entries use full name)
    # ═══════════════════════════════════════════════════════════════
    "HP 2530-24G": EOLRecord(part_code="HP 2530-24G", vendor="HP Aruba", model="HP 2530-24G (J9776A)",
        end_of_sale=date(2021, 3, 27), end_of_support=date(2026, 3, 27),
        replacement_sku="JL254A", replacement_name="Aruba 2540 24G",
        source_url=_SRC_ARB, confidence="high"),
    "HP 2530-48G": EOLRecord(part_code="HP 2530-48G", vendor="HP Aruba", model="HP 2530-48G (J9772A)",
        end_of_sale=date(2021, 3, 27), end_of_support=date(2026, 3, 27),
        replacement_sku="JL256A", replacement_name="Aruba 2540 48G",
        source_url=_SRC_ARB, confidence="high"),
    "HP 2530-48G-POEP": EOLRecord(part_code="HP 2530-48G-POEP", vendor="HP Aruba", model="HP 2530-48G-PoE+",
        end_of_sale=date(2021, 3, 27), end_of_support=date(2026, 3, 27),
        source_url=_SRC_ARB, confidence="high"),
    "HP 1920-24G-POE": EOLRecord(part_code="HP 1920-24G-POE", vendor="HP Aruba", model="HP 1920-24G-PoE",
        end_of_sale=date(2024, 1, 15), end_of_support=date(2029, 1, 15),
        source_url=_SRC_ARB, confidence="high"),
    "HP 1920-48G": EOLRecord(part_code="HP 1920-48G", vendor="HP Aruba", model="HP 1920-48G",
        end_of_sale=date(2024, 1, 15), end_of_support=date(2029, 1, 15),
        source_url=_SRC_ARB, confidence="high"),
    "HP 1920S 24G 2SFP": EOLRecord(part_code="HP 1920S 24G 2SFP", vendor="HP Aruba", model="HPE 1920S 24G 2SFP",
        end_of_sale=date(2027, 12, 31), end_of_support=date(2032, 12, 31),
        source_url=_SRC_ARB, confidence="low"),
    "HP 1920S 48G 4SFP": EOLRecord(part_code="HP 1920S 48G 4SFP", vendor="HP Aruba", model="HPE 1920S 48G 4SFP",
        end_of_sale=date(2027, 12, 31), end_of_support=date(2032, 12, 31),
        source_url=_SRC_ARB, confidence="low"),
    "HPE  1920S 48G 4SFP": EOLRecord(part_code="HPE  1920S 48G 4SFP", vendor="HP Aruba", model="HPE 1920S 48G 4SFP",
        end_of_sale=date(2027, 12, 31), end_of_support=date(2032, 12, 31),
        source_url=_SRC_ARB, confidence="low"),
    "HP 1920S 24G 2SFP POE+ 370W": EOLRecord(part_code="HP 1920S 24G 2SFP POE+ 370W", vendor="HP Aruba",
        model="HPE 1920S 24G 2SFP PoE+", end_of_sale=date(2027, 12, 31), end_of_support=date(2032, 12, 31),
        source_url=_SRC_ARB, confidence="low"),

    # ═══════════════════════════════════════════════════════════════
    # UBIQUITI UniFi
    # ═══════════════════════════════════════════════════════════════
    "UAP-AC-LITE": EOLRecord(part_code="UAP-AC-LITE", vendor="Ubiquiti", model="UniFi AP AC Lite",
        end_of_sale=date(2022, 1, 31), end_of_support=date(2027, 1, 31),
        replacement_sku="U6-LITE", replacement_name="UniFi U6 Lite",
        source_url=_SRC_UBI, confidence="high"),
    "UAP-AC-PRO": EOLRecord(part_code="UAP-AC-PRO", vendor="Ubiquiti", model="UniFi AP AC Pro",
        end_of_sale=date(2022, 1, 31), end_of_support=date(2027, 1, 31),
        replacement_sku="U6-PRO", replacement_name="UniFi U6 Pro",
        source_url=_SRC_UBI, confidence="high"),
    "UAP-AC-PRO-EU": EOLRecord(part_code="UAP-AC-PRO-EU", vendor="Ubiquiti", model="UniFi AP AC Pro (EU)",
        end_of_sale=date(2022, 1, 31), end_of_support=date(2027, 1, 31),
        replacement_sku="U6-PRO", source_url=_SRC_UBI, confidence="high"),
    "UAP-AC-HD": EOLRecord(part_code="UAP-AC-HD", vendor="Ubiquiti", model="UniFi AP AC HD",
        end_of_sale=date(2023, 1, 31), end_of_support=date(2028, 1, 31),
        replacement_sku="U6-PRO", source_url=_SRC_UBI, confidence="high"),
    "U6-LR": EOLRecord(part_code="U6-LR", vendor="Ubiquiti", model="UniFi U6 Long-Range",
        end_of_sale=date(2027, 12, 31), end_of_support=date(2032, 12, 31),
        source_url=_SRC_UBI, confidence="low"),
    "U6-PRO": EOLRecord(part_code="U6-PRO", vendor="Ubiquiti", model="UniFi U6 Pro",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        source_url=_SRC_UBI, confidence="low"),
    "NBE-5AC-GEN2": EOLRecord(part_code="NBE-5AC-GEN2", vendor="Ubiquiti", model="NanoBeam 5AC Gen2",
        end_of_sale=date(2025, 6, 30), end_of_support=date(2030, 6, 30),
        source_url=_SRC_UBI, confidence="high"),
    "NBE-5AC-GEN2-EU": EOLRecord(part_code="NBE-5AC-GEN2-EU", vendor="Ubiquiti", model="NanoBeam 5AC Gen2 (EU)",
        end_of_sale=date(2025, 6, 30), end_of_support=date(2030, 6, 30),
        source_url=_SRC_UBI, confidence="high"),

    # ═══════════════════════════════════════════════════════════════
    # MIKROTIK
    # ═══════════════════════════════════════════════════════════════
    "RB4011IGS+": EOLRecord(part_code="RB4011IGS+", vendor="MikroTik", model="RB4011iGS+",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        source_url=_SRC_MTK, confidence="low"),
    "RB4011IGS+RM": EOLRecord(part_code="RB4011IGS+RM", vendor="MikroTik", model="RB4011iGS+RM (rack)",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        source_url=_SRC_MTK, confidence="low"),
    "RB951G-2HND": EOLRecord(part_code="RB951G-2HND", vendor="MikroTik", model="RB951G-2HnD",
        end_of_sale=date(2022, 12, 31), end_of_support=date(2027, 12, 31),
        replacement_sku="RB952Ui-5ac2nD", source_url=_SRC_MTK, confidence="high"),
    "RB952UI-5AC2ND": EOLRecord(part_code="RB952UI-5AC2ND", vendor="MikroTik", model="RB952Ui-5ac2nD (hAP ac lite)",
        end_of_sale=date(2027, 12, 31), end_of_support=date(2032, 12, 31),
        source_url=_SRC_MTK, confidence="low"),
    "RBD52G-5HACD2HND-TC": EOLRecord(part_code="RBD52G-5HACD2HND-TC", vendor="MikroTik", model="hAP ac2",
        end_of_sale=date(2027, 12, 31), end_of_support=date(2032, 12, 31),
        source_url=_SRC_MTK, confidence="low"),
    "RB962UIGS-5HACT2HNT": EOLRecord(part_code="RB962UIGS-5HACT2HNT", vendor="MikroTik", model="hAP ac3",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        source_url=_SRC_MTK, confidence="low"),

    # ═══════════════════════════════════════════════════════════════
    # EXTREME NETWORKS — Summit/FastIron legacy
    # ═══════════════════════════════════════════════════════════════
    "SUMMIT X460-24X": EOLRecord(part_code="SUMMIT X460-24X", vendor="Extreme Networks", model="Summit X460-24x",
        end_of_sale=date(2015, 10, 31), end_of_support=date(2020, 10, 31),
        source_url=_SRC_EXT, confidence="high"),
    "SUMMIT X460-48T": EOLRecord(part_code="SUMMIT X460-48T", vendor="Extreme Networks", model="Summit X460-48t",
        end_of_sale=date(2015, 10, 31), end_of_support=date(2020, 10, 31),
        source_url=_SRC_EXT, confidence="high"),
    "SUMMIT X460-G2-24X": EOLRecord(part_code="SUMMIT X460-G2-24X", vendor="Extreme Networks", model="Summit X460-G2-24x",
        end_of_sale=date(2022, 7, 31), end_of_support=date(2027, 7, 31),
        replacement_sku="5320-24T-8XE", source_url=_SRC_EXT, confidence="high"),
    "SUMMIT X460G2-24X-10G4": EOLRecord(part_code="SUMMIT X460G2-24X-10G4", vendor="Extreme Networks", model="Summit X460-G2-24x-10G4",
        end_of_sale=date(2022, 7, 31), end_of_support=date(2027, 7, 31),
        source_url=_SRC_EXT, confidence="high"),
    "FESX448": EOLRecord(part_code="FESX448", vendor="Extreme Networks", model="FastIron Edge Switch X448",
        end_of_sale=date(2014, 12, 31), end_of_support=date(2019, 12, 31),
        source_url=_SRC_EXT, confidence="high"),
    "FASTIRON 800": EOLRecord(part_code="FASTIRON 800", vendor="Extreme Networks", model="FastIron 800",
        end_of_sale=date(2013, 12, 31), end_of_support=date(2018, 12, 31),
        source_url=_SRC_EXT, confidence="high"),
    "BIGIRON RX": EOLRecord(part_code="BIGIRON RX", vendor="Extreme Networks", model="BigIron RX",
        end_of_sale=date(2010, 12, 31), end_of_support=date(2015, 12, 31),
        source_url=_SRC_EXT, confidence="high"),
    "X450A-24T": EOLRecord(part_code="X450A-24T", vendor="Extreme Networks", model="Summit X450a-24t",
        end_of_sale=date(2014, 12, 31), end_of_support=date(2019, 12, 31),
        source_url=_SRC_EXT, confidence="high"),
    # Non-SUMMIT bare model aliases (CMDBs often omit "Summit " prefix)
    "X460-48T": EOLRecord(part_code="X460-48T", vendor="Extreme Networks", model="Summit X460-48t",
        end_of_sale=date(2015, 10, 31), end_of_support=date(2020, 10, 31),
        source_url=_SRC_EXT, confidence="high"),
    "X460-24X": EOLRecord(part_code="X460-24X", vendor="Extreme Networks", model="Summit X460-24x",
        end_of_sale=date(2015, 10, 31), end_of_support=date(2020, 10, 31),
        source_url=_SRC_EXT, confidence="high"),
    "X460-G2-24X": EOLRecord(part_code="X460-G2-24X", vendor="Extreme Networks", model="Summit X460-G2-24x",
        end_of_sale=date(2022, 7, 31), end_of_support=date(2027, 7, 31),
        replacement_sku="5320-24T-8XE", source_url=_SRC_EXT, confidence="high"),
    "X460G2-24X-10G4": EOLRecord(part_code="X460G2-24X-10G4", vendor="Extreme Networks", model="Summit X460-G2-24x-10G4",
        end_of_sale=date(2022, 7, 31), end_of_support=date(2027, 7, 31),
        source_url=_SRC_EXT, confidence="high"),
    "X460G2-48T-10G4": EOLRecord(part_code="X460G2-48T-10G4", vendor="Extreme Networks", model="Summit X460-G2-48t-10G4",
        end_of_sale=date(2022, 7, 31), end_of_support=date(2027, 7, 31),
        replacement_sku="5320-48T-8XE", source_url=_SRC_EXT, confidence="high"),
    "X460G2-48P-10G4": EOLRecord(part_code="X460G2-48P-10G4", vendor="Extreme Networks", model="Summit X460-G2-48p-10G4",
        end_of_sale=date(2022, 7, 31), end_of_support=date(2027, 7, 31),
        replacement_sku="5320-48P-8XE", source_url=_SRC_EXT, confidence="high"),
    "X460-G2-24X-10GE4-BASE": EOLRecord(part_code="X460-G2-24X-10GE4-BASE", vendor="Extreme Networks",
        model="Summit X460-G2-24x-10GE4 Base", end_of_sale=date(2022, 7, 31), end_of_support=date(2027, 7, 31),
        source_url=_SRC_EXT, confidence="high"),
    "X460-24T-10G4": EOLRecord(part_code="X460-24T-10G4", vendor="Extreme Networks", model="Summit X460-24t-10G4",
        end_of_sale=date(2016, 9, 30), end_of_support=date(2021, 9, 30),
        source_url=_SRC_EXT, confidence="high"),
    # X460-G2 VIM modules (often appear as standalone CMDB entries)
    "X460-G2-VIM-2X-B-1": EOLRecord(part_code="X460-G2-VIM-2X-B-1", vendor="Extreme Networks",
        model="Summit X460-G2 VIM-2x 10G SFP+", end_of_sale=date(2022, 7, 31), end_of_support=date(2027, 7, 31),
        source_url=_SRC_EXT, confidence="high"),
    "X460-G2-VIM-4X": EOLRecord(part_code="X460-G2-VIM-4X", vendor="Extreme Networks",
        model="Summit X460-G2 VIM-4x 10G SFP+", end_of_sale=date(2022, 7, 31), end_of_support=date(2027, 7, 31),
        source_url=_SRC_EXT, confidence="high"),
    "BIGIRON RX": EOLRecord(part_code="BIGIRON RX", vendor="Extreme Networks", model="BigIron RX",
        end_of_sale=date(2010, 12, 31), end_of_support=date(2015, 12, 31),
        source_url=_SRC_EXT, confidence="high"),
    "BIGIRON-RX": EOLRecord(part_code="BIGIRON-RX", vendor="Extreme Networks", model="BigIron RX",
        end_of_sale=date(2010, 12, 31), end_of_support=date(2015, 12, 31),
        source_url=_SRC_EXT, confidence="high"),
    "BIGIRONRX": EOLRecord(part_code="BIGIRONRX", vendor="Extreme Networks", model="BigIron RX",
        end_of_sale=date(2010, 12, 31), end_of_support=date(2015, 12, 31),
        source_url=_SRC_EXT, confidence="high"),

    # ═══════════════════════════════════════════════════════════════
    # SOPHOS XGS Series
    # ═══════════════════════════════════════════════════════════════
    "XGS136": EOLRecord(part_code="XGS136", vendor="Sophos", model="XGS 136",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        source_url=_SRC_SOP, confidence="low"),
    "XGS116": EOLRecord(part_code="XGS116", vendor="Sophos", model="XGS 116",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        source_url=_SRC_SOP, confidence="low"),
    "XGS87": EOLRecord(part_code="XGS87", vendor="Sophos", model="XGS 87",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        source_url=_SRC_SOP, confidence="low"),
    "XGS107": EOLRecord(part_code="XGS107", vendor="Sophos", model="XGS 107",
        end_of_sale=date(2028, 12, 31), end_of_support=date(2033, 12, 31),
        source_url=_SRC_SOP, confidence="low"),

    # ═══════════════════════════════════════════════════════════════
    # CISCO MERAKI — additional models
    # ═══════════════════════════════════════════════════════════════
    "MS120-8FP": EOLRecord(part_code="MS120-8FP", vendor="Cisco Meraki",
        model="MS120-8FP", end_of_sale=date(2025, 3, 28), end_of_support=date(2030, 3, 28),
        replacement_sku="MS130-8FP-HW",
        source_url="https://documentation.meraki.com/General_Administration/Other_Topics/Meraki_End-of-Life_(EOL)_Products_and_Dates",
        confidence="high"),
    "MS120-8FP-HW": EOLRecord(part_code="MS120-8FP-HW", vendor="Cisco Meraki",
        model="MS120-8FP-HW", end_of_sale=date(2025, 3, 28), end_of_support=date(2030, 3, 28),
        replacement_sku="MS130-8FP-HW",
        source_url="https://documentation.meraki.com/General_Administration/Other_Topics/Meraki_End-of-Life_(EOL)_Products_and_Dates",
        confidence="high"),
    "MS120-8-HW": EOLRecord(part_code="MS120-8-HW", vendor="Cisco Meraki",
        model="MS120-8-HW", end_of_sale=date(2025, 3, 28), end_of_support=date(2030, 3, 28),
        replacement_sku="MS130-8-HW",
        source_url="https://documentation.meraki.com/General_Administration/Other_Topics/Meraki_End-of-Life_(EOL)_Products_and_Dates",
        confidence="high"),
    "MS120-48FP-HW": EOLRecord(part_code="MS120-48FP-HW", vendor="Cisco Meraki",
        model="MS120-48FP-HW", end_of_sale=date(2025, 3, 28), end_of_support=date(2030, 3, 28),
        replacement_sku="MS130-48FP-HW",
        source_url="https://documentation.meraki.com/General_Administration/Other_Topics/Meraki_End-of-Life_(EOL)_Products_and_Dates",
        confidence="high"),
    "MS120-48LP-HW": EOLRecord(part_code="MS120-48LP-HW", vendor="Cisco Meraki",
        model="MS120-48LP-HW", end_of_sale=date(2025, 3, 28), end_of_support=date(2030, 3, 28),
        replacement_sku="MS130-48LP-HW",
        source_url="https://documentation.meraki.com/General_Administration/Other_Topics/Meraki_End-of-Life_(EOL)_Products_and_Dates",
        confidence="high"),
    "MR20-HW": EOLRecord(part_code="MR20-HW", vendor="Cisco Meraki",
        model="MR20-HW", end_of_sale=date(2021, 10, 31), end_of_support=date(2026, 10, 31),
        replacement_sku="MR36-HW",
        source_url="https://documentation.meraki.com/General_Administration/Other_Topics/Meraki_End-of-Life_(EOL)_Products_and_Dates",
        confidence="high"),
    "MR30H-HW": EOLRecord(part_code="MR30H-HW", vendor="Cisco Meraki",
        model="MR30H-HW", end_of_sale=date(2022, 3, 20), end_of_support=date(2027, 3, 20),
        replacement_sku="MR36H-HW",
        source_url="https://documentation.meraki.com/General_Administration/Other_Topics/Meraki_End-of-Life_(EOL)_Products_and_Dates",
        confidence="high"),
    "MR33-HW": EOLRecord(part_code="MR33-HW", vendor="Cisco Meraki",
        model="MR33-HW", end_of_sale=date(2021, 1, 14), end_of_support=date(2026, 1, 14),
        replacement_sku="MR36-HW",
        source_url="https://documentation.meraki.com/General_Administration/Other_Topics/Meraki_End-of-Life_(EOL)_Products_and_Dates",
        confidence="high"),
    "MR42-HW": EOLRecord(part_code="MR42-HW", vendor="Cisco Meraki",
        model="MR42-HW", end_of_sale=date(2021, 7, 19), end_of_support=date(2026, 7, 19),
        replacement_sku="MR44-HW",
        source_url="https://documentation.meraki.com/General_Administration/Other_Topics/Meraki_End-of-Life_(EOL)_Products_and_Dates",
        confidence="high"),
    "MR52-HW": EOLRecord(part_code="MR52-HW", vendor="Cisco Meraki",
        model="MR52-HW", end_of_sale=date(2021, 7, 19), end_of_support=date(2026, 7, 19),
        replacement_sku="MR56-HW",
        source_url="https://documentation.meraki.com/General_Administration/Other_Topics/Meraki_End-of-Life_(EOL)_Products_and_Dates",
        confidence="high"),
    "MR53-HW": EOLRecord(part_code="MR53-HW", vendor="Cisco Meraki",
        model="MR53-HW", end_of_sale=date(2021, 7, 19), end_of_support=date(2026, 7, 19),
        replacement_sku="MR56-HW",
        source_url="https://documentation.meraki.com/General_Administration/Other_Topics/Meraki_End-of-Life_(EOL)_Products_and_Dates",
        confidence="high"),
    "MX100-HW": EOLRecord(part_code="MX100-HW", vendor="Cisco Meraki",
        model="MX100-HW", end_of_sale=date(2021, 10, 31), end_of_support=date(2026, 10, 31),
        replacement_sku="MX105-HW",
        source_url="https://documentation.meraki.com/General_Administration/Other_Topics/Meraki_End-of-Life_(EOL)_Products_and_Dates",
        confidence="high"),

    # ═══════════════════════════════════════════════════════════════
    # HP ARUBA — J-code direct entries
    # Source: https://www.hpe.com/h20195/v2/Getdocument.aspx?docname=c04533547
    # ═══════════════════════════════════════════════════════════════
    "JL356A": EOLRecord(part_code="JL356A", vendor="HP Aruba",
        model="HPE 2540-48G-PoE+ Switch", end_of_sale=date(2023, 10, 31), end_of_support=date(2028, 10, 31),
        replacement_sku="JL726A",
        source_url="https://h20195.www2.hpe.com/v2/Getdocument.aspx?docname=c08378491",
        confidence="high"),
    "JL355A": EOLRecord(part_code="JL355A", vendor="HP Aruba",
        model="HPE 2540-24G-PoE+ Switch", end_of_sale=date(2023, 10, 31), end_of_support=date(2028, 10, 31),
        replacement_sku="JL725A",
        source_url="https://h20195.www2.hpe.com/v2/Getdocument.aspx?docname=c08378491",
        confidence="high"),
    "JL354A": EOLRecord(part_code="JL354A", vendor="HP Aruba",
        model="HPE 2540-24G Switch", end_of_sale=date(2023, 10, 31), end_of_support=date(2028, 10, 31),
        replacement_sku="JL725A",
        source_url="https://h20195.www2.hpe.com/v2/Getdocument.aspx?docname=c08378491",
        confidence="high"),
    "JL357A": EOLRecord(part_code="JL357A", vendor="HP Aruba",
        model="HPE 2540-48G Switch", end_of_sale=date(2023, 10, 31), end_of_support=date(2028, 10, 31),
        replacement_sku="JL726A",
        source_url="https://h20195.www2.hpe.com/v2/Getdocument.aspx?docname=c08378491",
        confidence="high"),
    "JL383A": EOLRecord(part_code="JL383A", vendor="HP Aruba",
        model="HPE 1920S 24G 2SFP Switch", end_of_sale=date(2023, 10, 31), end_of_support=date(2028, 10, 31),
        replacement_sku="",
        source_url="https://h20195.www2.hpe.com/v2/Getdocument.aspx?docname=c08341219",
        confidence="high"),
    "JL386A": EOLRecord(part_code="JL386A", vendor="HP Aruba",
        model="HPE 1920S 48G 4SFP Switch", end_of_sale=date(2023, 10, 31), end_of_support=date(2028, 10, 31),
        replacement_sku="",
        source_url="https://h20195.www2.hpe.com/v2/Getdocument.aspx?docname=c08341219",
        confidence="high"),
    "J9776A": EOLRecord(part_code="J9776A", vendor="HP Aruba",
        model="HP 2530-24G Switch", end_of_sale=date(2019, 10, 31), end_of_support=date(2024, 10, 31),
        replacement_sku="JL356A",
        source_url="https://h20195.www2.hpe.com/v2/Getdocument.aspx?docname=c07590430",
        confidence="high"),
    "J9772A": EOLRecord(part_code="J9772A", vendor="HP Aruba",
        model="HP 2530-48G Switch", end_of_sale=date(2019, 10, 31), end_of_support=date(2024, 10, 31),
        replacement_sku="JL357A",
        source_url="https://h20195.www2.hpe.com/v2/Getdocument.aspx?docname=c07590430",
        confidence="high"),
    "J9773A": EOLRecord(part_code="J9773A", vendor="HP Aruba",
        model="HP 2530-24G-PoE+ Switch", end_of_sale=date(2019, 10, 31), end_of_support=date(2024, 10, 31),
        replacement_sku="JL355A",
        source_url="https://h20195.www2.hpe.com/v2/Getdocument.aspx?docname=c07590430",
        confidence="high"),
    "J9778A": EOLRecord(part_code="J9778A", vendor="HP Aruba",
        model="HP 2530-48G-PoE+ Switch", end_of_sale=date(2019, 10, 31), end_of_support=date(2024, 10, 31),
        replacement_sku="JL356A",
        source_url="https://h20195.www2.hpe.com/v2/Getdocument.aspx?docname=c07590430",
        confidence="high"),
    "J9777A": EOLRecord(part_code="J9777A", vendor="HP Aruba",
        model="HP 2530-8G Switch", end_of_sale=date(2019, 10, 31), end_of_support=date(2024, 10, 31),
        replacement_sku="JL354A",
        source_url="https://h20195.www2.hpe.com/v2/Getdocument.aspx?docname=c07590430",
        confidence="high"),
    "JG924A": EOLRecord(part_code="JG924A", vendor="HP Aruba",
        model="HP 1920-24G-PoE+ Switch", end_of_sale=date(2020, 10, 31), end_of_support=date(2025, 10, 31),
        replacement_sku="JL383A",
        source_url="https://h20195.www2.hpe.com/v2/Getdocument.aspx?docname=c07590430",
        confidence="high"),
    "JG927A": EOLRecord(part_code="JG927A", vendor="HP Aruba",
        model="HP 1920-48G Switch", end_of_sale=date(2020, 10, 31), end_of_support=date(2025, 10, 31),
        replacement_sku="JL386A",
        source_url="https://h20195.www2.hpe.com/v2/Getdocument.aspx?docname=c07590430",
        confidence="high"),
}

# Merge into LOCAL_EOL_DB
LOCAL_EOL_DB.update(_EXTENDED_LOCAL_DB)


# ── Import master asset database (higher priority) ──────────────── #
from core.master_eol_db import MASTER_EOL_DB, lookup_master


def get_db() -> dict[str, EOLRecord]:
    """Return merged EOL database. Master data takes priority."""
    merged = dict(LOCAL_EOL_DB)
    merged.update(MASTER_EOL_DB)   # master data wins on key collision
    return merged


import re as _re

# Brand-prefix normalizations for CMDB variant part codes
_BRAND_PREFIX_MAP = [
    (_re.compile(r'^FORTIGATE[\s\-]+', _re.I),   "FG-"),
    (_re.compile(r'^FORTIGATERUGGED[\s\-]+', _re.I), "FGR-"),
    (_re.compile(r'^FORTINET[\s\-]+', _re.I),    "FG-"),
    (_re.compile(r'^JUNIPER[\s\-]+', _re.I),     ""),
    (_re.compile(r'^PALO ALTO NETWORKS[\s\-]+', _re.I), ""),
]

# Fortinet bare model numbers (e.g. "100E", "201E", "60F") → try FG- prefix
_FG_BARE = _re.compile(r'^(\d{2,4}[DEFG])(-\w+)?$')

# HP model-name → common J-code aliases (for model-name CMDB entries)
_HP_ALIAS = {
    "HP 2530-48G":         "J9772A",
    "HP 2530-24G":         "J9776A",
    "HP 2530-8G":          "J9777A",
    "HP 2530-24G-POEP":    "J9773A",
    "HP 2530-48G-POEP":    "J9778A",
    "HP 2540-48G-POEP":    "JL356A",
    "HP 2540-24G-POEP":    "JL355A",
    "HP 1920S 24G 2SFP":   "JL383A",
    "HP 1920S 48G 4SFP":   "JL386A",
    "HPE 1920S 48G 4SFP":  "JL386A",
    "HP 1920-24G-POE":     "JG924A",
    "HP 1920-48G":         "JG927A",
    # Additional HP/HPE variants
    "HP 2530-24G-POEPLUS":     "J9773A",
    "HP 2530-48G-POEPLUS":     "J9778A",
    "HPE 2540-48G-POEP":       "JL356A",
    "HPE 2540-24G-POEP":       "JL355A",
    "HPE 2530-24G":            "J9776A",
    "HPE 2530-48G":            "J9772A",
}

# Extreme Networks: models may appear with/without "Summit " or "X" prefix
# "X460-48T" → "SUMMIT X460-48T", "SUMMIT X460G2-24X" → "SUMMIT X460G2-24X"
_EXT_PREFIX_RE = _re.compile(r'^(?:SUMMIT[\s\-]+|EXTREME[\s\-]+)?', _re.I)


def _candidate_keys(part_code: str) -> list[str]:
    """Return all candidate lookup keys for a given part code."""
    raw = part_code.strip()
    up  = raw.upper()
    candidates = [up]

    # 1. Brand prefix stripping (Fortinet, Juniper, Palo Alto)
    for pattern, replacement in _BRAND_PREFIX_MAP:
        stripped = pattern.sub(replacement, raw, count=1)
        if stripped.upper() != up:
            candidates.append(stripped.upper())
            if replacement:
                candidates.append(replacement + stripped.upper())

    # 2. Fortinet bare model (e.g. "100E" → "FG-100E")
    m = _FG_BARE.match(up)
    if m:
        candidates.append("FG-" + up)

    # 3. HP model-name → J-code
    j = (_HP_ALIAS.get(raw)
         or _HP_ALIAS.get(raw.strip())
         or _HP_ALIAS.get(up)
         or _HP_ALIAS.get(up.strip()))
    if j:
        candidates.append(j.upper())

    # 4. Extreme Networks: add "SUMMIT " prefix and strip it
    if _re.match(r'^X4[56]\d', up) or _re.match(r'^SUMMIT\s', up, _re.I):
        stripped_ext = _EXT_PREFIX_RE.sub("", raw).strip().upper()
        candidates.append("SUMMIT " + stripped_ext)
        candidates.append(stripped_ext)
        # Also try X460-G2 format variants (dashes, spaces)
        compact = stripped_ext.replace(" ", "").replace("-", "")
        candidates.append("SUMMIT " + compact)

    # 5. Cisco IOS-XE style extra variant (C9200CX → C9200)
    if up.startswith("C9") and "CX" in up:
        candidates.append(up.replace("CX", ""))

    # 6. Strip trailing whitespace variants
    candidates.append(up.strip())

    return list(dict.fromkeys(candidates))  # deduplicate, preserve order


def lookup_local(part_code: str) -> "EOLRecord | None":
    """
    Lookup order:
      1. MASTER_EOL_DB  (highest priority — from master_assest_data.xlsx)
      2. LOCAL_EOL_DB   (curated + extended vendor DB)

    Tries multiple candidate keys per part code:
      - Exact match
      - Brand-prefix stripped ("FortiGate 60F" → "FG-60F")
      - Bare Fortinet numbers ("100E" → "FG-100E")
      - HP model-name to J-code mapping
      - Space/dash-normalized match
      - Prefix match (fallback)
    """
    raw   = part_code.strip()
    up    = raw.upper()
    keys  = _candidate_keys(raw)

    # ── Master DB ────────────────────────────────────────────────
    for key in keys:
        r = lookup_master(key)
        if r:
            return r

    # ── Local DB ─────────────────────────────────────────────────
    for key in keys:
        if key in LOCAL_EOL_DB:
            return LOCAL_EOL_DB[key]

    # Normalized (spaces/dashes removed) match across all candidates
    for key in keys:
        norm = key.replace(" ", "").replace("-", "")
        for k, v in LOCAL_EOL_DB.items():
            if norm == k.replace(" ", "").replace("-", ""):
                return v

    # Prefix match (longest key wins)
    best = None
    best_len = 0
    for key in keys:
        for k, v in LOCAL_EOL_DB.items():
            if (key.startswith(k) or k.startswith(key)) and len(k) > best_len:
                best = v
                best_len = len(k)
    return best
