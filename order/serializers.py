from rest_framework import serializers

from product.models import Product
from .models import OrderItem, Order
from product.serializers import ProductOrderSerializer

from rest_framework import serializers

from product.models import Product
from .models import OrderItem, Order
from product.serializers import ProductOrderSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductOrderSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id','product', 'is_delete', 'created_at', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['is_active', 'order_item','created_at','id']

