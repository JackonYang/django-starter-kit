# -*- coding:utf-8 -*-
from django.conf.urls import url

from .import views


urlpatterns = (
    url(r'^$', views.usertext_list_views, name='usertext_list_views'),
)
