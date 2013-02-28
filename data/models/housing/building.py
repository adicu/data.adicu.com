import logging
import sys
import os
import datetime


base_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)

single_building_format = {
    "Building": "",
    "ApartmentStyle": False,
    "SuiteStyle": False,
    "CorridorStyle": False,
    "PrivateBathroom": False,
    "SemiPrivateBathroom": False,
    "SharedBathroom": False,
    "PrivateKitchen": False,
    "SemiPrivateKitchen": False,
    "SharedKitchen": False,
    "Lounge": ""
}

SELECT = [key for key in single_building_format]
TABLE = "housing_amenities_t"

def build_response_dict(row):
    response = single_building_format.copy()
    for i, key in enumerate(single_building_format):
        response[key] = row[i]
    return response

