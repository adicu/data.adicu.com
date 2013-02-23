import logging
import sys
import os
import momoko
import functools

base_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)


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
                "courseid"
            ]

# Queries takes a dict
# We let the driver take care of injections
def do_sql(pg, queries, callback=None):
    # we build a string query with place holders such as 
    # "INSERT INTO test (num, data) VALUES (%s, %s)"
    # And a tuple for values such as 
    # (100, "abc'def")
    # to do pg.execute(str_query, tuples, callback);
    pass

