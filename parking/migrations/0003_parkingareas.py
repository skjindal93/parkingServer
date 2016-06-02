# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0002_auto_20160527_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='parkingAreas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('pi', models.ForeignKey(to='parking.raspberry')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
