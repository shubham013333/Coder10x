from django.contrib import admin
from .models import Post  # Ensure this matches the model name

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'published_date')
