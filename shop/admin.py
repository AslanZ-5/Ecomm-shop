from django.contrib import admin
from .models import *
from django import forms
from django.forms import ModelChoiceField, ModelForm
from django.core.exceptions import ValidationError
from PIL import Image


class ImageResolutionNotice(ModelForm):
    resolution = (400, 400)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = f"Upload an image with the minimum resolution {self.resolution[0]}x{self.resolution[1]} "

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_width,min_height = self.resolution
        if img.width < min_width or img.height < min_height:
            raise ValidationError("The image resolution is less than the minimum")
        return image
class LaptopAdmin(admin.ModelAdmin):
    form = ImageResolutionNotice

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='laptop'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartPhoneAdmin(admin.ModelAdmin):
    form = ImageResolutionNotice
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphone'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(SmartPhone, SmartPhoneAdmin)
admin.site.register(CartProduct)
