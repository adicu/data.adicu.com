
from flask import request, g
from os import environ

PG_LIMIT = environ['PG_LIMIT']


def build_where_statement(attr_converter):
    """
    Combines the querystring params into a WHERE statement for the sql query.
    """
    statements = []
    values = []
    for attr, val in request.args.iteritems():
        print attr, val
        try:
            # use LIKE for fuzzy string match
            statements.append(attr_converter[attr]+' LIKE %s')
            values.append(val)  # add after the possible keyerror
        except KeyError:
            pass
    if statements:
        return ' WHERE '+' AND '.join(statements), values
    return '', []


def build_query(table, attr_converter):
    """
    Constructs a pg sql query based on the table and given querystring.

    @param table: string name of the queried table
    @param attr_converter: dictionary of (querystring key -> database column)
    """
    where_statement, values = build_where_statement(attr_converter)
    query = """ SELECT DISTINCT {} FROM {} {} LIMIT {};""".format(
        ', '.join(attr_converter.values()),
        table,
        where_statement,
        PG_LIMIT,
    )
    print query
    g.cursor.execute(query, values)
    return g.cursor.fetchall()
