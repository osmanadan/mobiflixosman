# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-17 01:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20180917_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='video_url',
        ),
    ]