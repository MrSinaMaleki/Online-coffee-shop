
from product.serializers import ProductOrderSerializer
from rest_framework import serializers

from product.models import Product
from .models import OrderItem, Order
from product.serializers import ProductSerializer


class OrderItemSerializers(serializers.ModelSerializer):
    product = ProductOrderSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id','product', 'is_delete', 'created_at', 'quantity']


class OrderSerializers(serializers.ModelSerializer):
    items = OrderItemSerializers(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['is_active', 'items','created_at','id']



class ProductSerializerCustom(ProductSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price')


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializerCustom(read_only=True)


    # total_price = serializers.ReadOnlyField(source='total_price')

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price_at_order', 'total_price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    # total_order_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'is_completed', 'is_paid', 'created_at', 'updated_at', 'items', 'total_order_price']
