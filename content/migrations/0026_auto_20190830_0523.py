# Generated by Django 2.0.3 on 2019-08-30 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0025_content_trailer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='trailer',
            new_name='trailer_url',
        ),
    ]