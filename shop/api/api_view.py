from rest_framework.generics import ListAPIView
from .serializers import CategorySerializer,SmartphoneSerializer
from shop.models import Category,SmartPhone


class CategoryListApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SmartphoneListAPIView(ListAPIView):
    serializer_class = SmartphoneSerializer
    queryset = SmartPhone.objects.all()

    def get_queryset(self):
        slug = self.request.query_params.get('slug')
        price = self.request.query_params.get('price')
        ww = {'price':price,'slug':slug}
        if slug:
            return super().get_queryset().filter(**ww)
        else:
            return super().get_queryset()