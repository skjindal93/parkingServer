# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='areaRegionMapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='parkingAreas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('latitude', models.DecimalField(max_digits=15, decimal_places=10)),
                ('longitude', models.DecimalField(max_digits=15, decimal_places=10)),
                ('capacity', models.IntegerField()),
                ('filled', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='parkingRaspberryMapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.ForeignKey(related_name=b'area_mappings', to='parking.parkingAreas')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='parkingRegions',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.TextField(blank=True)),
                ('latitude', models.DecimalField(max_digits=15, decimal_places=10)),
                ('longitude', models.DecimalField(max_digits=15, decimal_places=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='raspberry',
            fields=[
                ('raspberry_id', models.AutoField(serialize=False, primary_key=True)),
                ('mac', models.CharField(max_length=255, null=True)),
                ('ip', models.CharField(max_length=255, null=True)),
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
                ('latitude', models.DecimalField(max_digits=15, decimal_places=10)),
                ('longitude', models.DecimalField(max_digits=15, decimal_places=10)),
                ('pi_port', models.IntegerField()),
                ('occupied', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('pi', models.ForeignKey(related_name=b'sensors', to='parking.raspberry')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='sensors',
            unique_together=set([('pi', 'pi_port')]),
        ),
        migrations.AddField(
            model_name='parkingraspberrymapping',
            name='pi',
            field=models.ForeignKey(related_name=b'pi_mappings', to='parking.raspberry'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='parkingraspberrymapping',
            unique_together=set([('area', 'pi')]),
        ),
        migrations.AddField(
            model_name='arearegionmapping',
            name='area',
            field=models.ForeignKey(related_name=b'region_mappings', to='parking.parkingAreas'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='arearegionmapping',
            name='region',
            field=models.ForeignKey(related_name=b'region_mappings', to='parking.parkingRegions'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='arearegionmapping',
            unique_together=set([('region', 'area')]),
        ),
    ]
