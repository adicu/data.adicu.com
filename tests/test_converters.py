
import unittest
from data.lib import converters


class TestConverters(unittest.TestCase):

    def test_string_statement_conversion(self):
        self.assertEqual('TEST_COL LIKE %s',
                         converters.where_string('TEST_COL'))
        self.assertEqual('THIS_COL LIKE %s',
                         converters.where_string('THIS_COL'))

    def test_int_statement_conversion(self):
        self.assertEqual('age = %s', converters.where_int('age'))
        self.assertEqual('street = %s', converters.where_int('street'))

    def test_double_statement_conversion(self):
        self.assertEqual('gpa_col = %s', converters.where_double('gpa_col'))
        self.assertEqual('score = %s', converters.where_double('score'))

    def test_bool_statement_conversion(self):
        self.assertEqual('ALIVE = %s', converters.where_bool('ALIVE'))
        self.assertEqual('IS_SUITE = %s', converters.where_bool('IS_SUITE'))
