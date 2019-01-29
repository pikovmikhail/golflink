# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-03 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corp', '0006_auto_20170814_0529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='content',
            new_name='content_en',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='headline',
            new_name='headline_en',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='summary',
            new_name='summary_en',
        ),
        migrations.AddField(
            model_name='news',
            name='content_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='headline_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='summary_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]