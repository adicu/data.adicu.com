import argparse
import time
import simplejson as json

import lib.pg

schema = [

    ]

def create_table():
    print 'Creating uem table with proper schema...'
    pg = lib.pg.pg_sync()
    db_query = 'CREATE TABLE IF NOT EXISTS uem_t (%s);' % (", ".join(
            ['%s %s' % column for column in schema]))
    cursor = pg.cursor()
    cursor.execute(db_query)
    pg.commit()


def drop_table():
    print 'Dropping uem table...'
    pg = lib.pg.pg_sync()
    db_query = 'DROP TABLE uem_t;'
    cursor = pg.cursor()
    cursor.execute(db_query)
    pg.commit()


def _typify(value, data_type):
    if data_type.startswith('varchar'):
        return '%s' % value.replace('\'','\\\'')
    if data_type == 'int':
        return str(int(value)) if value else 0
    if data_type == 'time':
        return '%sM' % value # given data is in form '09:00A'
    else:
        return None


def load_data(dump_file):
    pg = lib.pg.pg_sync()
    query_queue = []
    with open(dump_file) as f:
         for event in json.load(f):
             pairs = [(name, _typify(event[name], data_type)) for (name, data_type) in schema]
             [columns, values] = zip(*pairs)
             db_query = 'INSERT INTO uem_t (%s) VALUES (%s);' % (
                     ', '.join(columns), ', '.join(["%s"] * len(values)))
             query_queue.append(values)
             if len(query_queue) == 1000:
                 print 'submitting a batch'
                 cursor = pg.cursor()
                 cursor.executemany(db_query, query_queue)
                 pg.commit()
                 cursor.close()
                 query_queue = []


def main():
    parser = argparse.ArgumentParser(description="""Read a directory of uem
            JSON dump file and writes to Postgres.""")
    parser.add_argument('--create', action='store_true', help="""create the
            uem_t table if it doesn't already exist""")
    parser.add_argument('--drop', action='store_true', help="""drop the
            uem_t table""")
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
