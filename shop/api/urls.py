from django.urls import path
from .api_view import (CategoryListApiView,
                       SmartphoneListAPIView,
                       LaptopListAPIView,
                       SmartphoneAPIDetailView,
                        CustomersListAPIView,


)

urlpatterns = [
    path('categories/', CategoryListApiView.as_view(), name='categories'),
    path('customers/', CustomersListAPIView.as_view(), name='customers'),
    path('smartphones/', SmartphoneListAPIView.as_view(), name='smartphones'),
    path('laptops/', LaptopListAPIView.as_view(), name='laptops'),
    path('smartphone/<int:id>/', SmartphoneAPIDetailView.as_view(), name='smartphone_detail'),

]
