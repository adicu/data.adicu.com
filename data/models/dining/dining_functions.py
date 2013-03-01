import re
from datetime import datetime

def dining_hall(value):
    """Search by dining hall, for things like 'fer' for ferrs"""
    return "place", re.compile(value, re.IGNORECASE)

def meal_type(value):
    return "meal_type", re.compile(value, re.IGNORECASE)

def menu_item(value):
    values = [re.compile(item, re.IGNORECASE) for item in value.split(",")]
    return "menu", {"$all": values}

def meal_before(value):
    value = datetime.strptime(value, "%Y-%m-%d")
    return "day", {"$lt": value}

def meal_after(value):
    value = datetime.strptime(value, "%Y-%m-%d")
    return "day", {"$gt": value}

def meal_on(value):
    value = datetime.strptime(value, "%Y-%m-%d")
    return "day", value

