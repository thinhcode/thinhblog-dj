from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('blogs/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
]
