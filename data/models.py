# -*- Encoding: utf-8 -*-
import logging
from django.db import models

# UNIQUE constraint Exception
from django.db import IntegrityError


logger = logging.getLogger(__name__)


class Record(models.Model):
    """ 开奖记录

    """

    day = models.CharField(u'开奖日期', max_length=10)
    timestamp = models.CharField(u'开奖时间', max_length=8)
    seq = models.PositiveSmallIntegerField(u'当天开奖期号')

    win_str = models.CharField(u'开奖结果', max_length=23)

    @classmethod
    def create(cls, kjIssue, kjDate, kjZNum, **kwargs):
        seq = int(kjIssue[-3:])
        day, timestamp = kjDate.split()
        win_str = kjZNum

        try:
            obj, created = cls.objects.update_or_create(
                seq=seq, day=day, timestamp=timestamp, win_str=win_str)
        except IntegrityError as e:
            created = False
            if 'unique constraint' in e.message.lower():
                msg = 'UNIQUE constraint failed: {}~No.{:0>2d}({})'.format(
                    day, seq, win_str)
                logger.warning(msg)
            else:
                msg = 'save data failed: {}~No.{:0>2d}({})'.format(
                    day, seq, win_str)
                logger.exception(msg)
        return created

    @property
    def issue(self):
        return '{}~No.{:0>2d}'.format(self.day, self.seq)

    @property
    def time(self):
        """开奖时间"""
        return '{} {}'.format(self.day, self.timestamp)

    @property
    def win(self):
        """开奖号码"""
        return map(int, self.win_str.split())

    def __unicode__(self):
        return self.issue

    class Meta:
        verbose_name = u'开奖数据'
        verbose_name_plural = verbose_name

        unique_together = ('day', 'seq')

        ordering = ['-day', '-seq']
