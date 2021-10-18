from django.shortcuts import render
from django.views.generic import DetailView
from .models import Laptop, SmartPhone


def index(request):
    return render(request, 'shop/base.html')



