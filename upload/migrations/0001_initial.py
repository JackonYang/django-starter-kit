# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QiniuUploadToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=255)),
                ('bucket', models.CharField(max_length=100)),
                ('file_key', models.CharField(max_length=255)),
                ('origin_filename', models.CharField(max_length=255)),
                ('size_kb', models.IntegerField(default=-1)),
                ('file_ext', models.CharField(max_length=100)),
                ('referrer', models.CharField(default=b'', max_length=500)),
                ('ua', models.CharField(default=b'', max_length=500)),
                ('ip', models.CharField(default=b'', max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified_time', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
