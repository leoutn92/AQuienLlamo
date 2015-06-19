# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20150611_0211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nomEmpresa', models.CharField(max_length=30, unique=True)),
                ('CUIL', models.IntegerField()),
                ('usuario', models.ForeignKey(to='register.Cliente')),
            ],
        ),
        migrations.RemoveField(
            model_name='ṕroveedor',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Ṕroveedor',
        ),
    ]
