
from os import path
import sys
base_dir = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)

import unittest
import json
from data import app
from errors import errors


class TestingTemplate(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """ Instantiates a test instance of the app before each test """
        self.app = app.test_client()

    def check_error(self, resp, error_name):
        """ Tests that the resp is equal to the specified error """
        expected_error = errors.error_definitions[error_name]

        self.assertEqual(resp.status_code, expected_error['status'])
        self.assertEqual(
            json.loads(resp.data)['message'],
            expected_error['message'])
