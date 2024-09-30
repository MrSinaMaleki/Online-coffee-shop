from django.urls import path
from .views import ProductDetailAPIView,index,ProductListView
from django.views.generic import TemplateView
urlpatterns = [
    path('api/list/product/category/<int:pk>', ProductListView.as_view(), name='api_product-category-list'),
    path('api/list/product', ProductListView.as_view(), name='api_product-list'),
    path('api/detail/product/<int:pk>', ProductDetailAPIView.as_view(), name='api_product-detail'),
    path('<int:pk>', index, name='product-detail_view'),
    path('products/', TemplateView.as_view(template_name="product/all_products.html"), name='all-products'),

]
