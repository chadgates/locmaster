# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 14:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unlocode', '0002_auto_20160129_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locfunction',
            old_name='locfunction',
            new_name='functioncode',
        ),
        migrations.RenameField(
            model_name='locstatus',
            old_name='locstatus',
            new_name='statuscode',
        ),
    ]
