from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'first_name', 'last_name', 'phone', 'address', 'status', 'buying_type', 'comment',
                  'order_date']
