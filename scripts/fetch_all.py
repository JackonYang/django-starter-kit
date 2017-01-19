# -*- coding:utf-8 -*-
import logging

from .crawler import fetch


logger = logging.getLogger(__name__)


def run():
    """ entry point of runscript

    """
    logger.info('download data started')
    fetch(days=9)
    logger.info('download data finished')
