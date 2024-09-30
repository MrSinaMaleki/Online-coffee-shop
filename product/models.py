from django.db import models
from core.models import LogicalMixin
from django.core.exceptions import ValidationError
from core.managers import ActiveNotDeletedBaseManager


def validate_image_size(image):
    max_size_mb = 2
    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Image file size must be less than {max_size_mb} MB")


class ProductManager(ActiveNotDeletedBaseManager):
    def coffeeshop(self):
        return super().get_queryset().filter(is_coffee_shop=True)


class ProductPhotoManager(ActiveNotDeletedBaseManager):
    def covered(self):
        return super().get_queryset().filter(is_cover=True)


class Category(LogicalMixin):
    title = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        related_name='subcategories',
        related_query_name='subcategories',
        blank=True,
        null=True
    )

    objects = ActiveNotDeletedBaseManager()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        indexes = [models.Index(fields=['title'])]

    def __str__(self):
        return self.title

    @staticmethod
    def calculate_max_depth(root_category):

        """
        Recursively calculates the maximum depth of the category tree starting from a given root category.
        """

        if not root_category.subcategories.exists():
            return 0
        else:
            return 1 + max(Category.calculate_max_depth(sub) for sub in root_category.subcategories.all())

    def get_descendants(self, include_self=False, levels=None):

        """
        Fetch all descendants of the current category using dynamically determined levels of prefetching.
        If 'levels' is not provided, calculate it based on the maximum depth of the category tree.
        """

        if levels is None:
            levels = Category.calculate_max_depth(self)

        result = [self] if include_self else []
        queryset = Category.objects.all()

        for _ in range(levels):
            queryset = queryset.prefetch_related('subcategories')

        categories = queryset.filter(id=self.id)

        # noinspection PyShadowingNames
        def collect_categories(category, current_level):

            if current_level > 0:
                for subcategory in category.subcategories.all():
                    result.append(subcategory)
                    collect_categories(subcategory, current_level - 1)

        for category in categories:
            collect_categories(category, levels)

        return result

    def get_parents(self, includes_self=False, levels=None) -> list:
        '''if level back parent category '''
        level = Category.objects.count() if levels is None else levels
        category_list =[self] if includes_self else []
        parent = self.parent
        for _ in range(level):
            if parent is not None:
                category_list.append(c := parent)
                parent = c.parent
            else:
                break
        return category_list


class Product(LogicalMixin):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    serial_number = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='category',
                                 related_query_name='categorys', null=True)
    is_coffee_shop = models.BooleanField()
    timeline = models.CharField(max_length=9,
                                choices=(('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')),
                                null=True, blank=True)

    objects = ProductManager()

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
            models.Index(fields=['is_active'])
        ]


class ProductImage(LogicalMixin):
    product = models.ForeignKey(Product, related_query_name='images', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', validators=[validate_image_size])
    alt = models.TextField(blank=True, null=True)
    is_cover = models.BooleanField(default=False)

    objects = ProductPhotoManager()

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


class Ingredients(LogicalMixin):
    title = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, related_query_name='ingredients', related_name='ingredients', blank=True)

    objects = ActiveNotDeletedBaseManager()

    def __str__(self):
        return self.title
