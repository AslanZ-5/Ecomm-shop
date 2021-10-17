from django.contrib import admin
from .models import *
from django import forms
from django.forms import ModelChoiceField


class LaptopAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='laptop'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartPhoneAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphone'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Laptop,LaptopAdmin)
admin.site.register(SmartPhone,SmartPhoneAdmin)
admin.site.register(CartProduct)
