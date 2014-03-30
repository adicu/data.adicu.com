from lib.docs import convert as c
from inspect import getmembers as mem
from inspect import isfunction as func
import models.housing.room_functions as room
import models.housing.building_functions as building


lead = """Housing is broken down into two different endpoints,
                rooms and buildings.  Rooms has a bunch of room data (gasp) as
                well as some lottery information... Buildings has a list of
                amentities... We don't offer joins across these two datasets,
                so get creative! ;)"""
endpoints = {
                    "housing/rooms" : {
                        "request" : "{HOST}/housing/rooms?is_suite=true&api_token={{API_TOKEN}}",
                        "response" :
"""
{
    "status_code": 200,
    "data": [
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 2497,
            "RoomLocationSection": "47C - 1st Floor",
            "IsSuite": true,
            "Room": "47C 1A",
            "RoomType": "Single",
            "RoomSpace": "47C 1A-1 ",
            "Ay1213RSStatus": "Group Suite (In Person)",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 1 ",
            "RoomArea": 90,
            "PointValue": 21.6667,
            "FloorSuiteWebDescription": "",
            "ResidentialArea": "West Campus"
        },
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 2497,
            "RoomLocationSection": "47C - 1st Floor",
            "IsSuite": true,
            "Room": "47C 1B ",
            "RoomType": "Single",
            "RoomSpace": "47C 1B-1 ",
            "Ay1213RSStatus": "Group Suite (In Person)",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 1 ",
            "RoomArea": 120,
            "PointValue": 21.6667,
            "FloorSuiteWebDescription": "",
            "ResidentialArea": "West Campus"
        },
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 2497,
            "RoomLocationSection": "47C - 1st Floor",
            "IsSuite": true,
            "Room": "47C 1C ",
            "RoomType": "Single",
            "RoomSpace": "47C 1C-1",
            "Ay1213RSStatus": "Group Suite (In Person)",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 1 ",
            "RoomArea": 104,
            "PointValue": 21.6667,
            "FloorSuiteWebDescription": "",
            "ResidentialArea": "West Campus"
        },
        {
                "RoomLocation": "47 Claremont",
                "LotteryNumber": 2497,
                "RoomLocationSection": "47C - 1st Floor",
                "IsSuite": true,
                "Room": "47C 1D ",
                "RoomType": "Double",
                "RoomSpace": "47C 1D-2 ",
                "Ay1213RSStatus": "Group Suite (In Person)",
                "RoomLocationArea": "Small Suite",
                "RoomLocationFloorSuite": "47C - 1 ",
                "RoomArea": 180,
                "PointValue": 21.6667,
                "FloorSuiteWebDescription": "",
                "ResidentialArea": "West Campus"
        },
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 2497,
            "RoomLocationSection": "47C - 1st Floor",
            "IsSuite": true,
            "Room": "47C 1D ",
            "RoomType": "Double",
            "RoomSpace": "47C 1D-1 ",
            "Ay1213RSStatus": "Group Suite (In Person)",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 1 ",
            "RoomArea": 180,
            "PointValue": 21.6667,
            "FloorSuiteWebDescription": "",
            "ResidentialArea": "West Campus"
        },
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 2497,
            "RoomLocationSection": "47C - 1st Floor",
            "IsSuite": true,
            "Room": "47C 1E ",
            "RoomType": "Single",
            "RoomSpace": "47C 1E-1 ",
            "Ay1213RSStatus": "Group Suite (In Person)",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 1 ",
            "RoomArea": 81,
            "PointValue": 21.6667,
            "FloorSuiteWebDescription": "",
            "ResidentialArea": "West Campus"
        },
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 0,
            "RoomLocationSection": "47C - 2nd Floor",
            "IsSuite": true,
            "Room": "47C 21A",
            "RoomType": "Single",
            "RoomSpace": "47C 21A-1",
            "Ay1213RSStatus": "Withheld",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 21",
            "RoomArea": 105,
            "PointValue": 0,
            "FloorSuiteWebDescription": "3 Singles - 2 Doubles",
            "ResidentialArea": "West Campus"
        },
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 0,
            "RoomLocationSection": "47C - 2nd Floor",
            "IsSuite": true,
            "Room": "47C 21B",
            "RoomType": "Single",
            "RoomSpace": "47C 21B-1",
            "Ay1213RSStatus": "Withheld",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 21",
            "RoomArea": 120,
            "PointValue": 0,
            "FloorSuiteWebDescription": "3 Singles - 2 Doubles",
            "ResidentialArea": "West Campus"
        },
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 2257,
            "RoomLocationSection": "47C - 2nd Floor",
            "IsSuite": true,
            "Room": "47C 21C",
            "RoomType": "Double",
            "RoomSpace": "47C 21C-1",
            "Ay1213RSStatus": "Group Suite (In Person)",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 21",
            "RoomArea": 200,
            "PointValue": 10,
            "FloorSuiteWebDescription": "3 Singles - 2 Doubles",
            "ResidentialArea": "West Campus"
        },
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 2257,
            "RoomLocationSection": "47C - 2nd Floor",
            "IsSuite": true,
            "Room": "47C 21C",
            "RoomType": "Double",
            "RoomSpace": "47C 21C-2",
            "Ay1213RSStatus": "Group Suite (In Person)",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 21",
            "RoomArea": 200,
            "PointValue": 10,
            "FloorSuiteWebDescription": "3 Singles - 2 Doubles",
            "ResidentialArea": "West Campus"
        },
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 2257,
            "RoomLocationSection": "47C - 2nd Floor",
            "IsSuite": true,
            "Room": "47C 21D",
            "RoomType": "Double",
            "RoomSpace": "47C 21D-2",
            "Ay1213RSStatus": "Group Suite (In Person)",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 21",
            "RoomArea": 186,
            "PointValue": 10,
            "FloorSuiteWebDescription": "3 Singles - 2 Doubles",
            "ResidentialArea": "West Campus"
        },
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 2257,
            "RoomLocationSection": "47C - 2nd Floor",
            "IsSuite": true,
            "Room": "47C 21D",
            "RoomType": "Double",
            "RoomSpace": "47C 21D-1",
            "Ay1213RSStatus": "Group Suite (In Person)",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 21",
            "RoomArea": 186,
            "PointValue": 10,
            "FloorSuiteWebDescription": "3 Singles - 2 Doubles",
            "ResidentialArea": "West Campus"
        },
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 2257,
            "RoomLocationSection": "47C - 2nd Floor",
            "IsSuite": true,
            "Room": "47C 21E",
            "RoomType": "Single",
            "RoomSpace": "47C 21E-1",
            "Ay1213RSStatus": "Group Suite (In Person)",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 21",
            "RoomArea": 81,
            "PointValue": 10,
            "FloorSuiteWebDescription": "3 Singles - 2 Doubles",
            "ResidentialArea": "West Campus"
        },
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 877,
            "RoomLocationSection": "47C - 2nd Floor",
            "IsSuite": true,
            "Room": "47C 22A",
            "RoomType": "Single",
            "RoomSpace": "47C 22A-1",
            "Ay1213RSStatus": "Junior Regroup (In Person)",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 22",
            "RoomArea": 105,
            "PointValue": 20,
            "FloorSuiteWebDescription": "3 Singles - 2 Doubles",
            "ResidentialArea": "West Campus"
        },
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 877,
            "RoomLocationSection": "47C - 2nd Floor",
            "IsSuite": true,
            "Room": "47C 22B",
            "RoomType": "Single",
            "RoomSpace": "47C 22B-1",
            "Ay1213RSStatus": "Junior Regroup (In Person)",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 22",
            "RoomArea": 120,
            "PointValue": 20,
            "FloorSuiteWebDescription": "3 Singles - 2 Doubles",
            "ResidentialArea": "West Campus"
        },
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 877,
            "RoomLocationSection": "47C - 2nd Floor",
            "IsSuite": true,
            "Room": "47C 22C",
            "RoomType": "Double",
            "RoomSpace": "47C 22C-1",
            "Ay1213RSStatus": "Junior Regroup (In Person)",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 22",
            "RoomArea": 200,
            "PointValue": 20,
            "FloorSuiteWebDescription": "3 Singles - 2 Doubles",
            "ResidentialArea": "West Campus"
        },
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 877,
            "RoomLocationSection": "47C - 2nd Floor",
            "IsSuite": true,
            "Room": "47C 22C",
            "RoomType": "Double",
            "RoomSpace": "47C 22C-2",
            "Ay1213RSStatus": "Junior Regroup (In Person)",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 22",
            "RoomArea": 200,
            "PointValue": 20,
            "FloorSuiteWebDescription": "3 Singles - 2 Doubles",
            "ResidentialArea": "West Campus"
        },
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 0,
            "RoomLocationSection": "47C - 2nd Floor",
            "IsSuite": true,
            "Room": "47C 22D",
            "RoomType": "Double",
            "RoomSpace": "47C 22D-1",
            "Ay1213RSStatus": "Withheld",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 22",
            "RoomArea": 186,
            "PointValue": 0,
            "FloorSuiteWebDescription": "3 Singles - 2 Doubles",
            "ResidentialArea": "West Campus"
        },
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 2059,
            "RoomLocationSection": "47C - 2nd Floor",
            "IsSuite": true,
            "Room": "47C 22D",
            "RoomType": "Double",
            "RoomSpace": "47C 22D-2",
            "Ay1213RSStatus": "Junior Regroup (In Person)",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 22",
            "RoomArea": 186,
            "PointValue": 20,
            "FloorSuiteWebDescription": "3 Singles - 2 Doubles",
            "ResidentialArea": "West Campus"
        },
        {
            "RoomLocation": "47 Claremont",
            "LotteryNumber": 1029,
            "RoomLocationSection": "47C - 2nd Floor",
            "IsSuite": true,
            "Room": "47C 22E",
            "RoomType": "Single",
            "RoomSpace": "47C 22E-1",
            "Ay1213RSStatus": "Junior Regroup (In Person)",
            "RoomLocationArea": "Small Suite",
            "RoomLocationFloorSuite": "47C - 22",
            "RoomArea": 90,
            "PointValue": 20,
            "FloorSuiteWebDescription": "3 Singles - 2 Doubles",
            "ResidentialArea": "West Campus"
        }
    ],
    "status_txt": "OK"
}
""",
                        "queries" : c(mem(room, func)),
                    },
                    "housing/buildings" : {
                        "request" : "{HOST}/housing/buildings?name=watt&api_token={{API_TOKEN}}",
                        "response" :
"""
{
    "status_code": 200,
    "data": [
        {
            "Building": "Watt",
            "SharedKitchen": false,
            "SemiPrivateKitchen": false,
            "SuiteStyle": false,
            "ApartmentStyle": true,
            "Lounge": "",
            "SemiPrivateBathroom": false,
            "PrivateBathroom": true,
            "SharedBathroom": false,
            "CorridorStyle": false,
            "PrivateKitchen": true
        }
    ],
    "status_txt": "OK"
}
""",
                        "queries" : c(mem(building, func)),
                    },
                }

def get_lead():
    return lead

def get_endpoints():
    return endpoints
