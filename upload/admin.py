# -*- coding: utf-8*-
from django.contrib import admin

from .models import QiniuUploadToken


@admin.register(QiniuUploadToken)
class QiniuUploadTokenAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'token',
        'file_key',
        'origin_filename',
        'user',
        'referrer',
        'create_time',
    )

    search_fields = (
        '=user_id',
        'file_key',
    )

    readonly_fields = (
        'user',
    )
