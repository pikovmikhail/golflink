# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-02 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0041_clubadvertisement_corpadvertisement'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubadvertisement',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='corpadvertisement',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
