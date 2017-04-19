import redis

from pastes_api import config

cache = redis.StrictRedis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB
)