
from flask import Flask, g
import psycopg2
import psycopg2.pool

app = Flask(__name__)
app.config.from_object('config.flask_config')

pg_pool = psycopg2.pool.SimpleConnectionPool(5, 20, 
    database    = app.config['PG_DB'],
    user        = app.config['PG_USER'],
    password    = app.config['PG_PASS'],
    host        = app.config['PG_HOST'],
    port        = app.config['PG_PORT'],
)


@app.before_request
def get_connections():
    g.conn = pg_pool.getconn()


@app.teardown_request
def return_connections(*args, **kwargs):
    pg_pool.putconn(g.conn)


if __name__ == '__main__':
    app.run(host=app.config['HOST'])

