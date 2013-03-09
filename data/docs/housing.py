from lib.docs import convert as c
from inspect import getmembers as mem
from inspect import isfunction as func
import models.housing.room_functions as room
import models.housing.building_functions as building


lead = """Housing is broken down into two different endpoints,
                rooms and buildings.  Rooms has a bunch of room data (gasp) as
                well as some lottery information... Buildings has a list of
                amentities... We don't offer joins across these two datasets,
                so get creative! ;)"""
endpoints = {
                    "housing/rooms" : {
                        "request" : "http://data.adicu.com/housing/rooms?shared_bathroom=true&api_token=TOKEN",
                        "response" : "",
                        "queries" : c(mem(room, func)),
                    },
                    "housing/buildings" : {
                        "request" : "http://data.adicu.com/housing/buildings?name=&api_token=TOKEN",
                        "response" : "",
                        "queries" : c(mem(building, func)),
                    },
                }

def get_lead():
    return lead

def get_endpoints():
    return endpoints
