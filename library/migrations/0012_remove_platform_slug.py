# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-18 13:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_platform_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platform',
            name='slug',
        ),
    ]