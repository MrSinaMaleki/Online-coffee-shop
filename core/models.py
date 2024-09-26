from django.db import models


class ActiveLogicalBase(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class DeleteLogicalBase(models.Model):
    is_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True
