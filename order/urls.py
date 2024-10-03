from django.urls import path

from django.views.generic.base import TemplateView
from order.views import OrderItemList


urlpatterns = [
    path('api/1', OrderItemList.as_view(), name='order-list'),
    path('1/', TemplateView.as_view(template_name='account/StaffShopPage.html'), name='staff_page'),


]