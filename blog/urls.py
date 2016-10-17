from django.conf.urls import url, include
from django.views.generic import RedirectView

from blog import views

urlpatterns = [
    url(r'^$', views.home, name='blog.home'),
    url(r'^about/$', views.about, name='blog.about'),
    url(r'^contact/$', views.contact, name='blog.contact'),
    url(r'category/(?P<category_id>\d+)/$', views.show_posts_by_category, name='blog.posts_by_category'),
    url(r'author/(?P<author_id>\d+)/$', views.show_posts_by_author, name='blog.posts_by_author'),
    url(r'post/(?P<post_id>\d+)/$', views.show_post, name='blog.post'),
    url(r'^search/', include('haystack.urls')),
    # The index and Detail views of the Poll App are not used, so the urls are redirected to /blog/ (home)
    url(r'^polls/$', RedirectView.as_view(url='/blog/')),
    url(r'^polls/(\d+)/$', RedirectView.as_view(url='/blog/')),
    url(r'^polls/', include('polls.urls')),
]
