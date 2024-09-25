from rest_framework import serializers
from .models import Product, Category, ProductImage, Ingredients
from favorite.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title', 'parent']


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
            'id', 'title', 'price', 'description', 'is_coffee_shop',
            'timeline', 'category', 'images')

    def get_images(self, obj):
        images = obj.images.filter(is_cover=True)
        return ProductImageSerializer(images, many=True).data


# ********************************************************
class ProductIngratiatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('title',)


class ProductDetailSerializer(ProductSerializer):
    ingredients = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = (
            'id', 'title', 'price', 'quantity', 'serial_number', 'description', 'is_coffee_shop', 'timeline',
            'timeline', 'category', 'images',"ingredients")

    def get_images(self, obj):
        images = obj.images.filter()
        return ProductImageSerializer(images, many=True).data
    def get_ingredients(self, obj):
        print(obj.ingredients.all())
        ingredients = obj.ingredients.filter(is_delete=False)
        return ProductIngratiatingSerializer(ingredients, many=True).data
