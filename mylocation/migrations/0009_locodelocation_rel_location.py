# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-23 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mylocation', '0008_auto_20160223_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='locodelocation',
            name='rel_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='mylocation.Location'),
        ),
    ]