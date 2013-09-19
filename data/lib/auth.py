import os
import motor
import functools
import uuid

from bson.objectid import ObjectId, InvalidId
from lib.pg import pg_async

class TokenAuth:
    def __init__(self):
        self.pg = pg_async()

    def validate_token(self, token, callback):
        internal_callback = functools.partial(self._on_pg_response,
                callback=callback)
        query = "SELECT email FROM users_t WHERE token=%s"
        self.pg.execute(query, (token,), callback=internal_callback)

    def _on_pg_response(self, cursor, callback=None):
        result = cursor.fetchone()
        callback(result is not None)

class UserAuth:
    def __init__(self):
        self.pg = pg_async()

    def add_user(self, user, callback):
        internal_callback = functools.partial(self._on_pg_select,
                user=user, callback=callback)
        query = "SELECT email, token FROM users_t WHERE email=%s" 
        self.pg.execute(query, (user['email'],), callback=internal_callback)

    def _on_pg_select(self, cursor, user=None, callback=None):
        result = cursor.fetchone()
        if not result:
            user['token'] = uuid.uuid1().get_hex()

            internal_callback = functools.partial(self._on_pg_insert, 
                    callback=callback, user=user)
            query = "INSERT INTO users_t (email, token) VALUES (%s, %s)"
            self.pg.execute(query, (user['email'], user['token']), 
                    callback=internal_callback)
        else:
            callback({'user': result[0], 'token': result[1]}, None)

    def _on_pg_insert(self, cursor, user=None, callback=None):
        callback(user, None)
