from rest_framework import status, generics
from .models import Product
from .serializers import ProductSerializer
# from django.db.models import Q


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



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

