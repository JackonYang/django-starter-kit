# -*- coding: utf-8 -*-
import time
import random

import requests

import logging
from django.conf import settings
from django_redis import get_redis_connection

from data.models import Record


url = 'http://kaijiang.zhcw.com/open.jsp?czid=622&format=json&getDay=%d'

_conn = get_redis_connection("default")
logger = logging.getLogger(__name__)


def wait(f):
    lock_name = 'lottery-http-lock'

    def _wrap_func(*args, **kwargs):
        t = max(_conn.ttl(lock_name), settings.DELAY_FORCE_MIN)
        if t > 0:
            logger.info('sleep %s second' % t)
            time.sleep(t)

        n_t = int(random.uniform(settings.DELAY_BOTTOM, settings.DELAY_TOP))
        _conn.setex(lock_name, n_t, 'locking')
        return f(*args, **kwargs)
    return _wrap_func


@wait
def fetch(days=0, timeout=15):
    logger.info('%s days data. fetching...' % days)
    try:
        count = 0
        rsp = requests.get(url % days, timeout=timeout)
        for item in rsp.json().get('iteam', [])[::-1]:
            count += int(Record.create(**item))
        logger.info('%s new data saved' % count)
        if count:
            t_new = 30
            logger.info('sleep %s seconds because of new data got' % t_new)
            time.sleep(t_new)
        return count
    except requests.exceptions.Timeout:
        logger.warning('timeout!')
    except requests.exceptions.ConnectionError:
        logger.error('Connection refused!')
    except Exception:
        logger.exception('fail to fetch data')


def run():
    """ entry point of runscript

    """
    res = None
    while res is None:
        res = fetch(days=9)

    logger.info('keep fetching')

    while True:
        fetch()
