from lib.docs import convert as c
from inspect import getmembers as mem
from inspect import isfunction as func
import models.dining.dining_functions as dining

lead =  """Dining, the must have endpoint for anyone with a
                stomach on this campus! Check out the way locations are done,
                they are abbreviated in a strange way, like 'fer' for
                ferris."""
endpoints = {
                    "dining" : {
                        "request" : "http://data.adicu.com/dining?menu_item=pizza&pretty=true&api_token=TOKEN",
                        "response" : """ {
    "status_code": 200,
    "data": [
        {
            "url": "http://dining.columbia.edu/122week-one-tuesday-lunch-fbc",
            "menu": [
                "Firecracker Chicken Wrap",
                "Cheese Pizza",
                "Pepperoni Pizza",
                "Genovese Pizza",
                "Mushroom & Garlic Pizza",
                "Meatball Hero",
                "Chicken Tortilla Soup",
                "Smoked Ham Calzone",
                "Broccoli & Cheddar Soup",
                "Grits",
                "Waffles"
            ],
            "place": "Fer",
            "day": "2013-01-22 00:00:00",
            "meal_type": "LU"
        },""",
                        "queries" : c(mem(dining, func)),
                    }
                }

def get_lead():
    return lead

def get_endpoints():
    return endpoints
