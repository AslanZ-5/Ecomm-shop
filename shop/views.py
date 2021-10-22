from django.shortcuts import render
from django.views.generic import DetailView, View
from .models import Laptop, SmartPhone, Category, LatestProducts, Customer, Cart, CartProduct
from .mixins import CategoryDetailMixin
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType


# def index(request):

class BaseView(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_left_sidebar()
        products = LatestProducts.objects.get_products_for_models(
            'laptop', 'smartphone', with_respect_to='laptop'
        )
        context = {
            'categories': categories,
            'products': products,

        }
        return render(request, 'shop/base.html', context)


class ProductDetailView(CategoryDetailMixin, DetailView):
    CT_MODEL = {
        'laptop': Laptop,
        'smartphone': SmartPhone
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'shop/product_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ct_model'] = self.model._meta.model_name

        return context


class CategoryDetailView(CategoryDetailMixin, DetailView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'shop/category_detail.html'
    slug_url_kwarg = 'slug'


class AddCartView(View):
    def get(self, request, *args, **kwargs):
        ct_model = kwargs.get('ct_model')  # getting model name from url request
        product_slug = kwargs.get('slug')  # getting product's slug from url request
        content_type = ContentType.objects.get(model=ct_model)  # getting model by model name
        product = content_type.model_class().objects.get(
            slug=product_slug)  # getting product from product's model by product slug
        customer = Customer.objects.get(user=request.user) # getting customer by current user
        cart = Cart.objects.get(owner=customer, in_order=False) # getting cart by owner which is customer
        cart_product, created = CartProduct.objects.get_or_create(
            user=cart.owner, cart=cart, content_type=content_type,object_id=product.id,final_price=product.price
        ) # creating cart product by data which we got above
        cart.products.add(cart_product)

        return HttpResponseRedirect('/cart/')


class CartView(View):
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        cart = Cart.objects.get(owner=customer)
        categories = Category.objects.get_categories_for_left_sidebar()
        context = {
            'cart': cart,
            'categories': categories
        }
        return render(request, 'shop/cart.html', context)
