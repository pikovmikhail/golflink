# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-16 07:53
# flake8: noqa
from __future__ import unicode_literals

import clublink.base.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20170216_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to=clublink.base.utils.RandomizedUploadPath('page')),
        ),
    ]