from pprint import pprint

from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from product.models import Product
from product.serializers import ProductSerializer, ProductDetailSerializer

def index(request,pk):
    return render(request ,'detailProduct.html',{'pk':pk})

# Create your views here.

class ProductListAPIView(ListAPIView):
    queryset = Product.available.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.available.all()
    serializer_class = ProductDetailSerializer
