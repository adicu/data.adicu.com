from struct import unpack
from flask import g, request
from os import urandom, path, environ
import sys
from urlparse import urlparse

# add the parent directory for in-project imports
base_dir = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)
from errors import errors


GET_USER_EMAIL = "SELECT * FROM users_t WHERE email = %s;"
GET_USER_TOKEN = "SELECT * FROM users_t WHERE token = CAST(%s as TEXT);"
GET_DOMAIN = "SELECT * FROM users_t WHERE access = %s;"
INSERT_USER = ('INSERT INTO users_t (email, token, name, rate_limit) '
               'VALUES (%s, %s, %s, %s);')
TOKENS = 'tokens'
DOMAINS = 'domains'
DEFAULT_LIMIT = environ['RATE_LIMIT']
SPLIT_FACTOR = 4    # how to split the hour's api hits


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
    g.cursor.execute(INSERT_USER, [email, user_token, name, DEFAULT_LIMIT])
    g.pg_conn.commit()

    return user_token


def get_user(email, name):
    """ returns a users's ID given an email

    If the user does not exist a new user record is created.
    """
    g.cursor.execute(GET_USER_EMAIL, [email])
    user = g.cursor.fetchone()
    if user and g.redis.sismember(TOKENS, user['token']):
        return user['token']
    else:
        return create_user(email, name)


def check_token_validity():
    """ decorator for authenticated endpoints """
    req_token = request.args['token']
    if not g.redis.sismember(TOKENS, req_token):
        raise errors.AppError("INVALID_TOKEN")

def get_domain():
    if request.referrer:
        o = urlparse(request.referrer)
        return o.netloc
    else:
        return ""

def rate_limit():
    """ limits the user to a set number of requests per 15 minutes """
    if 'token' not in request.args:
        """ Check if referrer is whitelisted under a token """
        domain = get_domain()
        if not g.redis.sismember(DOMAINS, domain):
            raise errors.AppError("NO_TOKEN")
        key = "domains:'{}'".format(domain)
        if not g.redis.exists(key):
            g.cursor.execute(GET_DOMAIN, [domain])
            user = g.cursor.fetchone()
            g.redis.set(key, user['token'])
        req_token = g.redis.get(key)
    else:
        check_token_validity()   # check the token
        req_token = request.args['token']

    key = "rate:{}".format(req_token)
    # confirm key exists, if not instantiate
    if not g.redis.exists(key):
        g.cursor.execute(GET_USER_TOKEN, [req_token])
        user = g.cursor.fetchone()
        g.redis.setex(key, int(user['rate_limit'])/SPLIT_FACTOR,
                      60*60/SPLIT_FACTOR)

    # return error if being limited
    if int(g.redis.get(key)) <= 0:
        raise errors.AppError("RATE_LIMIT")

    g.redis.decr(key)
