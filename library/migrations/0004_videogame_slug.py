# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-17 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20170617_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogame',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]