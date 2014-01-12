
# library imports
from flask import Flask, g
import psycopg2
import psycopg2.pool
import psycopg2.extras


from errors import errors
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


# register error handlers
app.errorhandler(errors.AppError)(errors.handle_app_error)
app.errorhandler(404)(errors.handle_404_error)
app.errorhandler(Exception)(errors.handle_app_error)


""" Housing blueprint """
app.register_blueprint(housing_blueprint, url_prefix='/housing')


@app.route('/')
def home():
    with open('static/index.html') as f:
        return f.read()

if __name__ == '__main__':
    app.run(host=app.config['HOST'])
