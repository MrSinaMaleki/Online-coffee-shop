from .serializers import OrderItemSerializers, OrderSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from account.models import Human
from .models import Order, OrderItem, Product
from .serializers import OrderSerializer


class OrderItemList(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderItemSerializers

    def get(self, request, filterOrder=None):
        if request.user.is_superuser:
            if filterOrder is None:
                orders_is_not_complete = Order.objects.paid().filter(is_completed=False).order_by('-created_at')
                serializer = OrderSerializers(orders_is_not_complete, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message : is not super user'}, status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        print(request.data)
        if request.user.is_superuser:
            order = Order.objects.filter(pk=request.data['orderId']).first()
            if order is not None:
                order.is_completed = True
                order.save()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response({'message : is not super user'}, status=status.HTTP_403_FORBIDDEN)


class AddToCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        user = Human.objects.get(user_ptr_id=request.user.id)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            quantity = int(request.data.get('quantity', 1))
            if quantity <= 0:
                return Response({'error': 'Quantity must be greater than zero.'}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({'error': 'Invalid quantity provided.'}, status=status.HTTP_400_BAD_REQUEST)

        if product.quantity < quantity:
            return Response({'error': 'The quantity exceeds the available stock.'}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.not_paid().filter(user=user).first()

        if not order:
            order = Order.objects.create(user=user)

        order_item, item_created = OrderItem.objects.get_or_create(order=order, product=product)

        if not item_created:
            order_item.quantity += quantity
            if product.quantity < order_item.quantity:
                return Response({'error': 'The quantity exceeds the available stock.'},
                                status=status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE)
        else:
            order_item.price_at_order = product.price
            order_item.quantity = quantity

        order_item.save()

        return Response({'message': f'{quantity} items of {product.title} added to the order successfully.'},
                        status=status.HTTP_200_OK)


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = Human.objects.get(user_ptr_id=request.user.id)
        order = Order.objects.not_paid().filter(user=user).first()

        if not order:
            return Response({'message': 'Your cart is empty.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PayOrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, order_id):
        user = Human.objects.get(user_ptr_id=request.user.id)
        try:
            order = Order.objects.not_paid().filter(id=order_id, user=user).first()
            if not order:
                return Response({'error': 'Order not found or already paid.'}, status=status.HTTP_404_NOT_FOUND)

            for item in order.items.all():
                product = item.product
                if product.quantity >= item.quantity:
                    product.quantity -= item.quantity
                    if product.quantity == 0:
                        product.is_active = False
                    product.save()
                else:
                    return Response({'error': 'Not enough stock for one or more products.'},
                                    status=status.HTTP_400_BAD_REQUEST)

            order.is_paid = True
            order.save()

            return Response({'message': 'Order paid successfully.'}, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)


class CancelOrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, order_id):
        user = Human.objects.get(user_ptr_id=request.user.id)
        try:
            order = Order.objects.not_paid().filter(id=order_id, user=user).first()
            if not order:
                return Response({'error': 'Order not found or already paid.'}, status=status.HTTP_404_NOT_FOUND)

            order.is_delete = True
            order.save()

            return Response({'message': 'Order canceled successfully.'}, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)


class OrderHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = Human.objects.get(user_ptr_id=request.user.id)
        orders = Order.objects.paid().filter(user=user)

        if not orders.exists():
            return Response({'message': 'You have no previous orders.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
