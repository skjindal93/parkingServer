# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0003_auto_20160608_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingareas',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='parkingareas',
            name='filled',
            field=models.IntegerField(default=0),
        ),
    ]
