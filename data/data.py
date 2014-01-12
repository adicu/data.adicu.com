
# library imports
from flask import Flask, g
import psycopg2
import psycopg2.pool
import psycopg2.extras

# blueprint imports
from housing import housing_blueprint

app = Flask(__name__)
app.config.from_object('config.flask_config')

pg_pool = psycopg2.pool.SimpleConnectionPool(
    5,      # min connections
    20,     # max connections
    database=app.config['PG_DB'],
    user=app.config['PG_USER'],
    password=app.config['PG_PASSWORD'],
    host=app.config['PG_HOST'],
    port=app.config['PG_PORT'],
)


@app.before_request
def get_connections():
    """ Get a connection from the Postgres connection pool. """
    g.conn = pg_pool.getconn()
    # return python dictionaries from the cursor
    g.cursor = g.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


@app.teardown_request
def return_connections(*args, **kwargs):
    """ Return the connection to the Postgres connection pool. """
    g.cursor.close()
    pg_pool.putconn(g.conn)


""" Housing blueprint """
app.register_blueprint(housing_blueprint, url_prefix='/housing')

if __name__ == '__main__':
    app.run(host=app.config['HOST'])
