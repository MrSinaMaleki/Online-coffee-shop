from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import FavoriteCreateAPIView,FavoriteDeleteAPIView

urlpatterns = [
    path('api/favorite/create', FavoriteCreateAPIView.as_view(), name='favoriteCreate'),
    path('api/favorite/delete', FavoriteDeleteAPIView.as_view(), name='favoriteDelete'),

]
