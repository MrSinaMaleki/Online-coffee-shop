from django.urls import path
from .views import ProductListView, ProductCoffeeShopListView, CategoryView, \
    ProductDetailView, ProductDetailAPIView, ProductCategoryListView, RestaurantView, CategoryListView
from django.views.generic import TemplateView
urlpatterns = [
    path('api/list/product/category/<int:pk>', ProductListView.as_view(), name='api_product-category-list'),
    path('api/list/category', CategoryListView.as_view(), name='api-category-list'),
    path('api/list/product', ProductListView.as_view(), name='api_product-list'),
    path('api/detail/product/<int:pk>', ProductDetailAPIView.as_view(), name='api_product-detail'),
    path('api/list/coffeeshop', ProductCoffeeShopListView.as_view(), name='api_product-coffeeshop-list'),
    path('api/list/restaurant/<str:time>', ProductCategoryListView.as_view(), name='api_product-restaurant-list'),
    path('<int:pk>', ProductDetailView.as_view(), name='product-detail_view'),
    path('products/', TemplateView.as_view(template_name="product/all_products.html"), name='all-products'),
    path('category/<int:pk>', CategoryView.as_view(), name='category-product-list'),
    path('coffeeshop/', TemplateView.as_view(template_name="product/all_products_coffeeshop.html"), name='coffeeshop'),
    path('restaurant/<str:time>', RestaurantView.as_view(), name='restaurant'),
]
