# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-23 08:08
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0013_department_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
