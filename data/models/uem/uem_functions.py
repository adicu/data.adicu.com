import re

def room(value):
    return "Room", re.compile(value, re.IGNORECASE)

def event_name(value):
    return "Event Name", re.compile(value, re.IGNORECASE)

def event_starts_before(value):
    value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    return "Start", {"$lt": value}

def event_starts_after(value):
    value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    return "Start", {"$gt" : value}

def event_ends_before(value):
    value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    return "End", {"$lt": value}

def event_ends_after(value):
    value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    return "End", {"$gt": value}

def event_on(vale):
    value = datetime.strptime(value, "%Y-%m-%d")
    return "Date", value
