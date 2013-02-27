import sys
import argparse
import os
import tornado.ioloop
import bson.json_util as json
from datetime import datetime
import functools

import lib.mongo

def load_data(dump_file=None):
    mongo = lib.mongo.mongo_sync()
    insert_queue = []
    with open(dump_file) as f:
        js = json.loads(f.readline())
        for i, meal in enumerate(js["meals"]):
            meal["day"] = datetime.strptime(meal["day"], "%m-%d-%Y")
            meal["_id"] = i
            insert_queue.append(meal)
            if len(insert_queue) == 1000:
                print 'submitting batch'
                mongo.dining.insert(insert_queue)
                insert_queue = []
        if insert_queue:
            print 'submitting batch'
            mongo.dining.insert(insert_queue)

def finish_callback(result, error):
    print result

def create():
    pass

def drop():
    mongo = lib.mongo.mongo_aync()
    mongo.drop_database('dining')

def main():
    parser = argparse.ArgumentParser(description="""Read a directory of dining
    data JSON dump file and writes to Mongo.""")
    parser.add_argument('--drop', action='store_true', help="""drop the
            dining collection""")
    parser.add_argument('--create', action='store_true', help="""create the
            dining collection""")
    parser.add_argument('dump_file', help="""file containing the JSON dump""")
    args = parser.parse_args()
    if args.drop:
        drop()
    else:
        load_data(args.dump_file)

if __name__ == "__main__":
    main()
