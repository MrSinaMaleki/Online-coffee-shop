from django.db import models

from account.models import LogicalMixin, User
from order.models import OrderItem
from product.models import Product
from django.core.exceptions import ValidationError
from core.managers import ActiveNotDeletedBaseManager


class CommentManager(ActiveNotDeletedBaseManager):
    def accepted(self):
        return super().get_queryset().filter(is_accepted=True)

    def not_accepted(self):
        return super().get_queryset().filter(is_accepted=False)


class Comments(LogicalMixin):
    text = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    score = models.PositiveIntegerField(default=5)
    is_accepted = models.BooleanField(default=False)
    reply_comments = models.ForeignKey('Comments', on_delete=models.CASCADE, null=True,
                                       related_name='child',related_query_name="child", blank=True)

    objects = CommentManager()

    @property
    def is_buyer(self):
        if not self.user:
            return False

        return OrderItem.objects.filter(
            order__user=self.user,
            order__is_paid=True,
            product=self.product,
        ).exists()

    def clean(self):
        if not (0 <= self.score <= 5):
            raise ValidationError('Score must be between 0 and 5')
        if self.reply_comments and self.reply_comments == self:
            raise ValidationError('A comment cannot reply to itself.')

    def save(self, *args, **kwargs):
        self.clean()
        if not self.text:
            self.is_accepted = True
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{str(self.id)} -> {self.score} -> {self.user.first_name} , {self.user.last_name}'

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Comments'
