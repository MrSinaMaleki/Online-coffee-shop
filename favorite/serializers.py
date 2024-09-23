from rest_framework import serializers
from favorite.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'products']
        extra_kwargs = {'user': {'read_only': True}}

    def create(self, validated_data):
        print(self.context['request'].user)
        print(validated_data['products'])
        if self.context['request'].user.is_authenticated:
            return Favorite.objects.create(user=self.context['request'].user, products=validated_data['products'])
        raise serializers.ValidationError
