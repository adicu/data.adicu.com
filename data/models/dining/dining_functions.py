import re

def dining_hall(value):
    return "place", re.compile(value, re.IGNORECASE)

def meal_type(value):
    return "meal_type", re.compile(value, re.IGNORECASE)
