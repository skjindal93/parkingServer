# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0006_auto_20160530_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingraspberrymapping',
            name='pi',
            field=models.ForeignKey(related_name=b'pi_mappings', to='parking.raspberry'),
        ),
    ]
