import pika
import redis
from config import config


# redisPool = redis.ConnectionPool(host=config.REDIS_HOST, port=config.CACHE_REDIS_PORT, decode_responses=True)
# MessageQueuePool = pika.BlockingConnection(pika.ConnectionParameters(config.MQ_HOST))