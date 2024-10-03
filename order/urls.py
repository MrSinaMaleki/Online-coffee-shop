from django.urls import path

from django.views.generic.base import TemplateView
from order.views import OrderItemList
from .views import AddToCartAPIView, CartView, PayOrderAPIView, CancelOrderAPIView, OrderHistoryView


urlpatterns = [
    path('api/ordrlist', OrderItemList.as_view(), name='order-list'),
    path('admin/', TemplateView.as_view(template_name='account/StaffShopPage.html'), name='staff_page'),
    path('cart/add/<int:product_id>/', AddToCartAPIView.as_view(), name='add-to-cart'),
    path('cart/pay/<int:order_id>/', PayOrderAPIView.as_view(), name='pay-order'),
    path('cart/cancel/<int:order_id>/', CancelOrderAPIView.as_view(), name='cancel-order'),
    path('history/', OrderHistoryView.as_view(), name='order-history'),
    path('cart/viewcart', CartView.as_view(), name='view-cart'),

    path('cart/', TemplateView.as_view(template_name="order/cart.html"), name='cart'),
    path('history_order/', TemplateView.as_view(template_name="order/history_of_sales.html"), name='history'),


]

