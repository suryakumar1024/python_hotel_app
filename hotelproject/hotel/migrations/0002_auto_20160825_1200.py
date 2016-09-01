# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='closing_time',
            field=models.CharField(default=datetime.datetime(2016, 8, 25, 12, 0, 36, 945015), max_length=100),
        ),
        migrations.AddField(
            model_name='hotel',
            name='opening_time',
            field=models.CharField(default=datetime.datetime(2016, 8, 25, 12, 0, 36, 944975), max_length=100),
        ),
    ]
