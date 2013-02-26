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
    "Term": "",
    "SchoolName" : "",
    "TypeName" : "",
    "Instructor1Name": "",
    "Approval" : "",
    "NumFixedUnits" : 0,
    "MinUnits" : 0,
    "MaxUnits" : 0,
    "DepartmentName": "",
    "NumEnrolled": 0,
    "MaxSize" : 0,
    "CallNumber": "",
    "MeetsOn1" : "",
    "Building1" : "",
    "Room1": "",
    "StartTime1" : "",
    "EndTime1": "",
    "MeetsOn2" : "",
    "Building2" : "",
    "Room2": "",
    "StartTime2" : "",
    "EndTime2": "",
    "CampusName": "",
    "CampusCode": ""
}

time_format = ["StartTime1", "EndTime1", "StartTime2", "EndTime2"]
SELECT = [key for key in single_course_format]
TABLE = "courses_t"

def build_response_dict(row):
    response = single_course_format.copy()
    for i, key in enumerate(single_course_format):
        if key in time_format:
            response[key] = str(row[i])
        else:
            response[key] = row[i]
    return response
