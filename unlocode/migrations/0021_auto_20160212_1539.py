# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-12 15:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unlocode', '0020_auto_20160212_1515'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LocChangeTags',
            new_name='LocChangeTag',
        ),
    ]
