from django.contrib import admin
from .models import Comments


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'score', 'text', 'is_accepted', 'created_at']

    def get_readonly_fields(self, request, obj=None):
        if obj and not obj.text:
            return ['is_accepted'] + self.readonly_fields
        return self.readonly_fields


admin.site.register(Comments, CommentsAdmin)
