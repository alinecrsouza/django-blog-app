from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import Category, Post


def home(request):
    #return HttpResponse("Hello World")

    name = "Aline"
    #categories = {'PHP', 'Java', 'Ruby'}
    #for category in categories:
    #    Category.objects.create(name=category)

    all_categories = Category.objects.all()

    # category_python = Category.objects.get(id = 1)
    post = Post.objects.get(pk = 1)


    # post = Post()
    # post.name = "My First very Post"
    # post.content = "Content of my first Post"
    # post.status = "Published"
    # post.category = category_python
    # post.save()


    context = {
        'name': name,
        'categories': all_categories,
        'post': post,
    }

    #Category.objects.destroy(id=1)

    return render(request, 'blog/home.html', context)