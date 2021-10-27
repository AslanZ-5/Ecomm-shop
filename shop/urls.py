from django.urls import path
from shop import views

urlpatterns = [
    path('', views.BaseView.as_view(), name='home'),
    path('product/<str:ct_model>/<str:slug>/',views.ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/',views.CategoryDetailView.as_view(), name='category_detail'),
    path('cart/',views.CartView.as_view(),name='cart'),
    path('add-to-cart/<str:ct_model>/<str:slug>/',views.AddCartView.as_view(),name='add_to_cart'),
    path('remove-from-cart/<str:ct_model>/<str:slug>/',views.DeleteCartProductView.as_view(),name='remove_from_cart'),
    path('change-qty/<str:ct_model>/<str:slug>/',views.ChangeQTYView.as_view(),name='qty'),
    path('checkout/',views.CheckoutView.as_view(),name='checkout'),
    path('new_order/',views.MakeOrderView.as_view(),name='new_order'),
]

