# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-19 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0025_auto_20170703_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='icon',
            field=models.ImageField(default='', upload_to=library.models.get_image_path),
        ),
    ]
