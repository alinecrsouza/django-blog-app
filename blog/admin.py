from django.contrib import admin

from blog.models import Category, Post, Author, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'category_id')
    search_fields = ['name', 'content']
    list_filter = ['status', 'category_id', 'created_at']

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

