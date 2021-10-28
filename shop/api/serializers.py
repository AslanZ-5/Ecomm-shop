from rest_framework import serializers
from shop.models import Category, SmartPhone, Laptop


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'slug'
        ]


class BaseProductSerializer:
    slug = serializers.SlugField(required=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects)
    title = serializers.CharField(required=True)
    price = serializers.DecimalField(max_digits=9, decimal_places=2, required=True)
    discount_price = serializers.FloatField()
    description = serializers.CharField(required=False)
    image = serializers.ImageField(required=True)


class SmartphoneSerializer(BaseProductSerializer, serializers.ModelSerializer):
    diagonal = serializers.CharField(required=True)
    display = serializers.CharField(required=True)
    resolution = serializers.CharField(required=True)
    ram = serializers.CharField(required=True)
    accum_volume = serializers.CharField(required=True)
    time_without_charge = serializers.CharField(required=True)
    sd = serializers.BooleanField(required=True)
    sd_volume_max = serializers.CharField(required=True)
    main_camera_mp = serializers.CharField(required=True)
    frontal_camera_mp = serializers.CharField()
    class Meta:
        model = SmartPhone
        fields = '__all__'
