from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    #return HttpResponse("Hello World")

    name = "Aline"
    languages = {'Python', 'PHP', 'Java', 'Ruby'}

    context = {
        'name': name,
        'languages':languages
    }

    return render(request, 'blog/home.html', context)