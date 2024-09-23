from django.urls import path
from .views import ProductListAPIView
urlpatterns = [
    path('api/book', ProductListAPIView.as_view(), name='product-list'),

]