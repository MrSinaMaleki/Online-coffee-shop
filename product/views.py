from pprint import pprint

from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from product.models import Product
from product.serializers import ProductSerializer, ProductDetailSerializer


def index(request, pk):
    return render(request, 'product/detailProduct.html', {'pk': pk})


# Create your views here.

class ProductListAPIView(ListAPIView):
    queryset = Product.available.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.available.all()
    serializer_class = ProductDetailSerializer

# # todo
# class ProductListView(ListAPIView):
#     serializer_class = ProductSerializer
#
#     def get_queryset(self):
#         time = self.request.query_params.get('time', None)
#         if time:
#             return Product.available.filter(
#                 Q(is_coffee_shop=True) | Q(timeline=time)
#             )
#
#         return Product.available.filter(
#             Q(is_coffee_shop=True) | Q(timeline__isnull=False)
#         )
