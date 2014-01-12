
import json
import unittest
from data.errors import errors


class TestErrors(unittest.TestCase):

    def test_generator_default(self):
        """ test that the generator correctly creates a default error """
        err_data, _ = errors.construct_err()
        err_data = json.loads(err_data)

        self.assertDictEqual(errors.error_definitions['DEFAULT'], err_data)

    def test_generator_name_fail(self):
        """ test that the generator correctly defaults with a bad err name """
        err_data, _ = errors.construct_err(err_name='IMAGINARY_ERROR')
        err_data = json.loads(err_data)
        self.assertDictEqual(errors.error_definitions['DEFAULT'], err_data)

    def test_generator_success(self):
        """ test that the generator correctly creates an error """
        test_error = 'NO_RESULTS'
        err_data, _ = errors.construct_err(err_name=test_error)
        err_data = json.loads(err_data)
        self.assertDictEqual(errors.error_definitions[test_error], err_data)

    def test_catch_error_decorator_used(self):
        """ test that the decorator correctly catches """
        test_app = app.test_client()

        # test for raise AppError
        resp = test_app.get('/apperror')
        self.__check_error(resp, 'DEFAULT')

        # test for standard exception
        resp = test_app.get('/exception')
        self.__check_error(resp, errors.DEFAULT_ERROR)

    def test_catch_error_decorator_not_used(self):
        """ test that the decorator doesn't interfere with valid requests """
        test_app = app.test_client()

        # test that nothing is interfered with valid requests
        resp = test_app.get('/safe')
        self.assertEqual('hello world', resp.data)

    def __check_error(self, resp, error_name):
        """ Tests that the resp is equal to the specified error """
        expected_error = errors.error_definitions[error_name]

        self.assertEqual(resp.status_code, expected_error['status'])
        self.assertEqual(
            json.loads(resp.data)['message'],
            expected_error['message'])


""" Test app for the purpose of testing the decorator """
from flask import Flask
app = Flask(__name__)


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
