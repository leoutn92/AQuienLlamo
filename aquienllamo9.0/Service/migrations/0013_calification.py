# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0012_auto_20150925_0124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Value', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)])),
                ('Service', models.ForeignKey(to='Service.Service')),
                ('User', models.ForeignKey(to='Service.UserAQL')),
            ],
        ),
    ]
