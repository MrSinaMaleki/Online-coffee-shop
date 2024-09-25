from django.db import models
from core.models import DeleteLogicalBase
from django.core.exceptions import ValidationError


def validate_image_size(image):
    max_size_mb = 2
    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Image file size must be less than {max_size_mb} MB")


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class CoffeeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_coffee_shop=True)


class CoverPhotoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_cover=True)


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        related_name='subcategories',
        related_query_name='subcategories',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        indexes = [models.Index(fields=['title'])]

    def __str__(self):
        return self.title

class Product(DeleteLogicalBase):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    serial_number = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True)
    is_coffee_shop = models.BooleanField()
    timeline = models.CharField(max_length=9,
                                choices=(('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')),
                                null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    available = AvailableManager()
    coffeeshop = CoffeeManager()

    def clean(self):
        if self.is_coffee_shop and self.timeline:
            raise ValidationError("A product cannot belong to the coffee shop and have a timeline.")

        if not self.is_coffee_shop and not self.timeline:
            raise ValidationError("If the product does not belong to the coffee shop, a timeline must be provided.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at', 'price']
        indexes = [
            models.Index(fields=['is_available'])
        ]


class ProductImage(DeleteLogicalBase):
    product = models.ForeignKey(Product, related_query_name='images', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', validators=[validate_image_size])
    alt = models.TextField(blank=True, null=True)
    is_cover = models.BooleanField(default=False)

    covered = CoverPhotoManager()

    def clean(self):
        if self.is_cover:
            cover_images = ProductImage.objects.filter(product=self.product, is_cover=True).exclude(id=self.id)
            if cover_images.exists():
                raise ValidationError('Each product can only have one cover image.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.title} - {self.alt}"

    class Meta:
        indexes = [
            models.Index(fields=['product'])
        ]


class Ingredients(DeleteLogicalBase):
    title = models.CharField(max_length=100)
    products = models.ManyToManyField(Product,related_query_name='ingredients', related_name='ingredients', blank=True)

    def __str__(self):
        return self.title
