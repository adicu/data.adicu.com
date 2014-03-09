
# library imports
from flask import Flask, g
import psycopg2
import psycopg2.pool
import psycopg2.extras
import redis

# project libraries
from errors import errors
from auth import user

app = Flask(__name__)
app.config.from_object('config.flask_config')

# blueprint imports
from housing.housing import housing as housing_blueprint
from auth.auth import auth_blueprint


pg_pool = psycopg2.pool.SimpleConnectionPool(
    5,      # min connections
    20,     # max connections
    database=app.config['PG_DB'],
    user=app.config['PG_USER'],
    password=app.config['PG_PASSWORD'],
    host=app.config['PG_HOST'],
    port=app.config['PG_PORT'],
)

redis_pool = redis.ConnectionPool(
    host=app.config['REDIS_HOST'],
    port=app.config['REDIS_PORT'],
    db=app.config['REDIS_DB'],
)


@app.before_request
def get_connections():
    """ Get connections from the Postgres and redis pools. """
    g.pg_conn = pg_pool.getconn()
    # return python dictionaries from the cursor
    g.cursor = g.pg_conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    g.redis = redis.Redis(connection_pool=redis_pool)


@app.teardown_request
def return_connections(*args, **kwargs):
    """ Return the connection to the Postgres connection pool. """
    g.cursor.close()
    pg_pool.putconn(g.pg_conn)


# register error handlers
app.register_error_handler(errors.AppError, errors.handle_app_error)
app.register_error_handler(404, errors.handle_404_error)


""" Blueprints """
housing_blueprint.before_request(user.rate_limit)   # add rate limiting
app.register_blueprint(housing_blueprint, url_prefix='/housing')
app.register_blueprint(auth_blueprint, url_prefix='')


@app.route('/')
def home():
    with open('static/index.html') as f:
        return f.read()

if __name__ == '__main__':
    app.run(host=app.config['HOST'])
