from django.contrib.auth.models import User
from django.test import TestCase
from .models import Ad, Author, Category, Page, Post, Setting


class AdTest(TestCase):
    def setUp(self):
        Ad.objects.create(
            style='1'
        )

    def test_get_style_display(self):
        ad = Ad.objects.get(pk=1)
        self.assertEqual(ad.style, '1')
        self.assertEqual(str(ad), '300x250px')


class AuthorTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username='user'
        )
        Author.objects.create(
            user=user,
            display_name='test author'
        )

    def test_get_display_name(self):
        author = Author.objects.get(pk=1)
        self.assertEqual(str(author), 'test author')


class CategoryTest(TestCase):
    def setUp(self):
        Category.objects.create(
            title='test category',
            slug='test-category',
            color='1'
        )

    def test_get_absolute_url(self):
        category = Category.objects.get(pk=1)
        self.assertEqual(category.get_absolute_url(), f'/categories/{category.slug}/')

    def test_get_color(self):
        category = Category.objects.get(pk=1)
        self.assertEqual(category.color, '1')
        self.assertEqual(category.get_color(), 'primary')

    def test_get_title(self):
        category = Category.objects.get(pk=1)
        self.assertEqual(str(category), 'test category')


class PageTest(TestCase):
    def setUp(self):
        Page.objects.create(
            title='test page',
            slug='test-page'
        )

    def test_get_absolute_url(self):
        page = Page.objects.get(pk=1)
        self.assertEqual(page.get_absolute_url(), f'/{page.slug}/')

    def test_get_title(self):
        page = Page.objects.get(pk=1)
        self.assertEqual(str(page), 'test page')


class PostTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username='user'
        )
        author = Author.objects.create(
            user=user,
            display_name='test'
        )
        Post.objects.create(
            title='test post',
            slug='test-post',
            author=author,
            tags='test, post'
        )

    def test_get_absolute_url(self):
        post = Post.objects.get(pk=1)
        self.assertEqual(post.get_absolute_url(), f'/blogs/{post.slug}/')

    def test_tags_to_list(self):
        post = Post.objects.get(pk=1)
        self.assertEqual(post.tags_to_list(), ['test', 'post'])

    def test_get_title(self):
        post = Post.objects.get(pk=1)
        self.assertEqual(str(post), 'test post')


class SettingTest(TestCase):
    def setUp(self):
        Setting.objects.create()
        Setting.objects.create()

    def test_get_title_is_same(self):
        setting1 = Setting.objects.get(pk=1)
        setting2 = Setting.objects.get(pk=2)
        self.assertEqual(str(setting1), 'Thiết lập')
        self.assertEqual(str(setting2), 'Thiết lập')
