import os
import momoko

env = os.environ.get

pg_host = env('PG_HOST', None)
pg_port = env('PG_PORT', None)
pg_db = env('PG_DB', None)
pg_user = env('PG_USER', None)
pg_password = env('PG_PASSWORD', None)
dsn = 'dbname=%s user=%s password=%s host=%s port=%s' % (
            pg_database, pg_user, pg_password, pg_host, pg_port)

pg = momoko.Pool(dsn=dsn,
        minconn=1,
        maxconn=10,
        cleanup_timeout=10
)

def get_pg:
    return pg
