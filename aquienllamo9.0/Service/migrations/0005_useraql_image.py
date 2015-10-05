# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0004_auto_20150914_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraql',
            name='Image',
            field=models.ImageField(default=0, upload_to=b'static/ImageService'),
            preserve_default=False,
        ),
    ]
