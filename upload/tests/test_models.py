# -*- coding:utf-8 -*-
import pytest
import unittest
from django.test import RequestFactory

from django.contrib.auth import get_user_model

from upload.models import QiniuUploadToken


assertions = unittest.TestCase('__init__')


@pytest.mark.django_db
def test_create_token_img_no_sizekb():
    origin_filename = 'test-no-size.jpg'

    old = QiniuUploadToken.objects.count()
    token = QiniuUploadToken.objects.create_img_token(origin_filename)
    cur = QiniuUploadToken.objects.count()

    assertions.assertEqual(cur, old + 1)
    assertions.assertEqual(token.origin_filename, origin_filename)
    assertions.assertEqual(token.file_ext, '.jpg')
    assertions.assertTrue(token.file_key.endswith('.jpg'))
    assertions.assertTrue(token.bucket)
    assertions.assertTrue(token.token)

    assertions.assertTrue(str(token))


@pytest.mark.django_db
def test_create_token_img_with_sizekb():
    origin_filename = 'test-no-size.jpg'
    size_kb = 1024 * 1024 * 1024

    old = QiniuUploadToken.objects.count()
    token = QiniuUploadToken.objects.create_img_token(origin_filename, size_kb)
    cur = QiniuUploadToken.objects.count()

    assertions.assertEqual(token.size_kb, size_kb)

    assertions.assertEqual(cur, old + 1)
    assertions.assertEqual(token.origin_filename, origin_filename)
    assertions.assertEqual(token.file_ext, '.jpg')
    assertions.assertTrue(token.file_key.endswith('.jpg'))
    assertions.assertTrue(token.bucket)
    assertions.assertTrue(token.token)


@pytest.mark.django_db
def test_create_token_with_request():
    origin_filename = 'test-with-request.jpg'
    ua = 'pytest-request-ua'
    referrer = 'unittest-referrer'
    ip = '127.9.9.1'

    UserModel = get_user_model()
    factory = RequestFactory()

    request = factory.get(
        '/',
        HTTP_USER_AGENT=ua,
        HTTP_REFERER=referrer,
        REMOTE_ADDR=ip
    )
    request.user = UserModel.objects.first()

    old = QiniuUploadToken.objects.count()
    token = QiniuUploadToken.objects.create_img_token(origin_filename, request=request)
    cur = QiniuUploadToken.objects.count()

    assertions.assertEqual(cur, old + 1)
    assertions.assertEqual(token.origin_filename, origin_filename)
    assertions.assertEqual(token.file_ext, '.jpg')
    assertions.assertTrue(token.file_key.endswith('.jpg'))
    assertions.assertTrue(token.bucket)
    assertions.assertTrue(token.token)

    # assertions.assertEqual(token.user.id, request.user.id)
    assertions.assertEqual(token.ua, ua)
    assertions.assertEqual(token.referrer, referrer)
    assertions.assertEqual(token.ip, ip)


@pytest.mark.django_db
def test_create_token_lower_ext():
    origin_filename = 'test-low-ext.JPG'

    old = QiniuUploadToken.objects.count()
    token = QiniuUploadToken.objects.create_img_token(origin_filename)
    cur = QiniuUploadToken.objects.count()

    assertions.assertEqual(cur, old + 1)
    assertions.assertEqual(token.origin_filename, origin_filename)
    assertions.assertEqual(token.file_ext, '.jpg')
    assertions.assertTrue(token.file_key.endswith('.jpg'))
    assertions.assertTrue(token.bucket)
    assertions.assertTrue(token.token)
