# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_auto_20160826_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='closing_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='opening_time',
            field=models.TimeField(blank=True),
        ),
    ]
