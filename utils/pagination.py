# -*- coding: utf-8 -*-
from rest_framework.pagination import LimitOffsetPagination


class BasePagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 50
