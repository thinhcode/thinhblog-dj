from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('search/', views.SearchView.as_view(), name='search'),
    path('blogs/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('', views.PostListView.as_view(), name='post-list'),
]
