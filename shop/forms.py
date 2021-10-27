from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['order_date'].label = 'Order received date'
    order_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Order
        fields = ['customer', 'first_name', 'last_name', 'phone', 'address', 'status', 'buying_type', 'comment',
                  'order_date']
