from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from core.models import LogicalMixin
from core.managers import ActiveNotDeletedBaseManager


def validate_image_size(image):
    max_size_mb = 2
    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Image file size must be less than {max_size_mb} MB")


class Human(User, LogicalMixin):
    phone = models.CharField(unique=True, max_length=11, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(('male', 'Male'), ('female', 'Female')), null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_image', null=True, blank=True,
                                      validators=[validate_image_size])

    objects = ActiveNotDeletedBaseManager()

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name: 'Account USER'
        verbose_name_plural: 'Account USERS'
        ordering = ['-date_joined']
