import sys
import argparse
import os
import tornado.ioloop
import simplejson as json

import lib.mongo

def create():
    

def drop():


def load_data(dump_file):
    mongo = lib.mongo.mongo_aync()
    dining = mongo.dining
    insert_queue = []
    with open(dump_file) as f:
        js = json.load(f)
        for meal in js["meals"]:
            meal["day"] = time.strptime(meal["day"], "%m-%d-%Y")
            insert_queue.append(meal)
            if len(query_queue) == 1000:
                dining.insert(insert_queue, callback=_finish)
                insert_queue = []
        dining.insert(insert_queue, callback=_finish)

def _finish(result, error)
    print result

def main():
    parser = argparse.ArgumentParser(description="""Read a directory of dining
    data JSON dump file and writes to Mongo.""")
    parser.add_argument('--create', action='store_true', help="""create the
            dining collection if it doesn't already exist""")
    parser.add_argument('--drop', action='store_true', help="""drop the
            dining collection""")
    parser.add_argument('dump_file', help="""file containing the JSON dump""")
    args = parser.parse_args()
    if args.create:
        create()
    elif args.drop:
        drop()
    else:
        load_data(args.dump_file)

if __name__ == "__main__":
    tornado.ioloop.IOLoop.instance().start()
    main()
