# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0002_auto_20150914_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='Email',
            field=models.EmailField(default='desconocido', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='adress',
            field=models.CharField(default='desconocida', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraql',
            name='adress',
            field=models.CharField(default='desconocida', max_length=50),
            preserve_default=False,
        ),
    ]
