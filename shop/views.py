from django.shortcuts import render
from .models import Products
from django.core.paginator import  Paginator

def index(request):
    products = Products.objects.all()
    item_name = request.GET.get('item_name')
    #search code
    if item_name != '' and item_name is not None:
        products = products.filter(title__icontains=item_name)
    #paginator code
    paginator = Paginator(products,3)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request,'shop/index.html',{'products':products})

def detail(request,id):
    product = Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product':product})