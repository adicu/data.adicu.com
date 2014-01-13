
# add the parent directory for in-project imports
from os import path
import sys
base_dir = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)

import unittest
import flask
from lib import query, converters

""" Attribute converter for testing purposes """
attr_converter = {
    'test': {
        'column': 'test_column',
        'converter': converters.where_string
    },
    'foo': {
        'column': 'foo_column',
        'converter': converters.where_string
    }
}
test_table = 'test_table'


class TestQueryBuilder(unittest.TestCase):

    def test_build_where_statement_two_valid_attr(self):
        """ test that statement is correct with two attributes """
        statement, values = self.__test_where_statement_builder(
            '/?test=foo&foo=bar')
        self.assertEqual(statement,
                         'WHERE test_column LIKE %s AND foo_column LIKE %s')
        self.assertEqual(values, ['foo', 'bar'])

    def test_build_where_statement_fails_one_invalid_attr(self):
        """ test that builder fails with with 1 valid, 1 invalid params """
        with self.assertRaises(Exception) as err_context:
            self.__test_where_statement_builder('/?test=foo&wrong=bar')
        self.assertEqual(err_context.exception.name, 'INVALID_ATTRIBUTE')

    def test_build_where_statement_no_query(self):
        """ test that statement is correct with no querystring """
        statement, values = self.__test_where_statement_builder('/')
        self.assertEqual(statement, '')
        self.assertEqual(values, [])

    def __test_where_statement_builder(self, querystring):
        """ mocks a flask app in a request with the given querystring """
        app = flask.Flask(__name__)
        with app.test_request_context(querystring):
            return query.build_where_statement(attr_converter)

    def test_build_query_two_valid(self):
        """ test that query is correct with two attributes """
        query, values = self.__test_query_builder(
            '/?test=foo&foo=bar', 0)

        expected_query = (
            'SELECT DISTINCT test_column, foo_column '
            'FROM test_table '
            'WHERE test_column LIKE %s AND foo_column LIKE %s '
            'LIMIT 250 '
            'OFFSET 0;')
        self.assertEqual(query, expected_query)
        self.assertEqual(values, ['foo', 'bar'])

    def test_build_query_fails_one_invalid(self):
        """ test that query fails to build with 1 valid, 1 invalid attr """
        with self.assertRaises(Exception) as err_context:
            self.__test_query_builder('/?test=foo&wrong=bar', 0)
        self.assertEqual(err_context.exception.name, 'INVALID_ATTRIBUTE')

    def test_build_query_no_attr(self):
        """ test that query is correct with no querystring attributes """
        query, values = self.__test_query_builder('/', 0)

        expected_query = (
            'SELECT DISTINCT test_column, foo_column '
            'FROM test_table '
            ' '
            'LIMIT 250 '
            'OFFSET 0;')
        self.assertEqual(query, expected_query)
        self.assertEqual(values, [])

    def test_build_query_next_page(self):
        """ test that query is correct with no querystring attributes """
        query, values = self.__test_query_builder('/', 1)

        expected_query = (
            'SELECT DISTINCT test_column, foo_column '
            'FROM test_table '
            ' '
            'LIMIT 250 '
            'OFFSET 250;')
        self.assertEqual(query, expected_query)
        self.assertEqual(values, [])

    def __test_query_builder(self, querystring, page):
        """ mocks a flask app in a request with the given querystring """
        app = flask.Flask(__name__)
        with app.test_request_context(querystring):
            return query.build_query(test_table, attr_converter, page)
