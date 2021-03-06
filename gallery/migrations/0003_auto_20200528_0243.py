# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-27 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20200527_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='category',
        ),
        migrations.AddField(
            model_name='photo',
            name='category',
            field=models.ManyToManyField(to='gallery.Category'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(height_field='height', upload_to='', width_field='width'),
        ),
    ]
