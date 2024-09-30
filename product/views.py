from pprint import pprint

from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product, Category
from product.serializers import ProductSerializer, ProductDetailSerializer


def index(request, pk):
    return render(request, 'product/detailProduct.html', {'pk': pk})


# Create your views here.
class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


# # todo
class ProductListView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            if Category.objects.filter(pk=pk).exists():
                category = Category.objects.get(pk=pk)
                categories = category.get_descendants(include_self=True)
                products = Product.objects.filter(category__in=categories)
                serializer = ProductSerializer(products, many=True)
                serializer.context['request']=request
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            products = Product.objects.all().order_by('category')
            serializer = ProductSerializer(products, many=True)
            serializer.context['request']=request
            return Response(serializer.data, status=status.HTTP_200_OK)

    # def get_queryset(self):
    #     time = self.request.query_params.get('time', None)
    #     if time:
    #         return Product.available.filter(
    #             Q(is_coffee_shop=True) | Q(timeline=time)
    #         )
    #
    #     return Product.available.filter(
    #         Q(is_coffee_shop=True) | Q(timeline__isnull=False)
    #     )
