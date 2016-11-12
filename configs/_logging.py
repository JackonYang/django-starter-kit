# -*- coding: utf-8 -*-
import os
import logging.config


# PARAMS
LOG_ROOT_DIR = os.getenv('LOG_ROOT_DIR', 'log')
ROLLBAR_TOKEN = os.getenv('ROLLBAR_TOKEN', 'access_token')
ROLLBAR_ENV = os.getenv('ROLLBAR_ENV', 'production')


if not os.path.exists(LOG_ROOT_DIR):
    os.makedirs(LOG_ROOT_DIR)


# the automatic configuration process is disabled, not logging itself.
LOGGING_CONFIG = None


# manually configures logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    'formatters': {
        'verbose': {
            'format': '%(asctime)s | %(levelname)s | %(message)s | %(name)s | %(filename)s-%(lineno)s: %(funcName)s',
        },
        'basic': {
            'format': '%(asctime)s | %(levelname)s | %(message)s',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'basic',
        },
        # https://github.com/rollbar/pyrollbar/blob/master/rollbar/logger.py
        'rollbar': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'access_token': ROLLBAR_TOKEN,
            'environment': ROLLBAR_ENV,
            'class': 'rollbar.logger.RollbarHandler'
        },
        'django_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'django.log'),
            'formatter': 'verbose',
        },
        'root_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'root.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'handlers': ['console', 'django_file'],
            'propagate': False,
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['root_file', 'rollbar'],
    },
}


logging.config.dictConfig(LOGGING)
