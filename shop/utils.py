from django.db import models

def recalc(cart):
    # take all cartproducts from products, refer to all models final_price row and return their sum
    cart_data = cart.products.aggregate(models.Sum('final_price'), models.Sum('qty'))
    if cart_data['final_price__sum']:
        cart.final_price = cart_data['final_price__sum']
    else:
        cart.final_price = 0
    cart.total_product = cart_data['qty__sum']
    if cart.total_product == None:
        cart.total_product = 0
