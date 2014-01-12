
from functools import wraps
from flask import make_response, json
from os import path

err_file = '{}/definitions.json'.format(path.dirname(path.abspath(__file__)))
with open(err_file) as f:
    error_definitions = json.load(f)


class AppError(Exception):
    """ A error class for defined app errors. """

    def __init__(self, name):
        self.name = name


def catch_error(f):
    """
    Meant to wrap wrap flask routes and listen for app errors.

    Catches AppError when thrown and forms the defined error for the response.
    If the exception thrown is not defined as an AppError, a 500 error is
    returned.
    """
    @wraps(f)
    def decorated_endpoint(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except AppError as e:
            return make_error(err=e.name)
        except Exception:
            return make_error(err='SERVER_ERROR')
    return decorated_endpoint


def make_error(err='DEFAULT'):
    """ Forms a response object based off of the passed in error name. """
    json_data, code = construct_err(err_name=err)
    return make_response(json_data, code)


def construct_err(err_name='DEFAULT'):
    """
    Forms a json object based off of the passed in error name.

    @param err_name: name of the error that should match an error defined in
        definitions.json
    @return: (json, status_code)
    """
    if err_name not in error_definitions:
        err_name = 'DEFAULT'

    error_obj = error_definitions[err_name]

    return json.dumps({
        'message': error_obj['message'],
        'status': error_obj['status']
    }), error_obj['status']
