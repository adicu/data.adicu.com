import logging
import sys
import os
import datetime

base_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)

time_format = ["time"]

def get_collection():
    return "athletics"

def build_response_dict(document):
    document["time"] = str(document["time"])
    del document["_id"]
    return document
