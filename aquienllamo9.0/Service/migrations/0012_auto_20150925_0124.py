# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0011_remove_useraql_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='Calification',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]
