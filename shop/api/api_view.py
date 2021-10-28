from rest_framework.generics import ListAPIView
from .serializers import CategorySerializer,SmartphoneSerializer,LaptopSerializer
from shop.models import Category,SmartPhone,Laptop
from rest_framework.filters import SearchFilter


class CategoryListApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SmartphoneListAPIView(ListAPIView):
    serializer_class = SmartphoneSerializer
    queryset = SmartPhone.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price','slug']

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
    search_fields = ['price','slug']