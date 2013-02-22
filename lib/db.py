import os
import momoko
import tornadoredis
import motor

env = os.environ

# Postgres
pg_host = env('PG_HOST')
pg_port = env('PG_PORT')
pg_db   = env('PG_DB')
pg_user = env('PG_USER')
pg_pass = env('PG_PASSWORD')
dsn = 'dbname=%s user=%s password=%s host=%s port=%s' % (
            pg_db, pg_user, pg_pass, pg_host, pg_port)

pg = momoko.Pool(dsn=dsn,
        minconn=1,
        maxconn=10,
        cleanup_timeout=10
)

# Redis
redis_host = env('REDIS_HOST')
redis_port = env('REDIS_PORT')
redis_pass = env('REDIS_PASSOWRD')

redis = tornadoredis.Client(host=redis_host, port=redis_port,
        password=redis_password)
redis.connect()

# Mongo
mongo_user = env('MONGO_USER')
mongo_pass = env('MONGO_PASSWORD')
mongo_host = env('MONGO_HOST')
mongo_port = env('MONGO_PORT')
mongo_db   = env('MONGO_DB')

mongouri = "mongodb://%s:%s@%s:%s/%s" % (mongo_user, mongo_pass,
        mongo_host, mongo_port, mongo_db)

mongo = motor.MotorClient(host=mongouri)


def get_pg:
    return pg

def get_redis:
    return redis

def get_mongo:
    return mongo
