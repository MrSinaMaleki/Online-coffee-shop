from rest_framework import serializers
from .models import Human
from django.contrib.auth.models import User


class CustomUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = Human
        fields = '__all__'

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password2')

        human = Human.objects.create_user(username=validated_data['username'], password=password,
                                          email=validated_data['email'])
        return human


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        # This ensures that both fields are present
        if not data.get('username') or not data.get('password'):
            raise serializers.ValidationError("Username and password are required.")
        return data
