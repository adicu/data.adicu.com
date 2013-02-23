import os
import tornadoredis

redis_host = os.getenv('REDIS_HOST')
redis_port = os.getenv('REDIS_PORT')
redis_pass = os.getenv('REDIS_PASSWORD')

redis = tornadoredis.Client(host=redis_host, port=int(redis_port),
        password=redis_pass)
redis.connect()
