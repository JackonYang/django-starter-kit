# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('nick_name', models.CharField(max_length=256, verbose_name='\u6635\u79f0', blank=True)),
                ('status', models.IntegerField(default=21, verbose_name='\u72b6\u6001', choices=[(1, '\u6ce8\u518c\u4e2d'), (11, '\u5f85\u5ba1\u6838'), (21, '\u6b63\u5e38'), (99, '\u5df2\u7981\u7528')])),
                ('username', models.CharField(unique=True, max_length=244, verbose_name='username', db_index=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='\u7cfb\u7edf\u7ba1\u7406\u5458')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u8d26\u53f7\u7cfb\u7edf',
                'verbose_name_plural': '\u7528\u6237\u8d26\u53f7\u7cfb\u7edf',
            },
        ),
    ]
