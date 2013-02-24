import os
import momoko
import psycopg2
import functools

pg_host = os.getenv('PG_HOST')
pg_port = int(os.getenv('PG_PORT'))
pg_db   = os.getenv('PG_DB')
pg_user = os.getenv('PG_USER')
pg_pass = os.getenv('PG_PASSWORD')
dsn = 'dbname=%s user=%s password=%s host=%s port=%s' % (
            pg_db, pg_user, pg_pass, pg_host, pg_port)

def pg_aync():
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
    def __init__(self, pg=None, model=None):
        self.pg = pg
        self.model = model
    
    def execute(arguments, callback=None):
        self.arguments = arguments
        self.tornado_callback = callback
        query = self.build_sql_query()
        self.pg.execute(query, arguments, callback=self._on_sql_response)

    def build_sql_query():
        # We have a dict of query keys and values and call getattr with the key,
        # which returns a function pointer with the name of "key", which we call, which
        # provides a query fragment that function makes
        model = self.model
        query_fragments = [getattr(model, key)(value) for key, value in arguments]
        select = model.SELECT
        table = model.TABLE
        sql_query_fragments = {
                "select_body": ", "select
                "table": table,
                "query_fragments": ", ".join(query_fragments)}
        query = "SELECT %(select_body) FROM %(table) WHERE %(query_fraguments);" % sql_query_fragments
        return query

    def _on_sql_response():
        response = [model.build_response_dict(row) for row in cursor.fetchall()]
        # We call back to tornado to respond to the client
        self.tornado_callback(response)
