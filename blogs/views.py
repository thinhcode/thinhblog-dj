# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Post, Setting


def get_general_context():
    context = dict()
    context['categories'] = Category.objects.order_by('title')
    context['facebook'] = Setting.objects.values('facebook')[0].get('facebook')
    context['email'] = Setting.objects.values('email')[0].get('email')
    context['github'] = Setting.objects.values('github')[0].get('github')
    return context


class PostListView(ListView):
    model = Post
    template_name = 'blogs/index.html'
    ordering = ['-timestamp']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_general_context())
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogs/single.html'
