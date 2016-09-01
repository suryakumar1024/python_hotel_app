# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20160825_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='closing_time',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='opening_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
