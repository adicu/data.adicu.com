from lib.docs import convert as c
from inspect import getmembers as mem
from inspect import isfunction as func
import models.uem.uem_functions as uem

lead =  """UEM, for University Events Management is a delayed
                live feed of whats coming out UEM. Updated nightly, this
                endpoint has all the confirmed booked space on campus that UEM
                handles, which is alot.  Be sure to play around with the event
                name query param, because its probably the richest one"""
endpoints = {
                    "uem" : {
                        "request" : "http://data.adicu.com/uem?room=wien&pretty=true&api_token=API_TOKEN",
                        "response" : """{
    "status_code": 200,
    "data": [
        {
            "Event Name": "Varsity Show - Rehearsal",
            "End": "2013-02-28 23:00:00",
            "Room": "Wien Lounge",
            "Start": "2013-02-28 20:00:00",
            "Date": "2013-02-28 00:00:00",
            "id": "51302459c749140b2a2dc49b"
        },
    "status_txt": "OK",
    }""",
                        "queries" : c(mem(uem, func)),
                    },
                }

def get_lead():
    return lead

def get_endpoints():
    return endpoints
