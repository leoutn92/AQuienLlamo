# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0009_auto_20150924_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraql',
            name='Adress',
            field=models.CharField(default=b'no tiene', max_length=50),
        ),
    ]
