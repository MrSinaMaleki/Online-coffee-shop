from django.contrib import admin
from .models import Human


class HumanAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'gender', 'profile_image', 'get_age')
    list_filter = ('phone',)
    search_fields = ('username', 'phone')
    search_help_text = 'please enter phone number or username!'

    def get_age(self, obj):
        return obj.age
    get_age.short_description = 'Age'


admin.site.register(Human, HumanAdmin)
