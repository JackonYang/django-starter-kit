# -*- coding: utf-8 -*-
import socket
import logging

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
