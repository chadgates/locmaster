# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unlocode', '0006_auto_20160129_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdivision',
            name='shortcode',
            field=models.CharField(max_length=5),
        ),
    ]
