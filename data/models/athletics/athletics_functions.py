import re
import athletics
from datetime import datetime

def sport(value):
    """ """
    if value.lower() in athletics.sports():
        return "sport", value.lower()
    else:
        return "sport", re.compile(value, re.IGNORECASE)

def feed(value):
    """ """
    return "feed", re.compile(value, re.IGNORECASE)

def title(value):
    """ """
    return "title", re.compile(value, re.IGNORECASE)

def win(value):
    """ A boolean """
    if value.lower() == "true":
        value = True
    else:
        value = False

    return "win", value

def location(value):
    """ """
    return "location", re.compile(value, re.IGNORECASE)

def opponent(value):
    """ """
    return "opponent", re.compile(value, re.IGNORECASE)

def game_before(value):
    """Format is Y-M-D H-M-S"""
    value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    return "time", {"$lt": value}

def game_after(value):
    """Format is Y-M-D H-M-S"""
    value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    return "time", {"$gt" : value}
