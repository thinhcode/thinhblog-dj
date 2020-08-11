from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import RedirectView
from blogs import sitemaps
from . import views

sitemaps = {
    'categories': sitemaps.CategorySitemap(),
    'posts': sitemaps.PostSitemap(),
    'pages': sitemaps.PageSitemap(),
    'static': sitemaps.StaticViewSitemap(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('favicon.ico/', RedirectView.as_view(url='/static/blogs/img/favicon.ico')),
    path('robots.txt/', views.RobotsView.as_view()),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', include('blogs.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
