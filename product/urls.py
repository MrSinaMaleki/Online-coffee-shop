from django.urls import path
from .views import ProductListView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('api/products/', ProductListView.as_view(), name='product-list'),
   # path('', TemplateView.as_view(template_name='_base.html'))
]
