# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-21 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer_activity', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='volunteer',
        ),
        migrations.AddField(
            model_name='event',
            name='event_num',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]