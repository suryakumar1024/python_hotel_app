# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_menu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='hotel_name',
            new_name='hotel',
        ),
    ]
