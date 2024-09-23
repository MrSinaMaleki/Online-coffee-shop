from pprint import pprint

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from product.models import Product
from product.serializers import ProductSerializer


# Create your views here.
def books(request):
    return render(request, "_base.html")


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
