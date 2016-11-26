# -*- coding: utf-8 -*-
from django.db import models

import json
import os
import uuid

from django.conf import settings
from qiniu import Auth


q = Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)


image_bucket = 'user-image-test'


qiniu_return_body = json.dumps({
    'name': '$(fname)',
    'size': '$(fsize)',
    'key': '$(key)',
    'mimeType': '$(mimeType)',
    'hash': '$(etag)',
})


def policy_tmpl(bucket, size_limit):
    return {
        'scope': bucket,
        'insertOnly': 1,
        'returnBody': qiniu_return_body,
        'fsizeLimit': size_limit,
        'detectMime': 0,
    }


def image_policy(bucket):
    return policy_tmpl(
        bucket=bucket,
        size_limit=1024 * 1024 * 100,  # 100 MB
    )


class QiniuUploadTokenManager(models.Manager):
    def create_img_token(self, origin_filename, size_kb=-1, request=None):
        bucket = image_bucket
        policy = image_policy(image_bucket)
        return self._create_token(bucket, policy, origin_filename, size_kb, request)

    def _create_token(self, bucket, policy, origin_filename, size_kb, request=None):
        filename, ext = os.path.splitext(origin_filename)
        ext = ext.lower()
        new_filename = '%s%s' % (uuid.uuid4().hex, ext)

        data = {
            'origin_filename': origin_filename,
            'size_kb': size_kb,
            'bucket': bucket,
            'token': q.upload_token(bucket=bucket, policy=policy),
            'file_key': new_filename,
            'file_ext': ext,
        }

        if request:
            user = request.user
            data['user'] = user if user.is_authenticated() else None
            data['referrer'] = request.META.get('HTTP_REFERER', "")
            data['ua'] = request.META.get('HTTP_USER_AGENT', "")
            data['ip'] = request.META.get('REMOTE_ADDR', "")

        obj = self.model(**data)
        obj.save()
        return obj


class QiniuUploadToken(models.Model):
    # token info
    token = models.CharField(max_length=255)
    bucket = models.CharField(max_length=100)
    file_key = models.CharField(max_length=255)

    # origin file info
    origin_filename = models.CharField(max_length=255)
    size_kb = models.IntegerField(default=-1)
    file_ext = models.CharField(max_length=100)

    # user info
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    referrer = models.CharField(max_length=500, default='')
    ua = models.CharField(max_length=500, default='')
    ip = models.CharField(max_length=100, default='')

    create_time = models.DateTimeField(auto_now_add=True)
    last_modified_time = models.DateTimeField(auto_now=True)

    objects = QiniuUploadTokenManager()

    def __unicode__(self):
        return u'%s(user-%s)' % (self.file_key, self.user)

    class Meta:
        pass
