# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0020_auto_20150927_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='CreationDate',
            field=models.DateField(default=datetime.datetime(2015, 9, 27, 8, 19, 49, 607883, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='service',
            name='CreationDate',
            field=models.DateField(default=datetime.datetime(2015, 9, 27, 8, 19, 49, 606772, tzinfo=utc)),
        ),
    ]
