# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_auto_20150622_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='fechaRegistro',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 6, 22, 14, 51, 8, 208746, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fechaPedido',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
