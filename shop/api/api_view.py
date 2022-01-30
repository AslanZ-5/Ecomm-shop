from collections import OrderedDict
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from .serializers import CategorySerializer, SmartphoneSerializer, LaptopSerializer, CustomerSerializer
from shop.models import Category, SmartPhone, Customer, Laptop
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination


class CategoryPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('category_count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('output', data)
        ]))


class CategoryListApiView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CategoryPagination


class SmartphoneListAPIView(ListAPIView):
    serializer_class = SmartphoneSerializer
    queryset = SmartPhone.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'slug']

    ## Manually filtering
    # def get_queryset(self):
    #     slug = self.request.query_params.get('slug')
    #     price = self.request.query_params.get('price')
    #     ww = {'price':price,'slug':slug}
    #     if slug:
    #         return super().get_queryset().filter(**ww)
    #     else:
    #         return super().get_queryset()


class LaptopListAPIView(ListAPIView):
    serializer_class = LaptopSerializer
    queryset = Laptop.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'slug']


class SmartphoneAPIDetailView(RetrieveAPIView):
    serializer_class = SmartphoneSerializer
    queryset = SmartPhone.objects.all()
    lookup_field = 'id'


class CustomersListAPIView(ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
