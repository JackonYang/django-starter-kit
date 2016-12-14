# -*- coding: utf-8-*-
from django.contrib import admin

from .models import (
    UserText,
)


@admin.register(UserText)
class UserTextAdmin(admin.ModelAdmin):
    list_display = (
        'brief',
    )