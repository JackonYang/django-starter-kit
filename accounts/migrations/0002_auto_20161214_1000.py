# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_',
            name='email',
            field=models.CharField(default=b'', max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='user_',
            name='email_error',
            field=models.IntegerField(default=accounts.models.get_random_email_error),
        ),
        migrations.AddField(
            model_name='user_',
            name='mobile',
            field=models.CharField(default=b'', max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='user_',
            name='mobile_error',
            field=models.IntegerField(default=accounts.models.get_random_phone_error),
        ),
        migrations.AlterUniqueTogether(
            name='user_',
            unique_together=set([('mobile', 'mobile_error'), ('email', 'email_error')]),
        ),
    ]
