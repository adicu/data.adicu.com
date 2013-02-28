import os
import motor
import functools
import mongo as m

class TokenAuth:
    def __init__(self):
        self.collection = m.mongo_aync()["users"]

    def validate_token(self, token, callback):
        internal_callback = functools.partial(self._on_mongo_response,
                callback=callback)
        self.collection.find_one({"token":token}, callback=internal_callback)

    def _on_mongo_response(self, response, error, callback=None):
        if response:
            callback(True)
        else:
            callback(False)

