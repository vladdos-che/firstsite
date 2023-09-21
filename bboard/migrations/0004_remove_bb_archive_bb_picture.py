# Generated by Django 4.2.4 on 2023-09-18 11:26

import bboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_bb_archive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bb',
            name='archive',
        ),
        migrations.AddField(
            model_name='bb',
            name='picture',
            field=models.ImageField(blank=True, upload_to=bboard.models.get_timestamp_path),
        ),
    ]
