# -*- coding: utf-8 -*-
import socket
import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.template.response import TemplateResponse

from django_redis import get_redis_connection


logger = logging.getLogger(__name__)

host = socket.gethostname()
redis = get_redis_connection("default")


def home(request,
         template_name='home.html'):

    key = 'test:hits'
    redis.incr(key)

    context = {
        'hostname': host,
        'user': request.user,
        'hits': redis.get(key),
    }

    logger.info('hits: {hits}'.format(**context))

    return TemplateResponse(request, template_name, context)


@api_view(['GET'])
def api_home(request):
    user = request.user

    return Response('Hello %s!'
                    'My Host name is %s.' % (user, host))
