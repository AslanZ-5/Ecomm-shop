from django.contrib import admin
from .models import *
from django import forms
from django.forms import ModelChoiceField, ModelForm
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from PIL import Image


class ImageResolutionNotice(ModelForm):
    min_resolution = (199, 199)
    max_resolution = (500,500)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[
            'image'].help_text = mark_safe(f"<span style='color:red;'>Upload an image with the minimum resolution {self.min_resolution[0]}x{self.min_resolution[1]}</span> ")

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_width, min_height = self.min_resolution
        max_width, max_height = self.max_resolution
        if img.width < min_width or img.height < min_height:
            raise ValidationError("The image resolution is less than the minimum")
        if img.width > max_width or img.height > max_height:
            raise ValidationError("The image resolution is more than the minimum")
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
