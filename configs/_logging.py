# -*- coding: utf-8 -*-
import os
import logging.config

from utils.proj_vars import (
    HOSTNAME,
)


# PARAMS
LOG_ROOT_DIR = os.getenv('LOG_ROOT_DIR', 'log')
ROLLBAR_TOKEN = os.getenv('ROLLBAR_TOKEN', 'access_token')
ROLLBAR_ENV = os.getenv('ROLLBAR_ENV', HOSTNAME)
ROLLBAR_ENABLED = (os.getenv('ROLLBAR_ENABLED', 'FALSE').upper() == 'TRUE')


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
        'require_rollbar_enabled': {
            '()': 'utils.log.RequireRollbarEnabled',
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
            'filters': ['require_rollbar_enabled'],
            'access_token': ROLLBAR_TOKEN,
            'environment': ROLLBAR_ENV,
            'class': 'rollbar.logger.RollbarHandler',
        },
        'django_file': {
            'level': 'INFO',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'django.log'),
            'formatter': 'verbose',
        },
        'access_warning_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'access-warning.log'),
            'formatter': 'verbose',
        },
        'access_error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'access-error.log'),
            'formatter': 'verbose',
        },
        'elasticsearch_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'elasticsearch.log'),
            'formatter': 'verbose',
        },
        'library_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'library.log'),
            'formatter': 'verbose',
        },
        'root_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'root.log'),
            'formatter': 'verbose',
        },
        'warning_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'warning.log'),
            'formatter': 'verbose',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'error.log'),
            'formatter': 'verbose',
        },
        'client_file': {
            'level': 'INFO',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'client.log'),
            'formatter': 'verbose',
        },
        'openapi_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'openapi.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'handlers': ['console', 'django_file', 'warning_file', 'error_file'],
            'propagate': False,
        },
        'django.request': {
            'level': 'DEBUG',
            'handlers': ['access_warning_file', 'access_error_file'],
        },
        'django.security': {
            'handlers': ['django_file', 'rollbar'],
            'level': 'DEBUG',
        },
        'client': {
            'level': 'DEBUG',
            'handlers': ['rollbar', 'client_file'],
        },
        'openapi': {
            'level': 'DEBUG',
            'handlers': ['rollbar', 'openapi_file', 'access_warning_file', 'access_error_file'],
        },
        'elasticsearch': {
            # do not log all the elasticsearch messages
            'level': 'WARNING',
            'handlers': ['elasticsearch_file', 'warning_file', 'error_file'],
            'propagate': False,
        },
        'gensim': {
            'propagate': False,
            'handlers': ['library_file', ],
        },
        'summa': {
            'propagate': False,
            'handlers': ['library_file', ],
        },
        'theano': {
            'propagate': False,
            'handlers': ['library_file', ],
        },
        'urllib3': {
            'propagate': False,
            'handlers': ['library_file', ],
        },
        'jieba': {
            'propagate': False,
            'handlers': ['library_file', ],
        },
        'langid': {
            'propagate': False,
            'handlers': ['library_file', ],
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['root_file', 'rollbar', 'warning_file', 'error_file'],
    },
}


logging.config.dictConfig(LOGGING)
