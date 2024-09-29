from django.db import models
from account.models import LogicalMixin, Human
from product.models import Product
from core.managers import ActiveNotDeletedBaseManager


class Favorite(LogicalMixin):
    user = models.ForeignKey(Human, on_delete=models.CASCADE, related_query_name="favorites", related_name='favorites')
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_query_name="products",
                                 related_name='products')

    objects = ActiveNotDeletedBaseManager()

    def __str__(self):
        return f"{self.user} -> {self.products}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'products'], name='unique_favorite')
        ]
