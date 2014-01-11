
from flask import Blueprint, json
from os import path
import sys

# add the parent directory for in-project imports
base_dir = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)
from lib import query


housing = Blueprint('housing_blueprint', __name__)
TABLE = 'housing_t'

room_attributes = {
    'room_location_area': 'roomlocationarea',
    'residential_area': 'residentialarea',
    'room_location': 'roomlocation',
    'room_location_section': 'roomlocationsection',
    'room_location_floor_suite': 'roomlocationfloorsuite',
    'is_suite': 'issuite',
    'floor_suite_webdescription': 'floorsuitewebdescription',
    'room': 'room',
    'room_area': 'roomarea',
    'room_space': 'roomspace',
    'room_type': 'roomtype',
    'ay_12_13_rs_status': 'ay1213rsstatus',
    'point_value': 'pointvalue',
    'lottery_number': 'lotterynumber',
}


@housing.route('/rooms/options/<string:attribute>')
def options(attribute):
    """ Returns all options found in the database for this attribute """
    pass


@housing.route('/rooms')
def rooms():
    return json.dumps(query.build_query(TABLE, room_attributes))
