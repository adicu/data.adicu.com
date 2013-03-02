import re
from datetime import datetime
from bson.objectid import ObjectId

def room(value):
    """ """
    return "Room", re.compile(value, re.IGNORECASE)

def event_name(value):
    """ """
    return "Event Name", re.compile(value, re.IGNORECASE)

def event_starts_before(value):
    """Format is Y-M-D H-M-S"""
    value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    return "Start", {"$lt": value}

def event_starts_after(value):
    """Format is Y-M-D H-M-S"""
    value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    return "Start", {"$gt" : value}

def event_ends_before(value):
    """Format is Y-M-D H-M-S"""
    value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    return "End", {"$lt": value}

def event_ends_after(value):
    """Format is Y-M-D H-M-S"""
    value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    return "End", {"$gt": value}

def event_on(value):
    """Format is Y-M-D"""
    value = datetime.strptime(value, "%Y-%m-%d")
    return "Date", value

def id(value):
    """ """
    return "_id", ObjectId(value)
