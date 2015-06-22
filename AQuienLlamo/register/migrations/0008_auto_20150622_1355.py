# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_auto_20150611_0320'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, default=datetime.datetime(2015, 6, 22, 13, 55, 46, 84872, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='cliente',
            field=models.OneToOneField(to='register.Cliente'),
        ),
    ]
