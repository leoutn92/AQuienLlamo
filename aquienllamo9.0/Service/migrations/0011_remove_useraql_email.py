# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0010_auto_20150924_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraql',
            name='Email',
        ),
    ]
