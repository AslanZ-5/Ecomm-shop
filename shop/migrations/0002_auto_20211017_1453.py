# Generated by Django 3.2.8 on 2021-10-17 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_product', models.PositiveIntegerField(default=0)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Total Price')),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('qty', models.PositiveIntegerField(default=1)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Total Price')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_products', to='shop.cart')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category Name')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255, verbose_name='Phone number')),
                ('address', models.CharField(max_length=250, verbose_name='Customer Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Product Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Product Price')),
                ('discount_price', models.FloatField()),
                ('description', models.TextField(null=True, verbose_name='Product Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Product Image')),
                ('diagonal', models.CharField(max_length=255)),
                ('display', models.CharField(max_length=255)),
                ('processor_freq', models.CharField(max_length=255)),
                ('ram', models.CharField(max_length=255)),
                ('video_card', models.CharField(max_length=255)),
                ('time_without_charge', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Product Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SmartPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Product Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Product Price')),
                ('discount_price', models.FloatField()),
                ('description', models.TextField(null=True, verbose_name='Product Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Product Image')),
                ('diagonal', models.CharField(max_length=255)),
                ('display', models.CharField(max_length=255)),
                ('resolution', models.CharField(max_length=255)),
                ('ram', models.CharField(max_length=255)),
                ('accum_volume', models.CharField(max_length=255)),
                ('time_without_charge', models.CharField(max_length=255)),
                ('sd', models.BooleanField(default=True)),
                ('sd_volume_max', models.CharField(max_length=255, verbose_name='Maximum internal memory')),
                ('main_camera_mp', models.CharField(max_length=255)),
                ('frontal_camera_mp', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Product Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.AddField(
            model_name='cartproduct',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer', verbose_name='Customer'),
        ),
        migrations.AddField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer', verbose_name='Customer'),
        ),
    ]
