# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0004_auto_20160530_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensors',
            name='created',
            field=models.DateTimeField(default=datetime.date(2016, 5, 30), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensors',
            name='modified',
            field=models.DateTimeField(default=datetime.date(2016, 5, 30), auto_now=True),
            preserve_default=False,
        ),
    ]
