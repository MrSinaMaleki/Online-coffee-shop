from django.contrib import admin
from .models import Human


class HumanAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'gender', 'age', 'profile_image')
    list_filter = ('phone', 'age')
    search_fields = ('username', 'phone',)
    search_help_text = 'please enter phone number or username!'


admin.site.register(Human, HumanAdmin)
