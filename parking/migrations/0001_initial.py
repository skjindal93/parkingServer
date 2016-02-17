# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='parking_spots',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(max_digits=15, decimal_places=10)),
                ('longitude', models.DecimalField(max_digits=15, decimal_places=10)),
                ('table_name', models.CharField(max_length=255)),
                ('filled', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='sensors',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('latitude', models.DecimalField(max_digits=15, decimal_places=10)),
                ('longitude', models.DecimalField(max_digits=15, decimal_places=10)),
                ('pi_id', models.IntegerField()),
                ('pi_port', models.IntegerField()),
                ('occupied', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
