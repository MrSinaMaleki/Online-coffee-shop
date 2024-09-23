from django.urls import path
from .views import ProductListAPIView,books
urlpatterns = [
    path('',books,name='books'),
    path('api/book', ProductListAPIView.as_view(), name='product-list'),
    # path("", index, name="index"),
]