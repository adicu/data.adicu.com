from flask import Blueprint, json, g, make_response
from os import path
import sys

# add the parent directory for in-project imports
base_dir = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)
from lib import query
from lib import attributes
from errors import errors

housing = Blueprint('housing_blueprint', __name__)
ROOMS_TABLE = 'housing_t'
BUILDINGS_TABLE = 'housing_amenities_t'

room_attributes = attributes.build_dictionary(
    '{}/{}'.format(path.dirname(path.abspath(__file__)),
                   'room_attributes.json'))
building_attributes = attributes.build_dictionary(
    '{}/{}'.format(path.dirname(path.abspath(__file__)),
                   'building_attributes.json'))


@housing.route('/rooms/options/<string:attr>')
def room_options(attr):
    """
    Returns all options found in the database for this attribute

    @param attr: an attribute of the room objects
    """
    if attr not in room_attributes['columns']:
        raise errors.AppError('INVALID_ATTRIBUTE', attr_name=attr)
    pg_query, values = query.build_query(ROOMS_TABLE,
                                         room_attributes['columns'],
                                         option=attr)
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
    """
    Returns all rooms that match the given querystring
    """
    pg_query, values = query.build_query(ROOMS_TABLE,
                                         room_attributes['columns'],
                                         page=page)
    g.cursor.execute(pg_query, values)
    results = g.cursor.fetchall()
    if not len(results):    # no results
        raise errors.AppError('NO_RESULTS')
    return make_response(json.dumps({
        'results': results,
        'status': 200
    }), 200)


@housing.route('/buildings/options/<string:attr>')
def building_options(attr):
    """
    Returns all options found in the database for this attribute

    @param attr: an attribute of the building objects
    """
    if attr not in building_attributes['columns'].keys():
        raise errors.AppError('INVALID_ATTRIBUTE', attr_name=attr)
    # strip the dictionary down to the relevant attribute
    pg_query, values = query.build_query(BUILDINGS_TABLE,
                                         building_attributes['columns'],
                                         option=attr)
    g.cursor.execute(pg_query, values)
    results = g.cursor.fetchall()
    if not len(results):  # no results, shouldn't be called
        raise errors.AppError("NO_RESULTS")
    return make_response(json.dumps({
        'results': results,
        'status': 200
    }), 200)


@housing.route('/buildings')
@housing.route('/buildings/<int:page>')
def buildings(page=0):
    """ Returns all buildings that match the given querystring """
    pg_query, values = query.build_query(BUILDINGS_TABLE,
                                         building_attributes['columns'],
                                         page=page)
    g.cursor.execute(pg_query, values)
    results = g.cursor.fetchall()
    if not len(results):    # no results
        raise errors.AppError('NO_RESULTS')
    return make_response(json.dumps({
        'results': results,
        'status': 200
    }), 200)
