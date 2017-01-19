# -*- coding: utf-8-*-
from django.contrib import admin

from .models import Record


@admin.register(Record)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('day', 'seq', 'win_str', 'timestamp')
