# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0005_auto_20160530_1100'),
    ]

    operations = [
        migrations.DeleteModel(
            name='spots',
        ),
        migrations.AddField(
            model_name='parkingareas',
            name='capacity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parkingareas',
            name='filled',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parkingareas',
            name='latitude',
            field=models.DecimalField(default=50, max_digits=15, decimal_places=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parkingareas',
            name='longitude',
            field=models.DecimalField(default=50, max_digits=15, decimal_places=10),
            preserve_default=False,
        ),
    ]
