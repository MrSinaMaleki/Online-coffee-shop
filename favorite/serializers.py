from rest_framework import serializers

from account.models import Human
from favorite.models import Favorite
from rest_framework import validators
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.permissions import IsAuthenticated

class FavoriteAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'products']

    def create(self, validated_data):
        if self.context['request'].user.is_authenticated:
            user = Human.objects.get(pk=self.context['request'].user.id)
            return Favorite.objects.create(user=user, products=validated_data['products'])
        raise AuthenticationFailed('This user not authentication', code=400)

    def validate(self, data):
             products = Favorite.objects.filter(user=self.context['request'].user.id).values_list('products', flat=True)
             if data['products'].id in products:
                 raise validators.ValidationError('This product is already favorited')
             return data
class FavoriteRemoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'products']

    def create(self, validated_data):
        try:
            Favorite.objects.get(user=self.context['request'].user.id,products_id=validated_data['products']).delete()
        except Favorite.DoesNotExist:
            raise ValidationError('This product is not favorited')
        return validated_data