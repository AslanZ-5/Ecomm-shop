from rest_framework.generics import ListAPIView
from .serializers import CategorySerializer,SmartphoneSerializer
from shop.models import Category,SmartPhone


class CategoryListApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SmartphoneListAPIView(ListAPIView):
    serializer_class = SmartphoneSerializer
    queryset = SmartPhone.objects.all()

