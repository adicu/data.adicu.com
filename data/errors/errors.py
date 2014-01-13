
from flask import make_response, json
from os import path

DEFAULT_ERROR = 'SERVER_ERROR'
err_file = '{}/definitions.json'.format(path.dirname(path.abspath(__file__)))
with open(err_file) as f:
    error_definitions = json.load(f)


class AppError(Exception):
    """ A error class for defined app errors. """

    def __init__(self, name, **kwargs):
        """
        Define the error message and status

        @param name: error name that should match a definition in
            definitions.json, if a match is not found the default error will
            be returned.
        @param kwargs: named arguments are used in formatting error messages,
            if no arguments are passed the default arguments will be used.
        """
        self.name = name
        if self.name not in error_definitions:
            self.name = 'DEFAULT'
        error_obj = error_definitions[self.name]
        if kwargs:
            msg_options = kwargs
        else:
            msg_options = error_obj['default_options']

        self.message = error_obj['message'].format(**msg_options)
        self.status = error_obj['status']

    def response(self):
        """
        Builds a flask response object for the error

        @return: json w/ ['message', 'status'] & http status code
        """
        return make_response(json.dumps({
            'message': self.message,
            'status': self.status
        }), self.status)


def handle_app_error(err):
    """ Catches AppError when thrown and forms the defined err to responsed """
    if not isinstance(err, AppError):  # only called w/ regular Exceptions
        err = AppError(DEFAULT_ERROR)
    return err.response()


def handle_404_error(err):
    """ Catches 404 errors and forms the defined err to responsed """
    return AppError("PAGE/ENDPOINT_NOT_FOUND").response()
