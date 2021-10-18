# Generated by Django 3.2.8 on 2021-10-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20211017_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='slug',
            field=models.SlugField(default=None, unique=True),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='slug',
            field=models.SlugField(default=None, unique=True),
        ),
    ]