# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-23 14:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylocation', '0009_locodelocation_rel_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locodelocation',
            name='rel_location',
        ),
    ]