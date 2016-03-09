# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-12 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unlocode', '0018_auto_20160212_1450'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='locsubdivison',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='locsubdivison',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='locsubdivison',
            name='alpha2code',
        ),
        migrations.RemoveField(
            model_name='locsubdivison',
            name='name',
        ),
        migrations.RemoveField(
            model_name='locsubdivison',
            name='shortcode',
        ),
        migrations.RemoveField(
            model_name='locsubdivison',
            name='version',
        ),
    ]