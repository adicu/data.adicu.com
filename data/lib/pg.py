import os

import momoko
import psycopg2

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
