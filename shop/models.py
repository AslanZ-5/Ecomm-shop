from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class LatestProductsManager:

    @staticmethod
    def get_products_for_models(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_product = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_product)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model = with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to),reverse=True)
        return products


class LatestProducts:
    objects = LatestProductsManager()


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category Name')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Product Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Product Name')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Product Price')
    discount_price = models.FloatField()
    description = models.TextField(verbose_name='Product Description', null=True)
    image = models.ImageField(verbose_name='Product Image')

    def __str__(self):
        return self.title


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Customer', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart',  on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total Price')

    def __str__(self):
        return f'Product: {self.product.title}'


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Customer', on_delete=models.CASCADE)
    # products = models.ManyToManyField(Product,blank=True, related_name='related_cart')
    total_product = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total Price')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Customer', on_delete=models.CASCADE)
    phone = models.CharField(max_length=255, verbose_name='Phone number')
    address = models.CharField(max_length=250, verbose_name='Customer Address')

    def __str__(self):
        return f'Customer: {self.user.username} '


class Laptop(Product):
    diagonal = models.CharField(max_length=255)
    display = models.CharField(max_length=255)
    processor_freq = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    video_card = models.CharField(max_length=255)
    time_without_charge = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.category.name} {self.title}'


class SmartPhone(Product):
    diagonal = models.CharField(max_length=255)
    display = models.CharField(max_length=255)
    resolution = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    accum_volume = models.CharField(max_length=255)
    time_without_charge = models.CharField(max_length=255)
    sd = models.BooleanField(default=True)
    sd_volume_max = models.CharField(max_length=255, verbose_name='Maximum internal memory')
    main_camera_mp = models.CharField(max_length=255)
    frontal_camera_mp = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.category.name} {self.title}'


