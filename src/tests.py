from http import HTTPStatus
from django.test import TestCase


class RobotsTest(TestCase):
    def test_get(self):
        response = self.client.get('/robots.txt')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response['content-type'], 'text/plain')

    def test_post_disallowed(self):
        response = self.client.post('/robots.txt')
        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)


class SitemapTest(TestCase):
    def test_get(self):
        response = self.client.get('/sitemap.xml')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response['content-type'], 'application/xml')
