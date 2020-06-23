# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blogs/index.html'
    ordering = ['-timestamp']
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogs/single.html'
