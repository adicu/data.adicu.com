
import flask
from data.errors import errors
import template


class TestErrors(template.TestingTemplate):

    def test_generator_default(self):
        """ test that the generator correctly creates a default error """
        err_resp = self.__make_error(errors.AppError('DEFAULT'))
        self.check_error(err_resp, 'DEFAULT')

    def test_generator_name_fail(self):
        """ test that the generator correctly defaults with a bad err name """
        err_resp = self.__make_error(errors.AppError('IMAGINARY_ERROR'))
        self.check_error(err_resp, 'DEFAULT')

    def test_generator_success(self):
        """ test that the generator correctly creates an error """
        test_error = 'NO_RESULTS'
        err_resp = self.__make_error(errors.AppError(test_error))
        self.check_error(err_resp, test_error)

    def test_catch_error_used(self):
        """ test that the decorator correctly catches """
        test_app = app.test_client()

        # test for raise AppError
        resp = test_app.get('/apperror')
        self.check_error(resp, 'DEFAULT')

        # test for standard exception
        resp = test_app.get('/exception')
        self.check_error(resp, errors.DEFAULT_ERROR)

    def test_catch_error_format_used(self):
        """ test that the decorator correctly formats """
        test_app = app.test_client()

        # test for correctly formatting AppError
        attr = 'TEST'
        resp = test_app.get('/apperror/'+attr)
        self.check_error(resp, 'INVALID_ATTRIBUTE',
                         options={'attr_name': attr})

    def test_catch_error_default_format_used(self):
        """ test that the decorator correctly formats """
        test_app = app.test_client()

        # test for correctly formatting AppError w/o format params
        resp = test_app.get('/apperror/no_attr')
        self.check_error(resp, 'INVALID_ATTRIBUTE')

    def test_catch_error_not_used(self):
        """ test that the decorator doesn't interfere with valid requests """
        test_app = app.test_client()

        # test that nothing is interfered with valid requests
        resp = test_app.get('/safe')
        self.assertEqual('hello world', resp.data)

    def __make_error(self, err):
        """ Constructs an error in the request_context """
        app = flask.Flask(__name__)
        with app.test_request_context('/'):
            return errors.make_error(err)


""" Test app for the purpose of testing the decorator """
from flask import Flask
app = Flask(__name__)


@app.route('/apperror/<attr>')
def apperror_attr_raiser(attr):
    raise errors.AppError('INVALID_ATTRIBUTE', attr_name=attr)


@app.route('/apperror/no_attr')
def apperror_attr_raiser_no_attr():
    raise errors.AppError('INVALID_ATTRIBUTE')


@app.route('/apperror')
def apperror_raiser():
    raise errors.AppError('DEFAULT')


@app.route('/exception')
def exception_raiser():
    raise Exception('DEFAULT')


@app.route('/safe')
def hello():
    return 'hello world'

# register error handlers
app.errorhandler(errors.AppError)(errors.handle_app_error)
app.errorhandler(404)(errors.handle_404_error)
app.errorhandler(Exception)(errors.handle_app_error)
