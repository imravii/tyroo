# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-26 15:26
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190226_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='Schedule',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(0, 'Every 15 minutes'), (1, 'Every Hour'), (2, 'EveryDay')], max_length=11),
        ),
    ]