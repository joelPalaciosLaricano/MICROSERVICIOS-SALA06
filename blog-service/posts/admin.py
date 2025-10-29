from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'status', 'published_at', 'views')
    list_filter = ('status', 'published_at')
    search_fields = ('title', 'body')
