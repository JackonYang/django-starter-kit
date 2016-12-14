# -*- coding:utf-8 -*-
from django.db import models

from django.conf import settings


class Tag(models.Model):
    name = models.CharField(u"名称", max_length=16, unique=True)
    desc = models.TextField(u"简要描述", default='', blank=True)

    def __unicode__(self):
        return "Tag<%s>" % self.name

    class Meta:
        verbose_name = u"标签"
        verbose_name_plural = verbose_name


class UserText(models.Model):
    text = models.TextField(u'Text')
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)

    last_modified_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.brief()

    class Meta:
        verbose_name = u"用户文本"
        verbose_name_plural = verbose_name

    def brief(self):
        return self.text[:10]
