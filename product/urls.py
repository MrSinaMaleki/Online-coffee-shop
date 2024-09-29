from django.urls import path
from .views import ProductListAPIView,ProductDetailAPIView,index
from django.views.generic import TemplateView
urlpatterns = [
    path('api/list/product', ProductListAPIView.as_view(), name='api_product-list'),
    path('api/detail/product/<int:pk>', ProductDetailAPIView.as_view(), name='api_product-detail'),
    path('<int:pk>', index, name='product-detail_view'),
    path('products/', TemplateView.as_view(template_name="product/all_products.html"), name='all-products'),

]
