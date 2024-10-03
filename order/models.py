from django.db import models
from account.models import Human, LogicalMixin
from product.models import Product
from core.managers import ActiveNotDeletedBaseManager


class OrderManager(ActiveNotDeletedBaseManager):
    def completed(self):
        return self.get_queryset().filter(is_completed=True)

    def not_completed(self):
        return self.get_queryset().filter(is_completed=False)

    def paid(self):
        return self.get_queryset().filter(is_paid=True)

    def not_paid(self):
        return self.get_queryset().filter(is_paid=False)


class Order(LogicalMixin):
    user = models.ForeignKey(Human, on_delete=models.CASCADE, related_name='orders')
    is_completed = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    objects = OrderManager()

    def __str__(self):
        return str(self.id)

    @property
    def total_order_price(self):
        return sum(item.total_price for item in self.items.all())

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['is_completed']),
            models.Index(fields=['is_paid']),
        ]


class OrderItem(LogicalMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item',related_query_name='order_items')
    price_at_order = models.FloatField()

    objects = ActiveNotDeletedBaseManager()

    def save(self, *args, **kwargs):
        if not self.price_at_order:
            self.price_at_order = self.product.price
        super().save(*args, **kwargs)

    @property
    def total_price(self):
        return self.quantity * self.price_at_order

    def __str__(self):
        return str(self.id)

    class Meta:
        unique_together = ('product', 'order')
