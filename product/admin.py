from django.contrib import admin

from .models import Product, Category, ProductImage, Ingredients, CoffeeManager, AvailableManager, CoverPhotoManager, DeleteLogicalBase


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'quantity', 'serial_number', 'category', 'created_at', 'updated_at')
    list_filter = ('is_available',)
    search_fields = ('title', 'price')
    readonly_fields = ('is_available',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    search_fields = ('title',)

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'alt', 'is_over', 'objects', 'covered')
    search_fields = ('product',)

class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('title', 'product')
    search_fields = ('title',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Ingredients, IngredientsAdmin)
