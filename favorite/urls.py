from django.urls import path
from .views import FavoriteCreateAPIView,favorite,FavoriteListAPIView

urlpatterns = [
    path('',favorite, name='favorite'),
    path('api/f', FavoriteCreateAPIView.as_view(), name='favorite'),

]