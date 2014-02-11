import os
import momoko
import psycopg2
import functools
import logging

pg_host    = os.getenv('PG_HOST')
pg_port    = int(os.getenv('PG_PORT'))
pg_db      = os.getenv('PG_DB')
pg_user    = os.getenv('PG_USER')
pg_pass    = os.getenv('PG_PASSWORD')
pg_limit   = int(os.getenv('PG_LIMIT'))
pg_default = int(os.getenv('PG_DEFAULT'))
dsn = 'dbname=%s user=%s password=%s host=%s port=%s' % (
            pg_db, pg_user, pg_pass, pg_host, pg_port)


def pg_async():
    return momoko.AsyncClient({
            'host': pg_host,
            'database': pg_db,
            'port': pg_port,
            'user': pg_user,
            'password': pg_pass,
            'min_conn': 1,
            'max_conn': 20,
            'cleanup_timeout': 5
        })

def pg_sync():
    return psycopg2.connect(database=pg_db, user=pg_user,
            password=pg_pass, host=pg_host, port=pg_port)

class PGQuery:
    def __init__(self, model=None, model_functions=None):
        self.pg = pg_async()
        self.model = model
        self.model_functions = model_functions
    
    def execute(self, args, page=0, limit=pg_default, callback=None, unlimited=False):
        internal_callback = functools.partial(self._on_sql_response, callback=callback)

        if not unlimited:
            if not limit:
                limit = pg_default
            if limit < 0 or limit > pg_limit:
                limit = pg_limit
            offset = page * limit
        else:
            limit = "ALL"
            offset = 0

        query, arguments = self.build_sql_query(args, limit, offset)
        logging.info("Making SQL Query: %s" % (query % arguments))
        self.pg.execute(query, arguments, callback=internal_callback)

    def execute_many(self, argses, page=0, limit=pg_default, callback=None, unlimited=False):
        internal_callback = functools.partial(self._on_multi_sql_response,
                callback=callback)

        if not unlimited:
            if not limit:
                limit = pg_default
            elif limit < 0 or limit > pg_limit:
                limit = pg_limit
            offset = page * limit
        else:
            limit = "ALL"
            offset = 0

        query_pairs = [self.build_sql_query(args, limit, offset) for args in argses]
        sql = [(pair[0] % pair[1]) for pair in query_pairs]
        logging.info("Making SQL Queries: %s" % (sql))
        self.pg.chain(query_pairs, callback=internal_callback)

    def build_sql_query(self, arguments, limit, offset):
        # We have a dict of query keys and values and call getattr with the key,
        # which returns a function pointer with the name of "key", which we call, which
        # provides a query fragment that function makes
        model = self.model
        # slug is a list, each with (key, value, query_fragment)
        slug = [self.attr_func_wrap(key, value) for key, value in
                arguments.iteritems()]
        query_fragments = [fragment for _, _, fragment in slug]
        modified_arguments = {key: value for key, value, _ in slug}
        sql_query_fragments = {
                "select_body": ", ".join(model.SELECT),
                "table": model.TABLE,
                "query_fragments": " AND ".join(query_fragments),
                "limit": limit,
                "page": offset,
                "order_by" : model.ORDERBY,
        }

        query = "SELECT %(select_body)s FROM %(table)s WHERE %(query_fragments)s ORDER BY %(order_by)s LIMIT %(limit)s OFFSET %(page)s;" % sql_query_fragments
        print query
        
        return query, modified_arguments
    
    def attr_func_wrap(self, key, value):
        func = getattr(self.model_functions, key)
        value, fragment = func(value)
        return key, value, fragment

    def _on_multi_sql_response(self, cursors, callback=None):
        results = [cursor.fetchall() for cursor in cursors]
        responses = [[self.model.build_response_dict(row) for row in row_set] for row_set in results]
        print responses
        # We call back to tornado to respond to the client
        callback(responses)

    def _on_sql_response(self, cursor, callback=None):
        response = [self.model.build_response_dict(row) for row in cursor.fetchall()]
        # We call back to tornado to respond to the client
        callback(response)
