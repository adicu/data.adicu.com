import logging
import sys
import os
import datetime


base_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)

single_course_format = {
    "CourseTitle": "",
    "CourseSubtitle": "",
    "Course": "",
    "SchoolName" : "",
    "Approval" : "",
    "NumFixedUnits" : 0,
    "MinUnits" : 0,
    "MaxUnits" : 0,
    "DepartmentName": "",
    "DepartmentCode": "",
    "Description": ""
}

SELECT = [key for key in single_course_format]
TABLE = "courses_v2_t"
ORDERBY = "Course"

def build_response_dict(row):
    response = single_course_format.copy()
    for i, key in enumerate(single_course_format):
        response[key] = row[i]
    return response
