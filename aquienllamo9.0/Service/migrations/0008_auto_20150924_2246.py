# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0007_auto_20150924_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='Phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='useraql',
            name='Phone',
            field=models.IntegerField(max_length=10, blank=True),
        ),
    ]
