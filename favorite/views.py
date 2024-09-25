from rest_framework import status, generics
from .models import Favorite
from .serializers import FavoriteSerializer


class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

