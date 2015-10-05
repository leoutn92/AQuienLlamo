# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0014_useraql_creationdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraql',
            name='CreationDate',
        ),
        migrations.AddField(
            model_name='service',
            name='CreationDate',
            field=models.DateField(default=datetime.datetime(2015, 9, 27, 4, 31, 8, 900636, tzinfo=utc)),
        ),
    ]
