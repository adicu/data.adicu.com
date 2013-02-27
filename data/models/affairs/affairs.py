def get_collection():
    return "affairs"

def build_response_dict(document):
    del document["_id"]
    if "DATE" in document:
        document["DATE"] = str(document["DATE"])
    if "DATE END" in document:
        document["DATE END"] = str(document["DATE END"])
    if "Date" in document:
        document["Date"] = str(document["Date"])

    return document
