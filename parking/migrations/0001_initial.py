# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='raspberry',
            fields=[
                ('raspberry_id', models.AutoField(serialize=False, primary_key=True)),
                ('mac', models.CharField(max_length=255, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='raspberryPhone',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('phone_mac', models.CharField(max_length=255)),
                ('pi', models.ForeignKey(to='parking.raspberry')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='sensors',
            fields=[
                ('sensor_id', models.AutoField(serialize=False, primary_key=True)),
                ('latitude', models.DecimalField(null=True, max_digits=15, decimal_places=10)),
                ('longitude', models.DecimalField(null=True, max_digits=15, decimal_places=10)),
                ('pi_port', models.IntegerField()),
                ('occupied', models.BooleanField(default=False)),
                ('pi', models.ForeignKey(related_name=b'pis', to='parking.raspberry')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='spots',
            fields=[
                ('spot_id', models.AutoField(serialize=False, primary_key=True)),
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
        migrations.AlterUniqueTogether(
            name='sensors',
            unique_together=set([('pi', 'pi_port')]),
        ),
    ]
