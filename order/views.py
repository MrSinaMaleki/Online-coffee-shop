from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order, OrderItem
from rest_framework.permissions import IsAuthenticated
# from .serializers import OrderSerializer
from .serializers import OrderItemSerializer, OrderSerializer


# class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


# class OrderItemList(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = OrderItemSerializer
#     def get(self, request, format=None):
#         user = request.user
#         if request.user.is_superuser:
#             orders_is_not_complete = Order.objects.filter(is_completed=False)
#
#             orders_item=[item.order_item.all() for item in orders_is_not_complete]
#             print(orders_item)


class OrderItemList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemList(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderItemSerializer

    def get(self, request, filterOrder=None):
        if request.user.is_superuser:
            if filterOrder is None:
                orders_is_not_complete = Order.objects.filter(is_completed=False).order_by('-created_at')
                serializer = OrderSerializer(orders_is_not_complete, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message : is not super user'}, status=status.HTTP_403_FORBIDDEN)
    def post(self, request):
        print(request.data)
        if request.user.is_superuser:
            order=Order.objects.filter(pk=request.data['orderId']).first()
            if order is not None:
                order.is_completed = True
                order.save()
                return Response( status=status.HTTP_200_OK)
            return Response( status=status.HTTP_400_BAD_REQUEST)
        return Response({'message : is not super user'}, status=status.HTTP_403_FORBIDDEN)
