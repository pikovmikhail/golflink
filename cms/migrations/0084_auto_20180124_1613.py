# Generated by Django 2.0 on 2018-01-24 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0083_auto_20180114_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubpage',
            name='facebook_pixel_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='corppage',
            name='facebook_pixel_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
