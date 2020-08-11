from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Category, Page, Post


class CategorySitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return Category.objects.all()


class PostSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return Post.objects.filter(publish=True)

    @staticmethod
    def lastmod(item):
        return item.timestamp


class PageSitemap(Sitemap):
    priority = 0.3
    changefreq = 'yearly'

    def items(self):
        return Page.objects.all()


class StaticViewSitemap(Sitemap):
    priority = 0.3
    changefreq = 'weekly'

    def items(self):
        return ['blogs:index']

    def location(self, item):
        return reverse(item)
