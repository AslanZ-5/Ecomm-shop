from django.contrib import admin
from django.urls import path,include
from shop import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls'))
]
