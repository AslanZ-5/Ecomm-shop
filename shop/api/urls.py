from django.urls import path
from .api_view import CategoryListApiView, SmartphoneListAPIView

urlpatterns = [
    path('categories/', CategoryListApiView.as_view(), name='categories'),
    path('smartphones/', SmartphoneListAPIView.as_view(), name='smartphones')

]
