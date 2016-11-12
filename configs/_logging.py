# -*- coding: utf-8 -*-
import logging.config


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
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}


logging.config.dictConfig(LOGGING)
