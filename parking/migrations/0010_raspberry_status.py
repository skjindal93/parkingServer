# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0009_raspberry_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='raspberry',
            name='status',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
