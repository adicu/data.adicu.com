
from os import environ, path
import sys
# add the parent directory for in-project imports
base_dir = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from errors import errors
from flask import request

PG_LIMIT = environ['PG_LIMIT']


def build_where_statement(config_dict):
    """
    Combines the querystring params into a WHERE statement for the sql query.

    @param config_dict: dict with column names and converter functions
    """
    statements = []
    values = []
    # iterate over the querystring params
    for attr, val in request.args.iteritems():
        try:
            statements.append(config_dict[attr]['converter'](
                config_dict[attr]['column']))
            values.append(val)  # add after the possible keyerror
        except KeyError:
            raise errors.AppError('INVALID_ATTRIBUTE', attr_name=attr)
    if statements:
        return 'WHERE '+' AND '.join(statements), values
    return '', []


def build_query(table, config_dict, option=None, page=0):
    """
    Constructs a pg sql query based on the table and given querystring.

    @param table: string name of the queried table
    @param config_dict: dictionary of (querystring key -> database column)
    @param page: page of the results to return (only used when a query has
        > PG_LIMIT results)
    """
    if option:
        select_statement = '{} AS {}'.format(config_dict[option]['column'], option)
    else:
        select_statement = ', '.join(['{} AS {}'.format(config_dict[col]['column'], col)
            for col in config_dict])

    where_statement, values = build_where_statement(config_dict)
    print where_statement
    query = "SELECT DISTINCT {} FROM {} {} LIMIT {} OFFSET {};".format(
        select_statement,       # columns to select
        table,                  # db table
        where_statement,        # various statements to narrow search results
        PG_LIMIT,               # number of rows to return
        int(PG_LIMIT)*page      # number or rows to skip
    )
    print query
    return query, values
