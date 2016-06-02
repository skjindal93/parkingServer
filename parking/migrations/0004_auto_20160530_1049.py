# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0003_parkingareas'),
    ]

    operations = [
        migrations.CreateModel(
            name='parkingRaspberryMapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.ForeignKey(to='parking.parkingAreas')),
                ('pi', models.ForeignKey(to='parking.raspberry')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='parkingareas',
            name='pi',
        ),
    ]
