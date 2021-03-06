# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-17 01:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_content_video_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='description',
            field=models.TextField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='Posters'),
        ),
        migrations.AddField(
            model_name='content',
            name='time',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Content'),
        ),
    ]
