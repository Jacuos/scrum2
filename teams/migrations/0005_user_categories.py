# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qanda', '0001_initial'),
        ('teams', '0004_auto_20160619_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='categories',
            field=models.ManyToManyField(to='qanda.Category'),
        ),
    ]
