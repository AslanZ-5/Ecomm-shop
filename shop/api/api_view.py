from rest_framework.generics import ListAPIView
from .serializers import CategorySerializer
from shop.models import Category


class CategoryListApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
