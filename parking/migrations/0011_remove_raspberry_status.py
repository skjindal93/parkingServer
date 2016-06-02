# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0010_raspberry_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='raspberry',
            name='status',
        ),
    ]
