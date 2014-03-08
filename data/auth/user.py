
from struct import unpack
from flask import g, request
from os import urandom, path
import sys

# add the parent directory for in-project imports
base_dir = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)
from errors import errors


GET_USER = "SELECT * FROM users_t WHERE email = %s;"
INSERT_USER = ('INSERT INTO users_t (email, token, name) '
               'VALUES (%s, %s, %s);')
TOKENS = 'tokens'


def generate_token():
    """ Generate a random integer for a token.

    We use os.urandom() to create the token securely and struct.unpack() to
    create an unsigned long long from the random bytes. "<Q" corresponds to an
    unsigned long.
    """
    return unpack("<Q", urandom(8))[0]


def create_user(email, name):
    """ creates a new API consumer """
    user_token = generate_token()
    while g.redis.sismember(TOKENS, user_token):   # loop until unique
        user_token = generate_token()

    g.redis.sadd(TOKENS, user_token)
    g.cursor.execute(INSERT_USER, [email, user_token, name])
    g.pg_conn.commit()

    return user_token


def get_user(email, name):
    """ returns a users's ID given an email

    If the user does not exist a new user record is created.
    """
    g.cursor.execute(GET_USER, [email])
    user = g.cursor.fetchone()
    if user and g.redis.sismember(TOKENS, user['token']):
        return user['token']
    else:
        return create_user(email, name)


def valid_token():
    """ decorator for authenticated endpoints """
    if 'token' not in request.args:
        raise errors.AppError("NO_TOKEN")

    req_token = request.args['token']
    if not g.redis.sismember(TOKENS, req_token):
        raise errors.AppError("INVALID_TOKEN")
