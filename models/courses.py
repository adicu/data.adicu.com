import logging
import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)


import lib.dbs

possible_query_parameters = [
                "building",
                "term",
                "school",
                "call_number",
                "not_full",
                "professor",
                "department",
                "students_less_than",
                "class_type",
                "meets",
                "starts_before",
                "starts_after",
                "ends_before",
                "ends_after",
                "approval_required",
                "units",
                "title",
                "subtitle",
                "campus",
                "courseid",
            ]

def build_sql_query(queries):
    pass
