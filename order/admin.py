from django.contrib import admin
from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'updated_at', 'is_paid', 'is_completed')
    search_fields = ('user',)
    list_filter = ('is_paid', 'created_at')
    search_help_text = 'please enter user!'


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'order', 'order_item_price')
    search_fields = ('product',)
    search_help_text = 'please enter product!'


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
