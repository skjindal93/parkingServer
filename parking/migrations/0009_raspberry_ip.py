# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0008_auto_20160531_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='raspberry',
            name='ip',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
