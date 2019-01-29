# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-17 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0074_region_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='tee_time_url',
            field=models.URLField(blank=True, help_text='Used for US tee times that are region-specific', null=True),
        ),
    ]
