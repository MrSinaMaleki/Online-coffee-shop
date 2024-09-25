from django.db import models
from django.contrib.auth.models import User
from core.models import DeleteLogicalBase


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Human(User, DeleteLogicalBase):
    phone = models.CharField(unique=True, max_length=11)
    gender = models.CharField(max_length=6, choices=(('male', 'Male'), ('female', 'Female')), null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_image', null=True, blank=True)


    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name: 'Account USER'
        verbose_name_plural: 'Account USERS'
        ordering = ['-date_joined']
