# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_auto_20150622_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('fechaPedido', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('precioBase', models.IntegerField()),
                ('categoria', models.ForeignKey(to='register.Categoria')),
                ('estado', models.ForeignKey(to='register.Estado')),
                ('proveedor', models.ForeignKey(to='register.Proveedor')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='Servicio',
            field=models.ForeignKey(to='register.Servicio'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(to='register.Cliente'),
        ),
    ]
