from rest_framework import serializers
from .models import Product, Category, ProductImage, Ingredients
from favorite.models import Favorite

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'parent')


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image', 'is_cover', 'alt')


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(read_only=True)
    favorite = serializers.SerializerMethodField(read_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = (
            'id', 'title', 'price', 'description', 'is_coffee_shop',
            'timeline', 'images', 'favorite','category')

    def get_images(self, obj):
        images = obj.images.filter(is_cover=True)
        return ProductImageSerializer(images, many=True).data

    def get_favorite(self, obj):
        print(obj)
        print(self.context)
        if self.context['request'].user.is_authenticated:
            return Favorite.objects.filter(user_id=self.context['request'].user, products_id=obj.id).exists()
        return False




# ********************************************************
class ProductIngratiatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('title',)


class ProductDetailSerializer(ProductSerializer):
    ingredients = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)
    category = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = (
            'id', 'title', 'price', 'quantity', 'serial_number', 'description', 'is_coffee_shop', 'timeline',
            'timeline','category', 'images', "ingredients", 'favorite')

    def get_images(self, obj):
        images = obj.images.filter()
        return ProductImageSerializer(images, many=True).data

    def get_ingredients(self, obj):
        ingredients = obj.ingredients.filter(is_delete=False)
        return ProductIngratiatingSerializer(ingredients, many=True).data

    def get_category(self, obj):
        if(category_in_product := Category.objects.filter(id=obj.category.id)).exists():
            category = category_in_product.first()
            category_id=category.get_parents(includes_self=True)
            return CategorySerializer(category_id, many=True).data
        return False

#************************************order*************************

class ProductOrderSerializer(ProductSerializer):
        class Meta:
            model = Product
            fields = ('id', 'title','images','category','description')
