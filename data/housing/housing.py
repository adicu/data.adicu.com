
from flask import Blueprint, json, make_response
from os import path
import sys

# add the parent directory for in-project imports
base_dir = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)
from lib import query
from lib import converters


housing = Blueprint('housing_blueprint', __name__)
TABLE = 'housing_t'

"""
Dictionary of querystring parameters tied to their column names and a function
to form a WHERE statement.
"""
room_attributes = {
    'room_location_area': {
        'column': 'roomlocationarea',
        'converter': converters.where_string
    },
    'residential_area': {
        'column': 'residentialarea',
        'converter': converters.where_string
    },
    'room_location': {
        'column': 'roomlocation',
        'converter': converters.where_string
    },
    'room_location_section': {
        'column': 'roomlocationsection',
        'converter': converters.where_string
    },
    'room_location_floor_suite': {
        'column': 'roomlocationfloorsuite',
        'converter': converters.where_string
    },
    'is_suite': {
        'column': 'issuite',
        'converter': converters.where_bool
    },
    'floor_suite_webdescription': {
        'column': 'floorsuitewebdescription',
        'converter': converters.where_string
    },
    'room': {
        'column': 'room',
        'converter': converters.where_string
    },
    'room_area': {
        'column': 'roomarea',
        'converter': converters.where_int
    },
    'room_space': {
        'column': 'roomspace',
        'converter': converters.where_string
    },
    'room_type': {
        'column': 'roomtype',
        'converter': converters.where_string
    },
    'ay_12_13_rs_status': {
        'column': 'ay1213rsstatus',
        'converter': converters.where_string
    },
    'point_value': {
        'column': 'pointvalue',
        'converter': converters.where_double
    },
    'lottery_number': {
        'column': 'lotterynumber',
        'converter': converters.where_int
    },
}


@housing.route('/rooms/options/<string:attr>')
def options(attr):
    """ Returns all options found in the database for this attribute """
    if attr not in room_attributes:
        return make_response(json.dumps({
            'message': 'bad_query, {} is not a valid attribute'.format(attr)
        }), 400)
    relevant_values = {attr: room_attributes[attr]}
    return json.dumps(query.build_query(TABLE, relevant_values))


@housing.route('/rooms')
def rooms():
    return json.dumps(query.build_query(TABLE, room_attributes))
