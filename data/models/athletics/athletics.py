import logging
import sys
import os
import datetime

base_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)

time_format = ["time"]

def sports():
    return [
        'archery',
        'baseball',
        'cross_country',
        'fencing',
        'field_hockey',
        'football',
        'heavyweight_rowing',
        'lacrosse',
        'lightweight_rowing',
        'mens_basketball',
        'mens_golf',
        'mens_soccer',
        'mens_squash',
        'mens_swimming',
        'mens_tennis',
        'softball',
        'track',
        'volleyball',
        'womens_basketball',
        'womens_golf',
        'womens_soccer',
        'womens_rowing',
        'womens_squash',
        'womens_swimming',
        'womens_tennis',
        'wrestling',
    ]


def get_collection():
    return "athletics"

def build_response_dict(document):
    document["time"] = str(document["time"])
    del document["_id"]
    return document
