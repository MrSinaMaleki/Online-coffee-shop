from django.db import models


class LogicalMixin(models.Model):
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def activate(self):
        self.is_active = True
        self.save(update_fields=['is_active'])

    def deactivate(self):
        self.is_active = False
        self.save(update_fields=['is_active'])

    def make_delete(self):
        self.is_delete = True
        self.save(update_fields=['is_delete'])

    def make_undelete(self):
        self.is_delete = False
        self.save(update_fields=['is_delete'])
