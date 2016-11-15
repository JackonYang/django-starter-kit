# -*- coding: utf-8 -*-


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


def test_with_client(client):
    response = client.get('/')
    assert response.status_code == 200
