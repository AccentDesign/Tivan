# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-29 21:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0021_auto_20170625_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(default='', unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='collection',
            name='user',
        ),
        migrations.RemoveField(
            model_name='collectionitem',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='collectionitem',
            name='format',
        ),
        migrations.RemoveField(
            model_name='collectionitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='coverart',
            name='mediaItem',
        ),
        migrations.AddField(
            model_name='mediaitem',
            name='available',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='mediaitem',
            name='coverArt',
            field=models.ImageField(default='', upload_to=library.models.get_image_path),
        ),
        migrations.AddField(
            model_name='mediaitem',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Collection',
        ),
        migrations.DeleteModel(
            name='CollectionItem',
        ),
        migrations.DeleteModel(
            name='CoverArt',
        ),
        migrations.DeleteModel(
            name='MediaFormat',
        ),
        migrations.AddField(
            model_name='mediaitem',
            name='platform',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='library.Platform'),
        ),
    ]