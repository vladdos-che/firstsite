# Generated by Django 4.2 on 2023-05-29 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0005_alter_bb_options_alter_bb_order_with_respect_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='kind',
            field=models.CharField(choices=[('b', 'Куплю'), ('s', 'Продам'), ('c', 'Поменяю')], default='s', max_length=1),
        ),
    ]
