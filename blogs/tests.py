from django.test import TestCase
from .models import Ad, Category, Page


class AdTest(TestCase):
    def setUp(self):
        Ad.objects.create(
            style='1'
        )

    def test_get_style_display(self):
        ad = Ad.objects.get(pk=1)
        self.assertEqual(ad.style, '1')
        self.assertEqual(str(ad), '300x250px')


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
