# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-16 23:02
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20170216_0753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryimage',
            options={'ordering': ('sort',)},
        ),
        migrations.AlterModelOptions(
            name='listitem',
            options={'ordering': ('sort',)},
        ),
    ]
