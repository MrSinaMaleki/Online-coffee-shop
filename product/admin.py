from django.contrib import admin
from .models import Product, Category, ProductImage,Ingredients

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(Ingredients)