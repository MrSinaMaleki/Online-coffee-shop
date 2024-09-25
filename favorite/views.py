from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from favorite.models import Favorite
from rest_framework.generics import CreateAPIView, DestroyAPIView
from django.contrib.auth.decorators import login_required
from favorite.serializers import FavoriteAddSerializer,FavoriteRemoveSerializer
from product.models import Product


class FavoriteCreateAPIView(CreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteAddSerializer
    permission_classes = [IsAuthenticated]


class FavoriteDeleteAPIView(CreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteRemoveSerializer
    permission_classes = [IsAuthenticated]
