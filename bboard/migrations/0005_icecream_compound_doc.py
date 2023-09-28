# Generated by Django 4.2.4 on 2023-09-28 05:44

import bboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0004_remove_bb_archive_bb_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='compound_doc',
            field=models.FileField(blank=True, null=True, upload_to=bboard.models.get_timestamp_path, verbose_name='Документ с полным рецептом'),
        ),
    ]
