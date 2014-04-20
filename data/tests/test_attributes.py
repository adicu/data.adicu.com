import unittest
from os import path
from lib import attributes
from lib import converters

expected_dict = {
    "defaultSort": "room_location",
    "columns": {
        "room_location_area": {
            "column": "roomlocationarea",
            "type": "string",
            "description": "Residence type",
            "converter": converters.where_string
        },
        "residential_area": {
            "column": "residentialarea",
            "type": "string",
            "description": "Campus location",
            "converter": converters.where_string
        }
    }
}


class TestConverters(unittest.TestCase):

    def test_build_attribute_dictionary(self):
        """ test that attribute dictionaries are built correctly """
        self.assertDictEqual(
            expected_dict,
            attributes.build_dictionary(
                '{}/{}'.format(path.dirname(path.abspath(__file__)),
                               'test_attributes.json')))
