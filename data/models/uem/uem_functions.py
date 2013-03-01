import re

def room(value):
    return "Room", re.compile(value, re.IGNORECASE)

def event_name(value):
    return "Event Name", re.compile(value, re.IGNORECASE)

