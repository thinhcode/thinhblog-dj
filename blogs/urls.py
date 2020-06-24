from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('blogs/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('', views.PostListView.as_view(), name='post-list'),
]
