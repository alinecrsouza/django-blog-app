from django.contrib import admin

from blog.models import Category, Post, Author, Comment

# Post Admin Area Configuration
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'category')
    search_fields = ['name', 'content']
    list_filter = ['status', 'category', 'created_at']

# Comment Admin Area Configuration
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'post')
    search_fields = ['author', 'content']
    list_filter = ['post', 'created_at']

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

