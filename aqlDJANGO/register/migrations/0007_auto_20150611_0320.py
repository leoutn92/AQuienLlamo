# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_auto_20150611_0212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proveedor',
            old_name='usuario',
            new_name='cliente',
        ),
    ]
