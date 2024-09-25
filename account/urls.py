

from django.urls import path,include
from django.views.generic.base import TemplateView
from .views import SignUpAPIView, TempForm, LoginAPIView

urlpatterns = [
    # path('', include("django.contrib.auth.urls"), name='auth'),
    path("signup/signup_api/", SignUpAPIView.as_view(), name="signup_api"),
    path("login_api/", LoginAPIView.as_view(), name="login_api"),

    # path('API/temp', TempForm.as_view(), name="temp"),

    path("signup/", TemplateView.as_view(template_name='account/signin.html'), name="signup"),
    path("login/", TemplateView.as_view(template_name="account/login.html"), name="login"),
]