import json
from os import path
from lib import converters

converter_types = {
	'bool': converters.where_bool,
	'string': converters.where_string,
	'integer': converters.where_int,
	'double': converters.where_double
}

"""
Dictionary of querystring parameters tied to their column names and a function
to form a WHERE statement.
"""
def build_dictionary(attr_file):
	with open(attr_file) as f:
		table_attributes = json.loads(f.read())
	for key, value in table_attributes['columns'].items():
		table_attributes['columns'][key]['converter'] = converter_types[value['type']]
	return table_attributes