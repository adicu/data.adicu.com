from lib.docs import convert as c
from inspect import getmembers as mem
from inspect import isfunction as func
from models.courses_v2 import courses_functions as courses
from models.courses_v2 import sections_functions as sections

lead = """The courses API got a reboot to conceptually separate courses and sections. 

There are two courses endpoints: courses/v2/courses and courses/v2/sections.
All the sections for a course come embedded in that course. The query
parameters for the two are pretty disjoint for now; this should be fixed at
some point."""

endpoints = {
                    "courses" : {
                        "request" : "http://data.adicu.com/courses/v2/courses?api_token=API_TOKEN&department=coms&pretty=true&limit=1",
                        "response" : """{
    "status_code": 200,
    "data": [
        {
            "Description": "Provides comprehensive introduction to computational techniques for analyzing genomic data including DNA, RNA and protein structures; microarrays; transcription and regulation; regulatory, metabolic and protein interaction networks. The course covers sequence analysis algorithms, dynamic programming, hidden Markov models, phylogenetic analysis, Bayesian network techniques, neural networks, clustering algorithms, support vector machines, Boolean models of regulatory networks, flux based analysis of metabolic networks and scale-free network models. The course provides self-contained introduction to relevant biological mechanisms and methods.",
            "SchoolName": "INTERFACULTY",
            "CourseTitle": "COMPUTATIONAL GENOMICS",
            "MinUnits": 0,
            "DepartmentName": "COMPUTER SCIENCE",
            "Course": "CBMF4761",
            "NumFixedUnits": 30,
            "MaxUnits": 0,
            "DepartmentCode": "COMS",
            "Approval": "",
            "Sections": [
                {
                    "Term": "20131",
                    "CampusName": "MORNINGSIDE",
                    "StartTime2": "None",
                    "StartTime1": "16:10:00",
                    "Course": "CBMF4761",
                    "CampusCode": "MORN",
                    "Instructor1Name": "PE\\\\'ER, ITSHACK",
                    "Building1": "SEELEY W. MU",
                    "Building2": null,
                    "NumEnrolled": 15,
                    "CallNumber": 69280,
                    "MeetsOn1": "MW",
                    "EndTime1": "17:25:00",
                    "EndTime2": "None",
                    "MeetsOn2": null,
                    "TypeName": "LECTURE",
                    "MaxSize": 75,
                    "Room2": null,
                    "Room1": "1127"
                }
            ],
            "CourseSubtitle": "COMPUTATIONAL GENOMICS"
        }
    ],
    "status_txt": "OK"
}""",
                        "queries" : c(mem(courses, func)),
                    },
                    "sections" : {
                        "request" : "http://data.adicu.com/courses/v2/sections?api_token=API_TOKEN&not_full=false&pretty=true&limit=1",
                        "response" : """{
    "status_code": 200,
    "data": [
        {
            "Term": "20131",
            "CampusName": "BARNARD COLLEGE",
            "StartTime2": "None",
            "StartTime1": "13:10:00",
            "Course": "SPAN1102",
            "CampusCode": "CBAR",
            "Instructor1Name": "ARCE-FERNANDEZ, MARIA I",
            "Building1": "MILBANK HALL",
            "Building2": null,
            "NumEnrolled": 16,
            "CallNumber": 511,
            "MeetsOn1": "MTWR",
            "EndTime1": "14:15:00",
            "EndTime2": "None",
            "MeetsOn2": null,
            "TypeName": "LANGUAGE",
            "MaxSize": 15,
            "Room2": null,
            "Room1": "237"
        }
    ],
    "status_txt": "OK"
}""",
                        "queries" : c(mem(sections, func)),
                    },
                }

def get_lead():
    return lead

def get_endpoints():
    return endpoints
