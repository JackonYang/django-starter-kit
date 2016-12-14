# -*- coding:utf-8 -*-
from rest_framework import serializers

from .models import (
    UserText,
)


class UserTextSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserText
        exclude = ('created_time', 'last_modified_time')
