
from flask import make_response, json
from os import path

DEFAULT_ERROR = 'SERVER_ERROR'
err_file = '{}/definitions.json'.format(path.dirname(path.abspath(__file__)))
with open(err_file) as f:
    error_definitions = json.load(f)


class AppError(Exception):
    """ A error class for defined app errors. """

    def __init__(self, name, **kwargs):
        self.name = name
        if kwargs:
            self.options = kwargs


def handle_app_error(err):
    """ Catches AppError when thrown and forms the defined err to responsed """
    return make_error(err)


def handle_404_error(err):
    """ Catches 404 errors and forms the defined err to responsed """
    return make_error(AppError("PAGE/ENDPOINT_NOT_FOUND"))


def make_error(err):
    """ Forms a response object based off of the passed in error.

    @param err: error that usually has a definition in definitions.json
    @return: flask response object
    """
    err_name = getattr(err, 'name', DEFAULT_ERROR)

    if err_name not in error_definitions:
        err_name = 'DEFAULT'
    error_obj = error_definitions[err_name]
    err_options = getattr(err, 'options', error_obj['default_options'])

    return make_response(json.dumps({
        # formats error message with options
        'message': error_obj['message'].format(**err_options),
        'status': error_obj['status']
    }), error_obj['status'])
