# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-17 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_content_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='video_url',
            field=models.FileField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
