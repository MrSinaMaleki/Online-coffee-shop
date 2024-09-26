from rest_framework import serializers

from account.models import Human
from favorite.models import Favorite
from rest_framework.exceptions import AuthenticationFailed


class FavoriteAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['products']

    def create(self, validated_data):
        if self.context['request'].user.is_authenticated:

            user = Human.objects.get(pk=self.context['request'].user.id)
            if Favorite.objects.filter(products_id=validated_data['products'].id, user=user).exists():
                Favorite.objects.filter(products_id=validated_data['products'].id, user=user).delete()
                return validated_data
            else:
                return Favorite.objects.create(user=user, products_id=validated_data['products'].id)
        raise AuthenticationFailed('This user not authentication', code=400)
