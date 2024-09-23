from rest_framework import serializers

from account.models import Human
from favorite.models import Favorite
from rest_framework import validators

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'products']

    def create(self, validated_data):
        user = Human.objects.get(pk=self.context['request'].user.id)
        if self.context['request'].user.is_authenticated:
            return Favorite.objects.create(user=user, products=validated_data['products'])
        raise serializers.ValidationError

    def validate(self, data):
        products = Favorite.objects.filter(user=self.context['request'].user.id).values_list('products', flat=True)
        print(data['products'].id in products)
        if data['products'].id in products:
            raise validators.ValidationError('This product is already favorited')
        return data

