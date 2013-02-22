import os
import momoko
import tornadoredis
import motor
import psycopg2

env = os.environ

# Postgres
pg_host = env['PG_HOST']
pg_port = env['PG_PORT']
pg_db   = env['PG_DB']
pg_user = env['PG_USER']
pg_pass = env['PG_PASSWORD']
dsn = 'dbname=%s user=%s password=%s host=%s port=%s' % (
            pg_db, pg_user, pg_pass, pg_host, pg_port)

pg_async = momoko.BlockingClient({
    'host': pg_host,
    'database': pg_db,
    'port': pg_port,
    'user': pg_user,
    'password': pg_pass,
    'min_conn': 1,
    'max_conn': 20,
    'cleanup_timeout': 5
})
pg_sync = psycopg2.connect(database=pg_db, user=pg_user, password=pg_pass,
        host=pg_host, port=pg_port)

# Redis
redis_host = env['REDIS_HOST']
redis_port = env['REDIS_PORT']
redis_pass = env['REDIS_PASSWORD']

redis = tornadoredis.Client(host=redis_host, port=int(redis_port),
        password=redis_pass)
redis.connect()

# Mongo
mongo_user = env['MONGO_USER']
mongo_pass = env['MONGO_PASSWORD']
mongo_host = env['MONGO_HOST']
mongo_port = env['MONGO_PORT']
mongo_db   = env['MONGO_DB']

mongouri = "mongodb://%s:%s@%s:%s/%s" % (mongo_user, mongo_pass,
        mongo_host, mongo_port, mongo_db)

mongo = motor.MotorClient(host=mongouri)


