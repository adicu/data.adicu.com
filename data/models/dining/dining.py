import logging
import sys
import os
import datetime

base_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)

single_meal_format = {
        "place"    : "",
        "menu"     : "",
        "day"      : "",
        "url"      : "",
        "meal_type": ""
    }

time_format = ["day"]

def get_collection():
    return "dining"

def build_response_dict(document):
    print document
    response = single_meal_format.copy()
    for i, key in enumerate(single_meal_format):
        response[key] = document[key]
    return response
