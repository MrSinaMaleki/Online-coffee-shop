from pprint import pprint

from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View, DetailView, TemplateView
from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from order.models import OrderItem, Order
from product.models import Product, Category, Ingredients, ProductImage
from product.serializers import ProductSerializer, ProductDetailSerializer, CategorySerializer, ProductAdminSerializer, \
    IngredientsAdminSerializer, ImageAdminSerializer


class ProductDetailView(TemplateView):
    template_name = 'product/detailProduct.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'product/detailProduct.html'

# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['pk'] = self.object.pk
#     if 'product' in context:
#         del context['product']
#     return context


class CategoryView(TemplateView):
    template_name = 'product/all_products_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context


class ProductListView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            if Category.objects.filter(pk=pk).exists():
                category = Category.objects.get(pk=pk)
                categories = category.get_descendants(include_self=True)
                products = Product.objects.filter(category__in=categories)
                serializer = ProductSerializer(products, many=True)
                serializer.context['request'] = request
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            products = Product.objects.all().order_by('category')
            serializer = ProductSerializer(products, many=True)
            serializer.context['request'] = request
            return Response(serializer.data, status=status.HTTP_200_OK)


class ProductCoffeeShopListView(ListAPIView):
    queryset = Product.objects.coffeeshop()
    serializer_class = ProductSerializer


class ProductCategoryListView(APIView):
    def get(self, request, time=None):
        if time is not None:
            if Product.objects.filter(timeline=time).exists():
                products = Product.objects.filter(timeline=time)
                serializer = ProductSerializer(products, many=True)
                serializer.context['request'] = request
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            products = Product.objects.all().order_by('category')
            serializer = ProductSerializer(products, many=True)
            serializer.context['request'] = request
            return Response(serializer.data, status=status.HTTP_200_OK)


class RestaurantView(TemplateView):
    template_name = 'product/all_products_restaurant.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = self.kwargs['time']
        return context


'''all category'''


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


'''safety buffer'''


class SafetyBufferProductView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                quantity = Product.objects.get(pk=pk).quantity
                quantity_items = OrderItem.objects.filter(
                    Q(order__is_paid=False, order__is_completed=False,order__is_delete=False)).filter(product=pk)
                total = quantity - sum([i.quantity for i in quantity_items])
                return Response(data={'quantity': total}, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)


'''add product in admin panel'''


class AddCategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AddProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductAdminSerializer


class AddIngredientView(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsAdminSerializer


class AddProductImageView(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ImageAdminSerializer

