# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0002_auto_20160608_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingregions',
            name='name',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
