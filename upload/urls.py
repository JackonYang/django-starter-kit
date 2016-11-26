# -*- coding:utf-8 -*-
from django.conf.urls import url

from . import views


urlpatterns = (
    url(r'obtain-image-token', views.img_token_list_view, name='img_token_list_view'),
)
