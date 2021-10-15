from django.shortcuts import render
from .models import Products

def index(request):
    products = Products.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        products = products.filter(title__icontains=item_name)
    return render(request,'shop/index.html',{'products':products})

