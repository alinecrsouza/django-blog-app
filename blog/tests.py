import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Post, Comment, Category, Author
from polls.models import Question, Choice

# Functions to create objects for the tests
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

def create_category(name):
    """
    Creates a category with the given `name`.
    """
    return Category.objects.create(name=name)

def create_author(name):
    """
    Creates an author with the given `name`.
    """
    return Author.objects.create(name=name)

def create_question(question_text, days):
    """
    Creates a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

#Sample tests
class HomeViewTests(TestCase):
    def test_home_view_with_a_published_post(self):
        """
        Posts with the Published status should be displayed on the
       home page.
        """
        category = create_category('Category 1')
        author = create_author('Author 1')
        create_post(category=category, author=author, name='Published Post', content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin.', status='Published')
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('blog.home'))
        self.assertQuerysetEqual(
            response.context['posts'],
            ['<Post: Published Post>']
        )

    def test_home_view_with_a_draft_post(self):
        """
        Posts with the Draft status should not be displayed on the
       home page.
        """
        category = create_category('Category 1')
        author = create_author('Author 1')
        create_post(category=category, author=author, name='Draft Post', content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin.', status='Draft')
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('blog.home'))
        self.assertContains(response, "No posts are available.")
        self.assertQuerysetEqual(response.context['posts'], [])

    def test_home_view_with_draft_post_and_published_post(self):
        """
        Even if both draft and published posts exist, only published posts
        should be displayed.
        """
        category = create_category('Category 1')
        author = create_author('Author 1')
        create_post(category=category, author=author, name='Published Post',
                    content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin.',
                    status='Published')
        create_post(category=category, author=author, name='Draft Post',
                    content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin.',
                    status='Draft')
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('blog.home'))
        self.assertQuerysetEqual(
            response.context['posts'],
            ['<Post: Published Post>']
        )

    def test_home_view_with_two_published_posts(self):
        """
        The blog home page may display multiple posts.
        """
        category = create_category('Category 1')
        author = create_author('Author 1')
        create_post(category=category, author=author, name='Published Post 1',
                    content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin.',
                    status='Published')
        create_post(category=category, author=author, name='Published Post 2',
                    content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin.',
                    status='Published')
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('blog.home'))
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
        category = create_category('Category 1')
        author = create_author('Author 1')
        draft_post = create_post(category=category, author=author, name='Draft Post', content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin.', status='Draft')
        url = reverse('blog.post', args=(draft_post.id,))
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_show_post_view_with_a_published_post(self):
        """
        The view of a post with a published status should
        display the post content.
        """
        category = create_category('Category 1')
        author = create_author('Author 1')
        published_post = create_post(category=category, author=author, name='Published Post',
                    content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin.',
                    status='Published')
        url = reverse('blog.post', args=(published_post.id,))
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(url)
        self.assertContains(response, published_post.content)