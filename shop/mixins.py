from django.views.generic.detail import SingleObjectMixin
from django.views.generic import  View
from .models import Category,Cart,Customer


class CategoryDetailMixin(SingleObjectMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.get_categories_for_left_sidebar()
        return context

class CartMixin(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.authenticated:
            customer = Customer.objects.filter(user=request.user).first()
            cart = Cart.objects.filter(owner=customer, in_order=False).first()
            if cart:
                return cart
            else:
                cart = Cart.objects.create(owner=customer,)
        else:
            cart = Cart.objects.filter(for_anonymous_user=True).first()
            if cart:
                return Cart
            else:
                cart = Cart.objects.create(for_anonymous_user=True)
                return cart

