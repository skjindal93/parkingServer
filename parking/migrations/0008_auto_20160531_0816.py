# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0007_auto_20160531_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingraspberrymapping',
            name='area',
            field=models.ForeignKey(related_name=b'area_mappings', to='parking.parkingAreas'),
        ),
        migrations.AlterField(
            model_name='sensors',
            name='pi',
            field=models.ForeignKey(related_name=b'sensors', to='parking.raspberry'),
        ),
    ]
