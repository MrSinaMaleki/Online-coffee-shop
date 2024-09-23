from pprint import pprint

from django.shortcuts import render
from rest_framework.generics import ListAPIView

from product.models import Product
from product.serializers import ProductSerializer


# Create your views here.

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
