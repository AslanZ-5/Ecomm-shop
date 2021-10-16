from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category Name')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Product Name')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Product Price')
    discount_price = models.FloatField()
    category = models.FileField(Category, on_delete=models.CASCADE, verbose_name='Product Category', )
    description = models.TextField(verbose_name='Product Description', null=True)
    image = models.ImageField(verbose_name='Product Image')

    def __str__(self):
        return self.title


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Customer',on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Cart',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Product',on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total Price')
    def __str__(self):
        return f'Product: {self.product.title}'

class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Customer',on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,blank=True)
    total_product = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total Price')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Customer',on_delete=models.CASCADE)
    phone = models.CharField(max_length=255,verbose_name='Phone number')
    address = models.CharField(max_length=250,verbose_name='Customer Address')

    def __str__(self):
        return f'Customer: {self.user.first_name} {self.user.last_name}'


class Specification(models.Model):
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, verbose_name='Product name for specification')

    def __str__(self):
        return f'Specification for product: {self.name}'


