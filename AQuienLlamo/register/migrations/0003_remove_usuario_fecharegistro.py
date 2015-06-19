# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20150609_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='fechaRegistro',
        ),
    ]
