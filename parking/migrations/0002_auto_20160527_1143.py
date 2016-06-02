# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensors',
            name='latitude',
            field=models.DecimalField(max_digits=15, decimal_places=10),
        ),
        migrations.AlterField(
            model_name='sensors',
            name='longitude',
            field=models.DecimalField(max_digits=15, decimal_places=10),
        ),
    ]
