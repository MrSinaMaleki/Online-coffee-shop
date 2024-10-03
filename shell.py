import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from product.models import Product, Ingredients, Category

# Category.objects.create(title='coffee')
# Category.objects.create(title='food')
# Category.objects.create(title='coffee')
# Category.objects.create(title='coffee')
# Category.objects.create(title='coffee')
# coffee = Category.objects.get(id=1)
# food = Category.objects.get(id=2)
# Category.objects.create(title='espresso', parent=coffee)
# Category.objects.create(title='latte', parent=coffee)
# Category.objects.create(title='cappuccino', parent=coffee)
# Category.objects.create(title='pizza', parent=food)
# Category.objects.create(title='sandwich', parent=food)
# Category.objects.create(title='salad', parent=food)

