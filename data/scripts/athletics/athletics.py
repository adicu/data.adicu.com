import sys
import argparse
import os
import tornado.ioloop
import simplejson as json
from datetime import datetime

import lib.mongo

def load_data(dump_file=None):
    mongo = lib.mongo.mongo_sync()
    insert_queue = []
    with open(dump_file) as f:
        js = json.loads(f.readline())
        for sport, value in js.iteritems():
            for feed, matches in value.iteritems():
                for match in matches:
                    match["time"] = datetime.strptime(match["time"], "%a, %d %b %Y %H:%M:%S EST")
                    match["feed"] = feed
                    match["sport"] = sport
                    insert_queue.append(match)
                    if len(insert_queue) == 1000:
                        print 'submitting batch'
                        mongo.athletics.insert(match)
                        insert_queue = []
        if insert_queue:
            print 'submitting batch'
            mongo.athletics.insert(insert_queue)

def finish_callback(result, error):
    print error
    print result

def create():
    pass

def drop():
    mongo = lib.mongo.mongo_aync()
    mongo.drop_collection('athletics')

def main():
    parser = argparse.ArgumentParser(description="""Read a JSON dump file of
        athletics and writes to Mongo.""")
    parser.add_argument('--create', action='store_true', help="""Create the
            athletics collection if it doesn't already exist""")
    parser.add_argument('--drop', action='store_true', help="""drop the
            athletics collection""")
    parser.add_argument('--dump_file', help="""file containing the JSON dump""")
    args = parser.parse_args()
    if args.create:
        create_table()
    elif args.drop:
        drop()
    else:
        load_data(args.dump_file)

if __name__ == "__main__":
    tornado.ioloop.IOLoop.instance().start()
    main()
