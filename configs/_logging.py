# -*- coding: utf-8 -*-
import os
import logging.config


# PARAMS
LOG_ROOT_DIR = 'log'

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
        'handlers': ['root_file'],
    },
}


logging.config.dictConfig(LOGGING)
