# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0006_auto_20150924_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='Phone',
            field=models.IntegerField(blank=True),
        ),
    ]
