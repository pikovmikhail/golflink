# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-26 15:33
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0016_certificategrouptemplate_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsignature',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='signatures', to='clubs.Department'),
        ),
    ]
