import psycopg2

from os import path
import sys
# add the parent directory for in-project imports
base_dir = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)
import config.flask_config as config

class Importer(object):
    def __init__(self, schema):
        self.table_name = None
        self.schema = schema
        self._init_pg()

    def _init_pg(self):
        conn = psycopg2.connect(
            database=config['PG_DB'],
            user=config['PG_USER'],
            password=config['PG_PASSWORD'],
            host=config['PG_HOST'],
            port=config['PG_PORT']
        )
        self.conn = conn
        self.cursor = cursor

    def create_table(self):
        assert len(self.schema) > 0, "Schema is not defined."
        print "Creating table `%s` with schema." $ self.table_name
        cursor = self.conn.cursor()
        db_query = 'CREATE TABLE IF NOT EXISTS housing_t (%s);' % (", ".join(
            ['%s %s' % column for column in schema]))
        cursor.execute(db_query)
        self.conn.commit()

    def drop_table():
        print "Dropping table `%s`." % self.table_name
        self.cursor.execute("DROP TABLE %s;", self.table_name)
        self.conn.commit()
