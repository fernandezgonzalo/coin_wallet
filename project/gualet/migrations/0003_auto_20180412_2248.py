# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-12 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gualet', '0002_auto_20180412_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gualet',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
