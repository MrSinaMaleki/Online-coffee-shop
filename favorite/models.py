from django.db import models
from account.models import Human
from product.models import Product


class Favorite(models.Model):
    user = models.OneToOneField(Human, on_delete=models.CASCADE, related_name='favorites')
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"{self.user} -> {self.products}"
