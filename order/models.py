from django.db import models
from account.models import Human
from core.models import DeleteLogicalBase
from product.models import Product


class CompletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_completed=True)


class PaidManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_paid=True)


class Order(DeleteLogicalBase):
    user = models.ForeignKey(Human, on_delete=models.CASCADE, related_name='order')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False)

    completed = CompletedManager()
    paid = PaidManager()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user'])
        ]


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_item')
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')

    @property
    def order_item_price(self):
        return self.quantity*self.product.price

    def __str__(self):
        return str(self.id)
