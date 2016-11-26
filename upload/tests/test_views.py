# -*- coding:utf-8 -*-
import pytest
import unittest

from rest_framework.test import APIClient

# from django.contrib.auth import get_user_model


assertions = unittest.TestCase('__init__')


@pytest.mark.django_db
def test_create_img_token():
    url = '/api/upload/obtain-image-token/'

    send_data = {
        'origin_filename': 'test-create-image-views.png',
    }

    # UserModel = get_user_model()
    # user = UserModel.objects.first()

    client = APIClient()
    # client.force_authenticate(user=user)

    response = client.post(url, send_data)
    data = response.data

    assertions.assertEqual(data['origin_filename'], send_data['origin_filename'])
    assertions.assertEqual(data['file_ext'], '.png')
    assertions.assertTrue(data['file_key'].endswith('.png'))
    assertions.assertTrue(data['token'])


@pytest.mark.django_db
def test_create_img_token_sizekb():
    url = '/api/upload/obtain-image-token/'

    send_data = {
        'origin_filename': 'test-create-image-views.png',
        'size_kb': 1024 * 1024,
    }

    # UserModel = get_user_model()
    # user = UserModel.objects.first()

    client = APIClient()
    # client.force_authenticate(user=user)

    response = client.post(url, send_data)
    data = response.data

    assertions.assertEqual(data['origin_filename'], send_data['origin_filename'])
    assertions.assertEqual(data['size_kb'], send_data['size_kb'])
    assertions.assertEqual(data['file_ext'], '.png')
    assertions.assertTrue(data['file_key'].endswith('.png'))
    assertions.assertTrue(data['token'])


@pytest.mark.django_db
def test_create_img_token_no_name():
    url = '/api/upload/obtain-image-token/'

    send_data = {
    }

    # UserModel = get_user_model()
    # user = UserModel.objects.first()

    client = APIClient()
    # client.force_authenticate(user=user)

    response = client.post(url, send_data)
    data = response.data

    assertions.assertIn('origin_filename', data)
