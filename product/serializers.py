from rest_framework import serializers
from .models import Product, Category, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'parent']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image', 'is_cover', 'alt')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True)
    images = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'title', 'price', 'quantity', 'is_available', 'serial_number', 'description', 'is_coffee_shop', 'timeline',
            'category', 'images')

    def get_images(self, obj):
        images = obj.images.filter(is_cover=True)
        return ProductImageSerializer(images, many=True).data