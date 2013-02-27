import sys
import argparse
import os
import tornado.ioloop
import bson.json_util as json
from datetime import datetime
import functools

import lib.mongo

def load_data(dump_file, social, students, alumni):
    mongo = lib.mongo.mongo_sync()
    insert_queue = []
    with open(dump_file) as f:
        js = json.loads(f.read())
        for item in js:
            if social:
                item["social_media"] = True
            elif students:
                if item["Date"] != "TBD":
                    item["Date"] = datetime.strptime(item["Date"],"%m/%d/%Y")
                item["student_events"] = True
            else:
                item["DATE"] = datetime.strptime(item["DATE"], "%B %d, %Y")
                if "DATE END" in item:
                    item["DATE END"] = datetime.strptime(item["DATE END"], "%B %d, %Y")
                item["alumni_events"] = True
            insert_queue.append(item)
            if len(insert_queue) == 1000:
                print 'submitting batch'
                mongo.affairs.insert(insert_queue)
                insert_queue = []
        if insert_queue:
            print 'submitting batch'
            mongo.affairs.insert(insert_queue)

def finish_callback(result, error):
    print result

def create():
    pass

def drop():
    mongo = lib.mongo.mongo_sync()
    mongo.drop_collection('affairs')

def main():
    parser = argparse.ArgumentParser(description="""Read a directory of
    affairs data JSON dump file and writes to Mongo.""")
    parser.add_argument('--drop', action='store_true', help="""drop the
            affairs collection""")
    parser.add_argument('--create', action='store_true', help="""create the
            affairs collection""")
    parser.add_argument('--social', action='store_true', help="""load the
            social docs into the collection""")
    parser.add_argument('--students', action='store_true', help="""load the
            student docs into the collection""")
    parser.add_argument('--alumni', action='store_true', help="""load the
            alumni docs into the collection""")

    parser.add_argument('--dump_file', help="""file containing the JSON dump""")
    args = parser.parse_args()
    if args.drop:
        drop()
    elif not (args.social or args.students or args.alumni):
        print "You must specify either --social --students or --alumni"
    elif args.social and (args.students or args.alumni) or (args.students and args.alumni):
        print "You can't specify more than two arguments"
    else:
        load_data(args.dump_file, args.social, args.students, args.alumni)

if __name__ == "__main__":
    main()
