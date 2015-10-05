# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Name', models.CharField(max_length=30, unique=True, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NameService', models.CharField(max_length=50)),
                ('DescriptionService', models.TextField(max_length=500)),
                ('Calification', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('Phone', models.IntegerField()),
                ('Image', models.ImageField(upload_to=b'static/ImageService')),
                ('Category', models.ForeignKey(to='Service.Category')),
            ],
        ),
        migrations.CreateModel(
            name='UserAQL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('DNI', models.IntegerField()),
                ('Email', models.EmailField(max_length=300)),
                ('Phone', models.IntegerField(max_length=10)),
                ('User', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='User',
            field=models.ForeignKey(to='Service.UserAQL'),
        ),
    ]
