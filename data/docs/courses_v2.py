from lib.docs import convert as c
from inspect import getmembers as mem
from inspect import isfunction as func
import models.courses.courses_functions as courses

lead = """This endpoint is hiding a whole bunch of data! Make
                sure you use the different query parameters effectively to see
                its all done behind.  Think of it as one giant sql table
                you're making requests against."""

endpoints = {
                    "courses" : {
                        "request" : "http://data.adicu.com/courses?building=pupin&limit=1&pretty=true&api_token=API_TOKEN",
                        "response" : """{
    "status_code": 200,
    "data": [
        {
            "CampusCode": "MORN",
            "CampusName": "MORNINGSIDE",
            "StartTime2": "None",
            "StartTime1": "15:00:00",
            "CourseTitle": "EARTH, MOON AND PLANETS",
            "MinUnits": 0,
            "CallNumber": "66696",
            "Term": "20122",
            "EndTime1": "17:10:00",
            "Instructor1Name": "APPLEGATE, JAMES H",
            "Building1": "PUPIN LABORA",
            "Building2": null,
            "NumEnrolled": 3,
            "SchoolName": "SCHOOL OF CONTINUING EDUCATION",
            "DepartmentName": "ASTRONOMY",
            "MeetsOn1": "TR",
            "MaxSize": 999,
            "EndTime2": "None",
            "MeetsOn2": null,
            "TypeName": "LECTURE",
            "NumFixedUnits": 30,
            "MaxUnits": 0,
            "Room2": null,
            "Room1": "1332",
            "Approval": "",
            "CourseSubtitle": "EARTH, MOON AND PLANETS"
        }
    ],
    "status_txt": "OK"
} """,
                        "queries" : c(mem(courses, func)),
                    },
                }

def get_lead():
    return lead

def get_endpoints():
    return endpoints
