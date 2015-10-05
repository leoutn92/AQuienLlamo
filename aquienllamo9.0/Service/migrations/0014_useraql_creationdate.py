# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0013_calification'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraql',
            name='CreationDate',
            field=models.DateField(default=datetime.datetime(2015, 9, 27, 4, 27, 45, 574108, tzinfo=utc)),
        ),
    ]
