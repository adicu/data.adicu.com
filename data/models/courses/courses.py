import logging
import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)

single_course_format = {
        "Title": "",
        "Subtitle": "",
        "Term": "",
        "School" : "",
        "ClassType" : "",
        "Professor": "",
        "Description" : "",
        "Approval" : "",
        "Units" : 0,
        "MinUnits" : 0,
        "MaxUnits" : 0,
        "Department": "",
        "Size": 0,
        "MaxEnrollment" : 0,
        "Courseid": "",
        "CallNumber": "",
        "Type"
        "Meets": {
            "First": {
                "Days" : "",
                "Building" : "",
                "Room": "",
                "Starts" : "",
                "Ends": ""
            },
            "Second": {
                "Days" : "",
                "Building" : "",
                "Room": "",
                "Starts" : "",
                "Ends": ""
            }
        }
    }

SELECT = ["*"]
TABLE = "courses_t"

def build_response_dict(row):
    return row
