from django.urls import path
from shop import views

urlpatterns = [
    path('', views.index, name='home'),
    path('product/<str:ct_model>/<str:slug>/',views.ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/',views.CategoryDetailView.as_view(), name='category_detail'),
]

