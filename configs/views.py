# -*- coding: utf-8 -*-
import socket
import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.template.response import TemplateResponse


logger = logging.getLogger(__name__)

host = socket.gethostname()


def home(request,
         template_name='home.html'):

    context = {
        'hostname': host,
        'user': request.user,
    }

    return TemplateResponse(request, template_name, context)


@api_view(['GET'])
def api_home(request):
    user = request.user

    return Response('Hello %s!'
                    'My Host name is %s.' % (user, host))
