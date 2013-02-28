import logging
import sys
import os
import datetime


base_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)

single_room_format = {
    "RoomLocationArea": "",
    "ResidentialArea": "",
    "RoomLocation": "",
    "RoomLocationSection": "",
    "RoomLocationFloorSuite": "",
    "IsSuite": False,
    "FloorSuiteWebDescription": "",
    "Room": "",
    "RoomArea": 0,
    "RoomSpace": "",
    "RoomType": "",
    "Ay1213RSStatus": "",
    "PointValue": 0.0,
    "LotteryNumber": 0
}

SELECT = [key for key in single_room_format]
TABLE = "housing_t"

def build_response_dict(row):
    response = single_room_format.copy()
    for i, key in enumerate(single_room_format):
        response[key] = row[i]
    return response

