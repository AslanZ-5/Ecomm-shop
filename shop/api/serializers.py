from rest_framework import serializers
from shop.models import Category

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Category
        fields = [
            'id','name', 'slug'
        ]
