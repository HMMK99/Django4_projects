from django.contrib import admin

from .models import Post


# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'auther', 'publish', 'status']
    list_filter = ['auther', 'publish', 'status', 'created']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['auther']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
