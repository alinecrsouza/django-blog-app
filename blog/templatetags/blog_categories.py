from django import template
from blog.models import Category

register = template.Library()

@register.inclusion_tag('blog/categories.html')
def get_categories(self=None):
        return {
                'categories': Category.objects.all(),
        }