from django.contrib import admin
from .models import Comments


class CommentsAdmin(admin.ModelAdmin):

    list_display = ('id', 'text', 'user', 'product', 'score', 'is_accepted', 'reply_comments', 'created_at')
    list_filter = ('user', 'product', 'score')
    search_fields = ('product',)
    list_display_links = ('id', 'user')
    search_help_text = 'please enter product!'
    readonly_fields = ('score', 'text')


    def get_readonly_fields(self, request, obj=None):
        if obj and not obj.text:
            return ['is_accepted'] + self.readonly_fields
        return self.readonly_fields



admin.site.register(Comments, CommentsAdmin)
