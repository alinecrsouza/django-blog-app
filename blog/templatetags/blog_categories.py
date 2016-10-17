from django import template
from blog.models import Category

register = template.Library()

# render all categories in categories.html
@register.inclusion_tag('blog/categories.html')
def get_categories(self=None):
        return {
                'categories': Category.objects.all(),
        }