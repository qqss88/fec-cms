# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-31 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0094_auto_20170829_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionpage',
            name='menu_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='custompage',
            name='menu_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='resourcepage',
            name='menu_title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
