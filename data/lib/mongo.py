import os
import motor

mongo_user = os.getenv('MONGO_USER')
mongo_pass = os.getenv('MONGO_PASSWORD')
mongo_host = os.getenv('MONGO_HOST')
mongo_port = os.getenv('MONGO_PORT')
mongo_db   = os.getenv('MONGO_DB')

mongo_uri = "mongodb://%s:%s@%s:%s/%s" % (mongo_user, mongo_pass,
        mongo_host, mongo_port, mongo_db)

mongo = motor.MotorClient(host=mongo_uri)
