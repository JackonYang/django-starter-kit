# -*- coding:utf-8 -*-
import pytest
import unittest

from upload.models import QiniuUploadToken
from upload.serializers import UploadTokenSerializer


assertions = unittest.TestCase('__init__')


@pytest.mark.django_db
def test_obj2data():
    token = QiniuUploadToken.objects.create_img_token('test.jpg')
    serializer = UploadTokenSerializer(token)
    data = serializer.data

    exception = [
        'token',
        'file_key',
        'file_ext',
        # 'user',
        'create_time',
        'origin_filename',
        'size_kb',
    ]

    assertions.assertItemsEqual(data.keys(), exception)


@pytest.mark.django_db
def test_data2obj_name_only():

    data = {
        'origin_filename': 'serializer.test',
    }

    serializer = UploadTokenSerializer(data=data)
    res = serializer.is_valid()

    assertions.assertTrue(res)


@pytest.mark.django_db
def test_data2obj_int_sizekb():

    data = {
        'origin_filename': 'serializer.test',
        'size_kb': 199,
    }

    serializer = UploadTokenSerializer(data=data)
    res = serializer.is_valid()

    assertions.assertTrue(res)


@pytest.mark.django_db
def test_data2obj_float_sizekb():

    data = {
        'origin_filename': 'serializer.test',
        'size_kb': 199.9,
    }

    serializer = UploadTokenSerializer(data=data)
    res = serializer.is_valid()

    assertions.assertFalse(res)
    assertions.assertIn('size_kb', serializer.errors)


@pytest.mark.django_db
def test_data2obj_string_int_sizekb():

    data = {
        'origin_filename': 'serializer.test',
        'size_kb': '199',
    }

    serializer = UploadTokenSerializer(data=data)
    res = serializer.is_valid()

    assertions.assertTrue(res)


@pytest.mark.django_db
def test_data2obj_no_name():

    data = {
    }

    serializer = UploadTokenSerializer(data=data)
    res = serializer.is_valid()

    assertions.assertFalse(res)
    assertions.assertIn('origin_filename', serializer.errors)
