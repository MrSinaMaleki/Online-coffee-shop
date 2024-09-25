from multiprocessing.managers import Token

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate
from .models import Human
from .serializers import CustomUserSerializer, LoginSerializer


class SignUpAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"stat": "User was created!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)  # Use self.serializer_class
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data['username']  # Fetch data using validated_data
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key, "Success": "Login Successfully"})

            return Response({'Message': 'Invalid Username and Password'}, status=401)

class TempForm(CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = Human.objects.all()
