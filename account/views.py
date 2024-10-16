from multiprocessing.managers import Token

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from config import settings
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.shortcuts import redirect

from django.contrib.auth import authenticate, login, logout
from .models import User
from .serializers import CustomUserSerializer, LoginSerializer, ForgetPasswordSerializer, ResetPasswordSerializer, \
    ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ProfileSerializer


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
            email = serializer.validated_data['email']  # Fetch data using validated_data
            password = serializer.validated_data['password']

            user = authenticate(email=email, password=password)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({"token": token.key, "Success": "Login Successfully"})

            return Response({'Message': 'Invalid Username and Password'}, status=401)


def logout_view(request):
    logout(request)
    return redirect("/")


class ForgetPasswordAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ForgetPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"Message": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            reset_url = f"{request.scheme}://{request.get_host()}/account/reset_password/{uid}/{token}/"

            send_mail(
                subject="Password Reset Request",
                message=f"Please use the link below to reset your password:\n{reset_url}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
            return Response({"detail": "Password reset link sent. Please check your email."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordAPIView(APIView):
    def post(self, request, uidb64, token, *args, **kwargs):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                uid = urlsafe_base64_decode(uidb64).decode()
                user = User.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                return Response({"Message": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)

            if not default_token_generator.check_token(user, token):
                return Response({"Message": "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.validated_data['password'])
            user.save()

            return Response({"detail": "Password has been successfully reset."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class TempForm(CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = User.objects.all()
