# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import QiniuUploadToken


class UploadTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = QiniuUploadToken

        read_only_fields = (
            'token',
            'file_key',
            'file_ext',
            # 'user',
            'create_time',
        )

        fields = (
            'origin_filename',
            'size_kb',
        ) + read_only_fields
