# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('usuario', models.CharField(max_length=30, unique=True)),
                ('contrasenia', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('telefono', models.IntegerField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('fechaRegistro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ṕroveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nomEmpresa', models.CharField(max_length=30, unique=True)),
                ('CUIL', models.IntegerField(max_length=30)),
                ('usuario', models.ForeignKey(to='register.Usuario')),
            ],
        ),
    ]
