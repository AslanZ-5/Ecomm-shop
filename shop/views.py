from django.shortcuts import render
from .models import Products

def index(request):
    products = Products.objects.all()
    return render(request,'shop/index.html',{'products':products})

