# -*- coding: utf-8-*-
from django.contrib import admin

from .models import (
    Tag,
    UserText,
)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name',
    )


@admin.register(UserText)
class UserTextAdmin(admin.ModelAdmin):
    list_display = (
        'brief',
    )
