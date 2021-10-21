from django.shortcuts import render
from django.views.generic import DetailView, View
from .models import Laptop, SmartPhone, Category, LatestProducts, Customer, Cart
from .mixins import CategoryDetailMixin
from django.http import HttpResponseRedirect


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
        print(kwargs.get('ct_model'))
        print(kwargs.get('slug'))
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
