import logging
import sys
import os
import datetime

base_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)

def build_response_dict(row):
    response = single_course_format.copy()
    for i, key in enumerate(single_course_format):
        if key in time_format:
            response[key] = str(row[i])
        else:
            response[key] = row[i]
    return response
