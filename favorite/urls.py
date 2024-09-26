from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import FavoriteCreateAPIView

urlpatterns = [
    path('api/favorite/create', FavoriteCreateAPIView.as_view(), name='favoriteCreate'),


]
