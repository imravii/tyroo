# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-26 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20190226_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='Schedule',
            field=models.CharField(choices=[(0, 'Every 15 minutes'), (1, 'Every Hour'), (2, 'EveryDay')], max_length=100),
        ),
    ]
