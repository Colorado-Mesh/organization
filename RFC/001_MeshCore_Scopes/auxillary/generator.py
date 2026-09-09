#!/usr/bin/python3
from pprint import pprint as prettyprint

import colorado
from colorado import (
    Mountains,
    Airports,
    Municipalities,
    UnincorporatedAreas,
    Counties,
)

# TODO: Add geographic regions to colorado_python library
GEOGRAPHIC_AREAS = {
    "Western Slopes": "ws",
    "Front Range": "fr",
    "Eastern Plains": "ep",
    "Central Mountains": "cm",
    "San Luis Valley": "sl"
}

TAB_BETWEEN_ABBR_AND_TEXT = 2

def state_geographic_zone_code(zone: str) -> str:
    assert len(zone) == 2
    return f"co-{zone.lower()}"

def colorado_mesh_region_code(region: str) -> str:
    assert len(region) == 3
    return f"co-{region.lower()}"

state_data = {}
# State Geographic Zones (`co` + 2-letter abbr)
for zone_name, zone_abbr in GEOGRAPHIC_AREAS.items():
    code = state_geographic_zone_code(zone_abbr)
    state_data[code] = f"{zone_name} geographic zone"
# Colorado Mesh Regions (IATA) (`co` + 3-letter abbr)
for airport in Airports:
    code = colorado_mesh_region_code(airport.iata_code)
    state_data[code] = f"{airport.name}"

data = {
    "*": None,
    "us": {
        "west": {
            "mnw": {
                "co": state_data,
                "ut": None,
                "wy": None,
            }
        }
    },
}

def add_tabs(_input: str, tab_count: int) -> str:
    for _ in range(tab_count):
        _input = f"\t{_input}"

    return _input

def print_level(data: dict, max_levels: int, tab_depth: int) -> str:
    for key, value in data.items():
        level_text = add_tabs(key, tab_count=tab_depth)
        if isinstance(value, dict):
            print(f"{print_level(value, max_levels=max_levels, tab_depth=tab_depth + 1)}")
        else:
            tab_padding = max_levels - tab_depth + TAB_BETWEEN_ABBR_AND_TEXT
            level_text += add_tabs(value, tab_count=tab_padding)
        print(level_text)

print_level(data, tab_depth=0, max_levels=4)


