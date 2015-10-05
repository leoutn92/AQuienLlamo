# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0003_auto_20150914_2036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='adress',
            new_name='Adress',
        ),
        migrations.RenameField(
            model_name='useraql',
            old_name='adress',
            new_name='Adress',
        ),
    ]
