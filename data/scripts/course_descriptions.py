import sys
import argparse
import os
import time
import tornado.ioloop
from lxml import etree

import lib.pg

def load_data(dump_file):
    pg = lib.pg.pg_sync()
    db_query = """UPDATE courses_t SET description=%s WHERE course~~*%s;"""
    query_queue = []
    doc = etree.parse(dump_file)
    courses = doc.findall('course')
    for course in courses:
        department = course.findtext('subject_area_code')
        number = course.findtext('course_number_1')
        description = course.findtext('course_description')
        description = description.replace('\'', '\'\'')
        query_queue.append((description, '%%%s%%' % (department + str(number))))
    if query_queue:
        print 'submitting a batch'
        cursor = pg.cursor()
        cursor.executemany(db_query, query_queue)
        pg.commit()
        cursor.close()
        query_queue = []

def main():
    parser = argparse.ArgumentParser(description="""Read CCIT course description
             dump files and writes to Postgres.""")
    parser.add_argument('dump_files', nargs='+', help="""files containing the
            JSON dump""")
    args = parser.parse_args()
    for dump_file in args.dump_files:
        print 'reading from file %s' % dump_file
        load_data(dump_file)

if __name__ == "__main__":
    tornado.ioloop.IOLoop.instance().start()
    main()
