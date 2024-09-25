from rest_framework import status, generics
from .models import Human
from .serializers import HumanSerializer


class HumanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer

