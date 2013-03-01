import logging


def get_collection():
    return "uem"

time_format = ["Date", "Start", "End"]

def build_response_dict(document):
    for key in document:
        if key in time_format:
            document[key] = str(document[key])
        elif key == "_id":
            document["id"] = str(document[key])
            del document["_id"]
    return document
