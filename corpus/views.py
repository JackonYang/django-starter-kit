# -*- coding:utf-8 -*-
from rest_framework import generics, filters

# from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from .serializers import (
    UserTextSerializer,
)


class UserTextList(generics.ListCreateAPIView):
    serializer_class = UserTextSerializer

    # permission_classes = (IsAuthenticatedOrReadOnly, )

    filter_backends = (
        filters.OrderingFilter,
        filters.SearchFilter,
    )

    search_fields = (
        'text',
    )

    def get_queryset(self):
        ModelClass = self.serializer_class.Meta.model
        return ModelClass.objects.all()


usertext_list_views = UserTextList.as_view()
