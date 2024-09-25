from tkinter.font import names

from django.urls import path,include
from django.views.generic.base import TemplateView
from .views import SignUpAPIView, TempForm, LoginAPIView, ForgetPasswordAPIView, ResetPasswordAPIView

urlpatterns = [
    # path('', include("django.contrib.auth.urls"), name='auth'),

    path('', TemplateView.as_view(template_name="temp.html"), name='home'),
    path("signup/signup_api/", SignUpAPIView.as_view(), name="signup_api"),
    path("login_api/", LoginAPIView.as_view(), name="login_api"),

    # path('API/temp', TempForm.as_view(), name="temp"),

    path('forgot_password/', ForgetPasswordAPIView.as_view(), name='forgot_password'),
    path('reset_password/<uidb64>/<token>/', ResetPasswordAPIView.as_view(), name='reset_password'),


    path("signup/", TemplateView.as_view(template_name='account/signin.html'), name="signup"),
    path("login/", TemplateView.as_view(template_name="account/login.html"), name="login"),

    path("forgot_password_view/", TemplateView.as_view(template_name="account/forgotpassword.html"), name="forgot_password_view"),

    path("reset_password_view/<uidb64>/<token>/", TemplateView.as_view(template_name="account/resetpassword.html"),
         name="reset_password_view"),
]