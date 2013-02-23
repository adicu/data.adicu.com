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
def do_sql(pg, queries, callback):
    # we build a string query with place holders such as 
    # "INSERT INTO test (num, data) VALUES (%s, %s)"
    # And a tuple for values such as 
    # (100, "abc'def")
    internal_callback = functools.partial(form_dict, callback=callback)
    pg.execute("SELECT * FROM courses_t;", callback=internal_callback);

def form_dict(cursor, callback=None):
    # here we call back to the origninal function
    # ideally, we take our cursor here, and spit back a dict from our tuple
    # object
    callback({})


