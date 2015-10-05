# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0005_useraql_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraql',
            name='Image',
            field=models.ImageField(upload_to=b'static/ImageUserAQL'),
        ),
    ]
