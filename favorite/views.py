from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import Human
from favorite.models import Favorite
from rest_framework.generics import CreateAPIView

from favorite.serializers import FavoriteSerializer
from product.models import Product


# Create your views here.

# def favorite(request):
#     return render(request, '_base.html')
#
#
class FavoriteCreateAPIView(CreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer



# class FavoriteListAPIView(APIView):
#     def get(self, request):
#         favorites = Favorite.objects.all()
#         serializer = FavoriteSerializer(favorites, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         print(request.data, request.user.pk)
#         p = Product.objects.get(pk=request.user.pk)
#         user = Human.objects.get(pk=request.user.pk)
#         print(p)
#         if request.user.is_authenticated:
#             serializer = FavoriteSerializer(data={"products": p.id, 'user': user.id})
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response( status=status.HTTP_400_BAD_REQUEST)