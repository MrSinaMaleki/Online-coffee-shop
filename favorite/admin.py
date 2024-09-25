from django.contrib import admin
from .models import Favorite


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'products')
    list_filter = ('products',)
    search_fields = ('products', 'user')
    search_help_text = 'please enter product !'


admin.site.register(Favorite, FavoriteAdmin)
