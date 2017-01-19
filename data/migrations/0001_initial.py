# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(max_length=10, verbose_name='\u5f00\u5956\u65e5\u671f')),
                ('timestamp', models.CharField(max_length=8, verbose_name='\u5f00\u5956\u65f6\u95f4')),
                ('seq', models.PositiveSmallIntegerField(verbose_name='\u5f53\u5929\u5f00\u5956\u671f\u53f7')),
                ('win_str', models.CharField(max_length=23, verbose_name='\u5f00\u5956\u7ed3\u679c')),
            ],
            options={
                'ordering': ['-day', '-seq'],
                'verbose_name': '\u5f00\u5956\u6570\u636e',
                'verbose_name_plural': '\u5f00\u5956\u6570\u636e',
            },
        ),
        migrations.AlterUniqueTogether(
            name='record',
            unique_together=set([('day', 'seq')]),
        ),
    ]
