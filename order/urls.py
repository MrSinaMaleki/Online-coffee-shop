from django.urls import path
from .views import Cart
urlpatterns = [
    path('cart/',Cart.as_view(), name='cart')

]