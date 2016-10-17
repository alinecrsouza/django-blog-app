from django.test import TestCase
from django.urls import reverse

from .models import Post, Comment

def create_post(category, author, name, content, status):
    """
    Creates a post with the given `category, author, name, content, status`.
    """
    return Post.objects.create(category=category, author=author, name=name, content=content, status=status)

def create_comment(post, author, content):
    """
    Creates a comment with the given `post, author, content`.
    """
    return Comment.objects.create(post=post, author=author, content=content)

class HomeViewTests(TestCase):
    def test_home_view_with_a_published_post(self):
        """
        Posts with the Published status should be displayed on the
       home page.
        """
        create_post(category=1, author=1, name='Published Post', content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin.', status='Published')
        response = self.client.get(reverse('blog:home'))
        self.assertQuerysetEqual(
            response.context['posts'],
            ['<Post: Published Post>']
        )

    def test_home_view_with_a_draft_post(self):
        """
        Posts with the Draft status should not be displayed on the
       home page.
        """
        create_post(category=1, author=1, name='Draft Post', content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin.', status='Draft')
        response = self.client.get(reverse('blog:home'))
        self.assertContains(response, "No posts are available.")
        self.assertQuerysetEqual(response.context['posts'], [])

    def test_home_view_with_draft_post_and_published_post(self):
        """
        Even if both draft and published posts exist, only published posts
        should be displayed.
        """
        create_post(category=1, author=1, name='Published Post',
                    content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin.',
                    status='Published')
        create_post(category=1, author=1, name='Draft Post',
                    content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin.',
                    status='Draft')
        response = self.client.get(reverse('blog:home'))
        self.assertQuerysetEqual(
            response.context['posts'],
            ['<Post: Published Post>']
        )

    def test_home_view_with_two_published_posts(self):
        """
        The blog home page may display multiple posts.
        """
        create_post(category=1, author=1, name='Published Post 1',
                    content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin.',
                    status='Published')
        create_post(category=1, author=1, name='Published Post 2',
                    content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin.',
                    status='Published')
        response = self.client.get(reverse('blog:home'))
        self.assertQuerysetEqual(
            response.context['posts'],
            ['<Post: Published Post 2>', '<Post: Published Post 1>']
        )

class ShowPostViewTests(TestCase):
    def test_show_post_view_with_a_draft_post(self):
        """
        The view of a post with a draft status should
        return a 404 not found.
        """
        draft_post = create_post(category=1, author=1, name='Draft Post', content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin.', status='Draft')
        url = reverse('blog:show_post', args=(draft_post.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_show_post_view_with_a_published_post(self):
        """
        The view of a post with a published status should
        display the post content.
        """
        published_post = create_post(category=1, author=1, name='Published Post',
                    content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin.',
                    status='Published')
        url = reverse('blog:show_post', args=(published_post.id,))
        response = self.client.get(url)
        self.assertContains(response, published_post.content)