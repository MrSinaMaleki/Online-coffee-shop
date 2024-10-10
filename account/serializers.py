import re

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from favorite.models import Favorite
# from .models import User
from favorite.serializers import FavoriteAddSerializer
from rest_framework import serializers
from account.validators import CustomPasswordValidator

from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")


        obj = CustomPasswordValidator()
        obj.validate(data['password'])

        # regex = r'^((?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9]).{6,})\S$'
        #
        # if not re.match(regex, data['password']):
        #     raise serializers.ValidationError(
        #         'Password must contain at least 6 characters, including one uppercase letter, one lowercase letter, and one number.')

        email = data.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("A user with this email already exists.")

        return data

    def create(self, validated_data):
        # print(validated_data)
        password = validated_data.pop('password')
        validated_data.pop('password2')

        human = User.objects.create_user(password=password,
                                         email=validated_data['email'])
        return human


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        # This ensures that both fields are present
        if not data.get('email') or not data.get('password'):
            raise serializers.ValidationError("Username and password are required.")
        return data


class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords must match.")
        return data


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    favorites = FavoritesSerializer(many=True, read_only=True)

    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'gender', 'profile_image', 'favorites',
                  'date_of_birth', 'age']
        extra_kwargs = {
            'username': {'read_only': True},
        }

    def update(self, instance, validated_data):
        profile_image = validated_data.pop('profile_image', None)

        if profile_image:
            instance.profile_image = profile_image

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
