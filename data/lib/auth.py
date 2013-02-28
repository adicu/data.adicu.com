import os
import motor
import functools
import mongo as m

from bson.objectid import ObjectId

class TokenAuth:
    def __init__(self):
        self.collection = m.mongo_aync()["users"]

    def validate_token(self, token, callback):
        internal_callback = functools.partial(self._on_mongo_response,
                callback=callback)
        self.collection.find_one({"_id":ObjectId(token)}, callback=internal_callback)

    def _on_mongo_response(self, response, error, callback=None):
        if response:
            callback(True)
        else:
            callback(False)

class UserAuth:
    def __init__(self):
        self.collection = m.mongo_aync()["users"]

    def add_user(self, user, callback):
        internal_callback = functools.partial(self._on_mongo_find,
                user=user, callback=callback)
        self.collection.find_one({"email":user["email"]}, callback=internal_callback)

    def _on_mongo_find(self, response, error, user=None, callback=None):
        if not response:
            self.collection.insert(user, callback=callback)
        else:
            callback(response, error)
