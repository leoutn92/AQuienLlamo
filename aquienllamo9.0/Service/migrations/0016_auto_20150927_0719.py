# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0015_auto_20150927_0431'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Opinion', models.TextField(max_length=500)),
                ('CreationDate', models.DateField(default=datetime.datetime(2015, 9, 27, 7, 19, 38, 365081, tzinfo=utc))),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='CreationDate',
            field=models.DateField(default=datetime.datetime(2015, 9, 27, 7, 19, 38, 363836, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='comment',
            name='Service',
            field=models.ForeignKey(to='Service.Service'),
        ),
        migrations.AddField(
            model_name='comment',
            name='User',
            field=models.ForeignKey(to='Service.UserAQL'),
        ),
    ]
