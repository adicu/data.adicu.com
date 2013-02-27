import argparse
import csv
import os
import sys
import time

import lib.pg

schema =  [
    ("RoomLocationArea", "varchar(32)"),
    ("ResidentialArea", "varchar(32)"),
    ("RoomLocation", "varchar(32)"),
    ("RoomLocationSection", "varchar(32)"),
    ("RoomLocationFloorSuite", "varchar(32)"),
    ("IsSuite", "boolean"),
    ("FloorSuiteWebDescription", "varchar(32)"),
    ("Room", "varchar(32)"),
    ("RoomArea", "int"),
    ("RoomSpace", "varchar(32)"),
    ("RoomType", "varchar(64)"),
    ("AY1213RSStatus", "varchar(32)"),
    ("PointValue", "double precision"),
    ("LotteryNumber", "int"),
]


def create_table():
    print 'Creating housing table with proper schema...'
    pg = lib.pg.pg_sync()
    db_query = 'CREATE TABLE IF NOT EXISTS housing_t (%s);' % (", ".join(
            ['%s %s' % column for column in schema]))
    cursor = pg.cursor()
    cursor.execute(db_query)
    pg.commit()

def drop_table():
    print 'Dropping housing table...'
    pg = lib.pg.pg_sync()
    db_query = 'DROP TABLE housing_t;'
    cursor = pg.cursor()
    cursor.execute(db_query)
    pg.commit()

def _typify(value, data_type):
    if data_type.startswith('varchar'):
        return '%s' % value.replace('\'','\\\'')
    if data_type == 'int':
        return str(int(value)) if value else str(0)
    if data_type == 'double precision':
        return str(float(value)) if value else str(0.0)
    if data_type == 'boolean':
        return value # we're given the values as 'TRUE' or 'FALSE'
    else:
        return None

def load_data(dump_file):
    pg = lib.pg.pg_sync()
    query_queue = []
    with open(dump_file) as f:
        reader = csv.reader(f)
        reader.next() # skip header row
        for row in csv.reader(f):
            columns = [name for (name, data_type) in schema]
            values = [_typify(value, data_type) for ((name, data_type), value) in zip(schema, row)]
            db_query = 'INSERT INTO housing_t (%s) VALUES (%s);' % (
                    ', '.join(columns), ', '.join(["%s"] * len(values)))
            query_queue.append(values)
            if len(query_queue) == 1000:
                print 'submitting a batch'
                cursor = pg.cursor()
                cursor.executemany(db_query, query_queue)
                pg.commit()
                cursor.close()
                query_queue = []
        if query_queue:
            print 'submitting a batch'
            cursor = pg.cursor()
            cursor.executemany(db_query, query_queue)
            pg.commit()
            cursor.close()
            query_queue = []

def main():
    parser = argparse.ArgumentParser(description="""Read a housing data CSV
            dump file and writes to Postgres.""")
    parser.add_argument('--create', action='store_true', help="""create the
            housing_t table if it doesn't already exist""")
    parser.add_argument('--drop', action='store_true', help="""drop the
            housing_t table""")
    parser.add_argument('dump_file', help="""file containing the CSV dump""")
    args = parser.parse_args()
    if args.create:
        create_table()
    elif args.drop:
        drop_table()
    else:
        load_data(args.dump_file)

if __name__ == "__main__":
    main()
