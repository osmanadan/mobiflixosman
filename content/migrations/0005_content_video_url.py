# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-17 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_remove_content_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='video_url',
            field=models.FileField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
