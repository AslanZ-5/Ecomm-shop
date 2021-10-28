# Generated by Django 3.2.8 on 2021-10-27 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20211027_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(blank=True, max_length=255, related_name='related_customer', to='shop.Order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('completed', 'new order'), ('completed', 'order is completed'), ('in_progress', 'order in progress'), ('is_ready', 'order is ready')], default='NEW', max_length=255),
        ),
    ]