
from flask import Blueprint, json, g, make_response
from os import path
import sys

# add the parent directory for in-project imports
base_dir = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)
from lib import query
from lib import converters
from errors import errors


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
    """
    Returns all options found in the database for this attribute

    @param attr: an attribute of the room objects
    """
    if attr not in room_attributes:
        raise errors.AppError('INVALID_ATTRIBUTE', attr_name=attr)
    pg_query, values = query.build_query(TABLE, room_attributes, option=attr)
    g.cursor.execute(pg_query, values)
    results = g.cursor.fetchall()
    if not len(results):    # no results, shouldn't be called
        raise errors.AppError('NO_RESULTS')
    return make_response(json.dumps({
        'results': results,
        'status': 200
    }), 200)


@housing.route('/rooms')
@housing.route('/rooms/<int:page>')
def rooms(page=0):
    """ Returns all rooms that match the given querystring """
    pg_query, values = query.build_query(TABLE, room_attributes, page=page)
    g.cursor.execute(pg_query, values)
    results = g.cursor.fetchall()
    if not len(results):    # no results
        raise errors.AppError('NO_RESULTS')
    return make_response(json.dumps({
        'results': results,
        'status': 200
    }), 200)
