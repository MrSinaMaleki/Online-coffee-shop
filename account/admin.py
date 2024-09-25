from cProfile import Profile

from django.contrib import admin

from account.models import Human

# Register your models here.
admin.site.register(Human)