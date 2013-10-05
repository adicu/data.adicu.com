#!/usr/bin/env python

from lib.pg import pg_sync
from tornado.httpclient import HTTPClient
import os
import json

BATCH_SIZE = 500

COURSE_COLUMNS = [
    "Course",
    "CourseFull",
    "DepartmentCode", 
    "DepartmentName", 
    "CourseTitle", 
    "CourseSubtitle", 
    "Description"
]

def add_bulk_item(batch, pgrow, es_index, es_type):
    action = { 'index' : {
        "_index" : es_index,
        "_type" : es_type,
        "_id" : pgrow[0]
    }}
    source = {}
    for i, key in enumerate(COURSE_COLUMNS):
        source[key] = pgrow[i]
    source['Term'] = pgrow[len(COURSE_COLUMNS)]
    source['Instructor'] = pgrow[len(COURSE_COLUMNS) + 1]

    batch.append(action)
    batch.append(source)

def submit_batch(base_url, batch):
    print("Submitting a batch")
    http = HTTPClient()
    url = base_url + '_bulk'
    body = '\n'.join(json.dumps(doc) for doc in batch)
    resp = http.fetch(url, method = 'POST', body = body)
    resp.rethrow()

def import_data():
    pg = pg_sync()

    es_index = os.getenv('ES_INDEX')
    if not es_index:
        raise Exception("ES_INDEX variable not set")
    es_host = os.getenv('ES_HOST', 'localhost')
    es_port = os.getenv('ES_PORT', '9200')
    es_type = 'courses'
    base_url = 'http://' + es_host + ':' + es_port + '/'
    
    batch = []
    query = ('SELECT %s, array_agg(DISTINCT s.term) AS \"term\", '
             'array_agg(DISTINCT s.instructor1name) as \"instructor\" '
             'FROM courses_v2_t c JOIN sections_v2_t s '
             'ON c.course = s.course GROUP BY c.course'
            ) % ', '.join('c.' + colname for colname in COURSE_COLUMNS)
    cursor = pg.cursor()
    cursor.execute(query)

    for row in cursor:
        add_bulk_item(batch, row, es_index, es_type)
        if len(batch) == BATCH_SIZE:
            submit_batch(base_url, batch)
            del batch[:] # empty out batch so we can add more to it

    # if there are any more items in the batch, submit them
    if len(batch) > 0:
        submit_batch(base_url, batch)

if __name__ == '__main__':
    import_data()
