
import unittest
import json
from data import data
from data.errors import errors


class TestingTemplate(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """ Instantiates a test instance of the app before each test """
        self.app = data.app.test_client()

    def check_error(self, resp, error_name):
        """ Tests that the resp is equal to the specified error """
        expected_error = errors.error_definitions[error_name]

        self.assertEqual(resp.status_code, expected_error['status'])
        self.assertEqual(
            json.loads(resp.data)['message'],
            expected_error['message'])
