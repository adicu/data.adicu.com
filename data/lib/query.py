
from os import environ, path
import sys
# add the parent directory for in-project imports
base_dir = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from errors import errors
from flask import request

PG_LIMIT = int(environ['PG_LIMIT'])


def build_select_statemnt(config_dict, option=None):
    """
    Buildings the select statement based on the config_dict passed in. If
    option is instantiated then only that column will be returned.
    """
    if option:
        stmnt = '{} AS {}'.format(config_dict[option]['column'], option)
    else:
        stmnt = ', '.join(['{} AS {}'.format(
            config_dict[col]['column'], col) for col in config_dict])
    return 'SELECT DISTINCT ' + stmnt


def build_from_statement(table):
    """
    Builds the from statement based on the configuration for the query
    """
    return "FROM {}".format(table)


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
            if attr != 'token':
                raise errors.AppError('INVALID_ATTRIBUTE', attr_name=attr)
    if statements:
        return 'WHERE '+' AND '.join(statements), values
    return '', []


def build_order_by_statement(config_dict):
    """
    Builds the from statement based on the configuration for the query
    """
    # TODO: implement when config is switched to objects
    return ""


def build_query(table, config_dict, option=None, page=0):
    """
    Constructs a pg sql query based on the table and given querystring.

    @param table: string name of the queried table
    @param config_dict: dictionary of (querystring key -> database column)
    @param page: page of the results to return (only used when a query has
        > PG_LIMIT results)
    """
    where_statement, values = build_where_statement(config_dict)
    query = (
        "{select_stmnt} {from_stmnt} {where_stmnt} "
        "LIMIT {limit} OFFSET {offset};"
    ).format(
        select_stmnt=build_select_statemnt(config_dict, option),
        from_stmnt=build_from_statement(table),
        where_stmnt=where_statement,
        limit=PG_LIMIT,
        offset=PG_LIMIT*page
    )
    return query, values
