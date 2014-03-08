
import unittest
import json
import data
from errors import errors
import redis


test_email, test_user, test_token = 'test@test.com', 'tester', '12345'
test_record = {
    'email': test_email,
    'token': test_token,
    'name': test_user
}


class TestingTemplate(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """ Instantiates a test instance of the app before each test """
        self.app = data.app.test_client()
        r = redis.Redis(connection_pool=data.redis_pool)
        r.sadd('tokens', test_token)

    def check_error(self, resp, error_name, options=None):
        """ Tests that the resp is equal to the specified error """
        expected_error = errors.error_definitions[error_name]
        if not options:
            options = expected_error['default_options']

        self.assertEqual(resp.status_code, expected_error['status'])
        self.assertEqual(
            json.loads(resp.data)['message'],
            expected_error['message'].format(**options))


class MockingTemplate(unittest.TestCase):

    def check_query(self, obj, expected_query, expected_values):
        """ check a mocked query was called correctly """
        query, values = obj.call_args[0]
        self.assertEqual(query, expected_query)
        for i, val in enumerate(expected_values):
            self.assertEqual(values[i], val)

    def check_queries(self, obj, expected_queries, expected_values):
        """ check a mocked query was called correctly """
        for j, args in enumerate(obj.call_args_list):
            query, values = args[0][0], args[0][1]
            self.assertEqual(query, expected_queries[j])
            for i, val in enumerate(expected_values[j]):
                self.assertEqual(values[i], val)
