from django.db.models.signals import pre_save
from django.dispatch import receiver
from product.models import Product


@receiver(pre_save, sender=Product)
def calculate_new_price(sender, instance, **kwargs):
    instance.price = instance.old_price - instance.off
