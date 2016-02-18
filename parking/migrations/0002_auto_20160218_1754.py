# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='raspberryphone',
            old_name='phone_id',
            new_name='pi_id',
        ),
    ]
