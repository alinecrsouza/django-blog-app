from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.urls import reverse
from .forms import CommentForm



from blog.models import Category, Post, Comment

def home(request):
    all_categories = Category.objects.all()
    posts_list = Post.objects.filter(status='Published').order_by('-created_at')
    paginator = Paginator(posts_list, 3)  # Show 3 posts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    context = {
        'categories': all_categories,
        'posts': posts,
    }

    return render(request, 'blog/home.html', context)

def show_posts_by_category(request, category_id):
    all_categories = Category.objects.all()
    category = Category.objects.get(pk = category_id)
    posts = Post.objects.filter(category = category, status = 'Published')
    context ={
        'posts': posts,
        'categories': all_categories,
        'category': category,
    }
    return render(request, 'blog/home.html', context)

def show_post(request, post_id):
    all_categories = Category.objects.all()
    post = Post.objects.get(pk = post_id)
    comments = Comment.objects.filter(post = post)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # optional HttpResponseRedirect here
            return HttpResponseRedirect(reverse('blog.post', args=(post.id,)))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CommentForm()

    context ={
        'comments': comments,
        'categories': all_categories,
        'post': post,
        'form': form,
    }
    return render(request, 'blog/post.html', context)

# def get_comment(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = CommentForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('blog/post.html')
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = CommentForm()
#
#     return render(request, 'blog/post.html', {'form': form})