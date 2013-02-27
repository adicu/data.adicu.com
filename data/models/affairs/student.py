import sys
import os
import datetime

single_event_format = {}

time_format = [""]
SELECT = [key for key in single_event_format]
TABLE = "affairs_student_t"

def build_response_dict(row):
    response = single_course_format.copy()
    for i, key in enumerate(single_course_format):
        if key in time_format:
            response[key] = str(row[i])
        else:
            response[key] = row[i]
    return response
