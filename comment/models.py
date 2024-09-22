from django.db import models
from account.models import DeleteLogicalBase, Human
from product.models import Product


class AcceptedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_accepted=True)


class Comments(DeleteLogicalBase):
    text = models.TextField(max_length=500)
    user = models.ForeignKey(Human, on_delete=models.SET_NULL, null=True, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    score = models.PositiveIntegerField(default=5)
    is_accepted = models.BooleanField(default=False)
    reply_comments = models.ForeignKey('Comments', on_delete=models.CASCADE, null=True,
                                       related_name='child', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    accepted = AcceptedManager()

    def __str__(self):
        return f'{str(self.id)} -> {self.score} -> {self.user.username}'

    class Meta:
        ordering = ['-created_at']
