import os
import motor
import functools
import tornado.gen

from pymongo import MongoClient


mongo_user  = os.getenv('MONGO_USER')
mongo_pass  = os.getenv('MONGO_PASSWORD')
mongo_host  = os.getenv('MONGO_HOST')
mongo_port  = os.getenv('MONGO_PORT')
mongo_db    = os.getenv('MONGO_DB')
mongo_limit = os.getenv('MONGO_LIMIT')

mongo_uri = "mongodb://%s:%s@%s:%s/%s" % (mongo_user, mongo_pass,
        mongo_host, mongo_port, mongo_db)

def mongo_aync():
    return motor.MotorClient(host=mongo_uri).open_sync()[mongo_db]

def mongo_sync():
    return MongoClient(mongo_uri)[mongo_db]

class MongoQuery:
    def __init__(self, model=None, model_functions=None):
        self.mongo = mongo_aync()

    @tornado.gen.engine
    def execute(self, args, page=0, limit=0, callback=None):
        results = []

        query, arguments = self.build_mongo_query(args)

        if limit:
            arguments["limit"] = limit
        cursor = collection.find(arguments, limit=limit, skip=page*limit)
        while (yield cursor.fetch_next):
            results.append(cursor.next_object())
        response = [self.model.build_response_dict(result) for result in results]
        callback(response)

    def build_mongo_query(self, arguments):
        model = self.model
        # slug is a list, each with (key, value)
        slug = [self.attr_func_wrap(key, value) for key, value in
                arguments.iteritems()]
        return dict(slug)
    
    def attr_func_wrap(self, key, value):
        func = getattr(self.model_functions, key)
        value, fragment = func(value)
        return fragment, value
