from django.urls import path
from .views import FavoriteCreateAPIView

urlpatterns = [
    path('api/f', FavoriteCreateAPIView.as_view(), name='favorite'),
]