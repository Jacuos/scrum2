# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20160618_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='number',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=1000, null=True),
        ),
    ]
