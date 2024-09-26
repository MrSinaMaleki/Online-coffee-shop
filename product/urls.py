from django.urls import path
from .views import ProductListAPIView,ProductDetailAPIView,index
from django.views.generic import TemplateView
urlpatterns = [
    path('api/list/product', ProductListAPIView.as_view(), name='product-list'),
    path('api/detail/product/<int:pk>', ProductDetailAPIView.as_view(), name='product-detail'),
    path('<int:pk>', index, name='product-detail1'),

]