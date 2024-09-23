from django.urls import path
from .views import FavoriteCreateAPIView,favorite,FavoriteListAPIView

urlpatterns = [
    path('api/f', FavoriteCreateAPIView.as_view(), name='favorite'),

]