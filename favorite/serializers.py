from django.db.models import Q
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
            favorite = Favorite.objects.filter(products_id=validated_data['products'].id,user=user)
            if favorite.exists():
                for i in favorite:
                     i.is_active=False
                     i.is_delete=True
                     i.save()
                return validated_data
            else:
                Favorite.objects.create(user=user, products_id=validated_data['products'].id)
                return validated_data
        raise AuthenticationFailed('This user not authentication', code=400)
