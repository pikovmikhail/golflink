# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-01 13:51
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('guid', models.CharField(max_length=36, unique=True)),
                ('number', models.IntegerField()),
                ('type', models.CharField(max_length=255)),
            ],
        ),
    ]
