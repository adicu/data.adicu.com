
"""
Forms the statements within the WHERE clause in the query.

Separated so we can later add fuzzy string matching.
"""


def where_string(attr):
    return "{} LIKE %s".format(attr)


def where_int(attr):
    return "{} = %s".format(attr)


def where_double(attr):
    return "{} = %s".format(attr)


def where_bool(attr):
    return "{} = %s".format(attr)
