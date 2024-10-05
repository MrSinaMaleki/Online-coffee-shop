from rest_framework import serializers
from account.models import User
from favorite.models import Favorite
from rest_framework.exceptions import AuthenticationFailed


class FavoriteAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['products']

    def create(self, validated_data):
        if self.context['request'].user.is_authenticated:
            user = User.objects.get(pk=self.context['request'].user.id)
            try:
                favorite = Favorite.objects.get(products_id=validated_data['products'].id, user=user)
                favorite.is_active = False
                favorite.is_delete = True
                favorite.save()
            except Favorite.DoesNotExist:
                Favorite.objects.create(user=user, products_id=validated_data['products'].id)
            return validated_data
        raise AuthenticationFailed('This user not authentication', code=400)
