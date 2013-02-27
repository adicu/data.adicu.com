import sys
import argparse
import os
import time
import tornado.ioloop

import simplejson as json

import lib.mongo

def main():
    parser = argparse.ArgumentParser(description="""Read a directory of courses
            JSON dump file and writes to Postgres.""")
    parser.add_argument('--create', action='store_true', help="""create the
            courses_t table if it doesn't already exist""")
    parser.add_argument('--drop', action='store_true', help="""drop the
            courses_t table""")
    parser.add_argument('dump_file', help="""file containing the JSON dump""")
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
