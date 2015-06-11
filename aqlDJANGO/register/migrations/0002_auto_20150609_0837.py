# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ṕroveedor',
            name='CUIL',
            field=models.IntegerField(),
        ),
    ]
