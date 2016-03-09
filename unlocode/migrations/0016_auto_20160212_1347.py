# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-12 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unlocode', '0015_auto_20160211_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locode',
            name='locchangeindicator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='unlocode.LocChangeIndicator'),
        ),
        migrations.AlterField(
            model_name='locode',
            name='locodecountry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unlocode.LocCountry'),
        ),
        migrations.AlterField(
            model_name='locode',
            name='locstatus',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='unlocode.LocStatus'),
        ),
        migrations.AlterField(
            model_name='locode',
            name='locsubdivision',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='unlocode.LocSubdivison'),
        ),
    ]
