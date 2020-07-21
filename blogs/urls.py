from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('search/', views.SearchView.as_view(), name='search'),
    path('blogs/<slug:slug>/', views.PostDetailView.as_view(), name='post'),
    path('categories/<slug:slug>/', views.CategoryListView.as_view(), name='category'),
    path('<slug:slug>/', views.PageDetailView.as_view(), name='page'),
    path('', views.PostListView.as_view(), name='index'),
]
