# Generated by Django 3.2.8 on 2021-10-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_cart_total_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_product',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
