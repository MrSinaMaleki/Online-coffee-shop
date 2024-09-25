from django.contrib import admin
from .models import Human


class HumanAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']


admin.site.register(Human, HumanAdmin)

