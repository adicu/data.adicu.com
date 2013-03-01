import argparse
import time
import simplejson as json
import functools

from datetime import datetime

import lib.mongo

def load_data(dump_file=None):
    mongo = lib.mongo.mongo_sync()
    insert_queue = []
    with open(dump_file) as f:
        js = json.loads(f.read())
        for event in js:
            start = "%s %s" % (event["Date"], event["Start"])
            end = "%s %s" % (event["Date"], event["End"])
            event["Start"] = datetime.strptime(start, "%m/%d/%Y %I:%M %p")
            event["End"] = datetime.strptime(end, "%m/%d/%Y %I:%M %p")
            event["Date"] = datetime.strptime(event["Date"], "%m/%d/%Y")
            insert_queue.append(event)
            if len(insert_queue) == 1000:
                print 'submitting batch'
                mongo.uem.insert(insert_queue)
                insert_queue = []
        if insert_queue:
            print 'submitting batch'
            mongo.uem.insert(insert_queue)

def finish_callback(result, error):
    print result

def create():
    pass

def drop():
    mongo = lib.mongo.mongo_sync()
    mongo.drop_collection('uem')


def main():
    parser = argparse.ArgumentParser(description="""Read a directory of uem
            JSON dump file and writes to mongo.""")
    parser.add_argument('--create', action='store_true', help="""create the
            uem collection if it doesn't already exist""")
    parser.add_argument('--drop', action='store_true', help="""drop the
            uem collection""")
    parser.add_argument('--dump_file', help="""file containing the JSON dump""")
    args = parser.parse_args()
    if args.create:
        create_table()
    elif args.drop:
        drop_table()
    else:
        load_data(args.dump_file)

if __name__ == "__main__":
    tornado.ioloop.IOLoop.instance().start()
    main()
