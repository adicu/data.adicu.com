
from struct import unpack
from flask import g
from os import urandom


GET_USER = "SELECT * FROM users_t WHERE email = %s;"
INSERT_USER = ('INSERT INTO users_t (email, token, name) '
               'VALUES (%s, %s, %s);')


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
    g.cursor.execute(INSERT_USER, [email, user_token, name])
    g.pg_conn.commit()
    return user_token


def get_user(email, name):
    """ returns a users's ID given an email

    If the user does not exist a new user record is created.
    """
    g.cursor.execute(GET_USER, [email])
    user = g.cursor.fetchone()
    if user:
        return user['token']
    else:
        return create_user(email, name)
