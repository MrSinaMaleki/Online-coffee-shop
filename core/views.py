from rest_framework import status, generics
from .models import ActiveLogicalBase
from .serializers import ActiveSerializer


class ActiveDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActiveLogicalBase.objects.all()
    serializer_class = ActiveSerializer
