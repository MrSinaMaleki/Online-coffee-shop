from django.shortcuts import render
from rest_framework.response import Response
from favorite.models import Favorite
from rest_framework.generics import CreateAPIView

from favorite.serializers import FavoriteSerializer


# Create your views here.


class FavoriteCreateAPIView(CreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
