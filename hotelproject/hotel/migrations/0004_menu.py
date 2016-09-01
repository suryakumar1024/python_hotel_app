# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_auto_20160826_0536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_one', models.CharField(default=b'none', max_length=100)),
                ('item_two', models.CharField(default=b'none', max_length=100)),
                ('hotel_name', models.ForeignKey(to='hotel.Hotel')),
            ],
        ),
    ]
