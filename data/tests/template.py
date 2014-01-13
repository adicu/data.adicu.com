
import unittest
import json
from data import app
from errors import errors


class TestingTemplate(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """ Instantiates a test instance of the app before each test """
        self.app = app.test_client()

    def check_error(self, resp, error_name, options=None):
        """ Tests that the resp is equal to the specified error """
        expected_error = errors.error_definitions[error_name]
        if not options:
            options = expected_error['default_options']

        self.assertEqual(resp.status_code, expected_error['status'])
        self.assertEqual(
            json.loads(resp.data)['message'],
            expected_error['message'].format(**options))
