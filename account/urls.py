

from django.urls import path,include
from django.views.generic.base import TemplateView
from .views import SignUpAPIView,TempForm

urlpatterns = [
    # path('', include("django.contrib.auth.urls"), name='auth'),
    path("signup_api/", SignUpAPIView.as_view(), name="signup_api"),

    path('API/temp', TempForm.as_view(), name="temp"),

    path("", TemplateView.as_view(template_name='account/signin.html'), name="signup"),
]