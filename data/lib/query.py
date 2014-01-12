
from os import environ, path
import sys
# add the parent directory for in-project imports
base_dir = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from errors import errors
from flask import request

PG_LIMIT = environ['PG_LIMIT']


def build_where_statement(attr_converter):
    """
    Combines the querystring params into a WHERE statement for the sql query.

    @param attr_converter: dict with column names and converter functions
    """
    statements = []
    values = []
    # iterate over the querystring params
    for attr, val in request.args.iteritems():
        try:
            statements.append(attr_converter[attr]['converter'](
                attr_converter[attr]['column']))
            values.append(val)  # add after the possible keyerror
        except KeyError:
            raise errors.AppError('INVALID_ATTRIBUTE', attr_name=attr)
    if statements:
        return 'WHERE '+' AND '.join(statements), values
    return '', []


def build_query(table, attr_converter, page=0):
    """
    Constructs a pg sql query based on the table and given querystring.

    @param table: string name of the queried table
    @param attr_converter: dictionary of (querystring key -> database column)
    @param page: page of the results to return (only used when a query has
        > PG_LIMIT results)
    """
    where_statement, values = build_where_statement(attr_converter)
    query = "SELECT DISTINCT {} FROM {} {} LIMIT {} OFFSET {};".format(
        ', '.join([attr_converter[x]['column'] for x in attr_converter]),
        table,                  # db table
        where_statement,        # various statements to narrow search results
        PG_LIMIT,               # number of rows to return
        int(PG_LIMIT)*page      # number or rows to skip
    )
    return query, values
