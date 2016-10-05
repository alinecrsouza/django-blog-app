from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import Category


def home(request):
    #return HttpResponse("Hello World")

    name = "Aline"
    categories = {'PHP', 'Java', 'Ruby'}
    for category in categories:
        Category.objects.create(name=category)

    all_categories = Category.objects.all()

    context = {
        'name': name,
        'categories': all_categories
    }

    #Category.objects.destroy(id=1)

    return render(request, 'blog/home.html', context)