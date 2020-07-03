from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView, View
from django.utils.translation import gettext_lazy as _
from .models import Category, Post, Setting


def get_general_context():
    context = dict()
    context['categories'] = Category.objects.order_by('title')

    setting_obj = Setting.objects
    if setting_obj.exists():
        context['facebook'] = setting_obj.values().last().get('facebook')
        context['email'] = setting_obj.values().last().get('email')
        context['github'] = setting_obj.values().last().get('github')
    
    return context


class SearchView(ListView):
    model = Post
    template_name = 'blogs/index.html'
    ordering = ['-timestamp']
    page_kwarg = _('trang')
    paginate_by = 2

    def get_queryset(self):
        search_query = self.request.GET.get('q', '')
        search_list = Post.objects.filter(
            Q(title__icontains=search_query) | Q(tags__icontains=search_query) | Q(content__icontains=search_query)
        )
        ordering = self.get_ordering()
        if ordering:
            search_list = search_list.order_by(*ordering)
        return search_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_general_context())
        context['search_query'] = self.request.GET.get('q', '')
        return context


class PostListView(ListView):
    model = Post
    template_name = 'blogs/index.html'
    ordering = ['-timestamp']
    page_kwarg = _('trang')
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_general_context())
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogs/single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_general_context())
        return context
