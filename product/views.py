from rest_framework.generics import ListAPIView
from product.models import Product
from django.db.models import Q
from .serializers import ProductSerializer


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        time = self.request.query_params.get('time', None)
        if time:
            return Product.available.filter(
                Q(is_coffee_shop=True) | Q(timeline=time)
            )

        return Product.available.filter(
            Q(is_coffee_shop=True) | Q(timeline__isnull=False)
        )
