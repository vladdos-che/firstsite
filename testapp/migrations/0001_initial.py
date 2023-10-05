# Generated by Django 4.2.4 on 2023-10-05 11:53

import bboard.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=bboard.models.get_timestamp_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('jpg', 'png', 'gif'))], verbose_name='Изображение')),
                ('desc', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
