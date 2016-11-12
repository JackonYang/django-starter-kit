# -*- coding: utf-8 -*-

import os

# variables that read from environment
REDIS_CONN = os.getenv('REDIS_CONN', 'redis://127.0.0.1:6379/2')


# cache with django-redis
# http://niwinz.github.io/django-redis/latest/
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_CONN,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
