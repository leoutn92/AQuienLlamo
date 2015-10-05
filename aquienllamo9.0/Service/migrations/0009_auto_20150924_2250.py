# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0008_auto_20150924_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraql',
            name='Phone',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
