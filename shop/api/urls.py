from django.urls import path
from .api_view import CategoryListApiView

urlpatterns = [
    path('categories', CategoryListApiView.as_view(), name='categories')
    
]