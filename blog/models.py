from django.db import models
from django.forms import ModelForm
from django.core import urlresolvers

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category)
    author = models.ForeignKey(Author, default = 1)
    name = models.CharField(max_length=255)
    content = models.TextField()
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default = 'Draft' )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

# class CommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['post', 'author', 'content']