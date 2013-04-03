import os
import motor
import functools
import mongo as m

from bson.objectid import ObjectId, InvalidId

class TokenAuth:
    def __init__(self):
        self.collection = m.mongo_aync()["users"]

    def validate_token(self, token, callback):
        internal_callback = functools.partial(self._on_mongo_response,
                callback=callback)
        try:
            object_id = ObjectId(token)
        except InvalidId:
            object_id = ObjectId()
        self.collection.find_one({"_id": object_id }, callback=internal_callback)

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
            internal_callback = functools.partial(self._on_mongo_insert, callback=callback)
            self.collection.insert(user, callback=internal_callback)
        else:
            callback(response, error)
    
    def _on_mongo_insert(self, response, error, callback):
        if error:
            callback(None, error)
        else:
            internal_callback = functools.partial(self._on_mongo_find, callback=callback)
            self.collection.find_one({"_id":response}, callback=internal_callback)
