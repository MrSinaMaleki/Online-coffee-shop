from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Comments


@receiver([post_save, post_delete], sender=Comments)
def update_product_score(sender, instance, **kwargs):
    product = instance.product
    comments_count = product.comments.accepted().count()
    if comments_count > 0:
        product.score = sum([comment.score for comment in product.comments.accepted().all()]) / comments_count
    else:
        product.score = 5
    product.save()
