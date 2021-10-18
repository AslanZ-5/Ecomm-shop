from django.shortcuts import render
from django.views.generic import DetailView
from .models import Laptop, SmartPhone


def index(request):
    return render(request, 'shop/base.html')


class ProductDetailView(DetailView):
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
