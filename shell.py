import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from product.models import Product,Ingredients

products = Product.objects.get(pk=1)
print(products.ingredients.all())
