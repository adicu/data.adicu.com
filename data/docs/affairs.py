from lib.docs import convert as c
from inspect import getmembers as mem
from inspect import isfunction as func
import models.affairs.affairs_functions as affairs


lead =  """The affairs endpoint is pretty different from the
    others, as this one doesn't have any query parameters, just
    ping the endpoint, and see all the results we have fly!"""

endpoints = {
    "affairs/social_media" : {
        "request": "http://data.adicu.com/affairs/social_media?pretty=true&api_token=TOKEN",
        "response": """
{
    "status_code": 200,
    "data": [
        {
            "Facebook": "http://www.facebook.com/ColumbiaCSA",
            "social_media": true,
            "Name / Lead Office": "Center for Student Advising",
            "Twitter Handle": "http://twitter.com/ColumbiaCSA"
        }
    ],
    "status_txt" : "OK",
}""",
        "queries" : None,
    },
    
    "affairs/student_events" : {
        "request": "http://data.adicu.com/affairs/student_events?pretty=true&api_token=TOKEN",
        "response": """
{
    "status_code": 200,
    "data": [
        {
            "student_events": true,
            "Description": "Reps from Tufts Vet School will present on veterinary medicine",
            "Lead Office": "PreProfessional Advising (CSA)",
            "Audience": "All students interested in veterinary medicine",
            "Location": "401 Lerner",
            "Time": "6:00 - 7:30 p.m.",
            "Date": "2013-02-25 00:00:00",
            "Event": "Tufts School of Vet Medicine Visit"
        },
    ],
    "status_txt": "OK" 
} """,
        "queries" : None,
    },

    "affairs/alumni_events" : {
        "request": "http://data.adicu.com/affairs/alumni_events?pretty=true&api_token=TOKEN",
        "response": """{
    "status_code": 200,
    "data": [
        {
            "STATUS": "Confirmed",
            "LEAD ALUMNI AFFAIRS STAFF": "Trimmer*",
            "SPEAKER/PURPOSE": "Board Meeting",
            "EVENT TIME": "7 p.m.",
            "Sponsor": "CCYA",
            "VENUE/LOCATION": "CAC, Schapiro Conference Room",
            "DATE": "2013-02-20 00:00:00",
            "TARGET AUDIENCE": "CCYA Board Members",
            "EVENT": "CCYA Full Board Meeting",
            "alumni_events": true
        },
    ],
    status_txt="OK"
} """,
                            "queries" : None,
    },
}

def get_lead():
    return lead

def get_endpoints():
    return endpoints
