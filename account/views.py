
from django.shortcuts import render
from .models import Human
# Create your views here.
from django.contrib.auth.models import User
Human.objects.create_user()

