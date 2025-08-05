from django.contrib import admin
from .models import Post, Subscription

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_preview', 'published_date')
    search_fields = ('title', 'content')

    def content_preview(self, obj):
        return obj.content[:50] + ('...' if len(obj.content) > 50 else '')
    content_preview.short_description = 'Content Preview'

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
