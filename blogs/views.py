from django.shortcuts import render
from django.db.models import F, Q
from django.views.generic import ListView, DetailView, View
from django.utils.translation import gettext_lazy as _
from .models import Ad, Category, Post, Setting


def get_ad_queryset(id: int):
    return Ad.objects.filter(style__exact=str(id)).last()

def get_general_context():
    context = dict()
    context['categories'] = Category.objects.all()
    context['ad_300x250'] = get_ad_queryset(1)
    context['ad_468x60'] = get_ad_queryset(2)
    context['ad_728x90'] = get_ad_queryset(3)
    context['ad_300x600'] = get_ad_queryset(4)

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


class CategoryListView(ListView):
    model = Post
    template_name = 'blogs/index.html'
    ordering = ['-timestamp']
    page_kwarg = _('trang')
    paginate_by = 2

    def get_queryset(self):
        category_list = Post.objects.filter(categories__slug=self.kwargs.get('slug'))
        ordering = self.get_ordering()
        if ordering:
            category_list = category_list.order_by(*ordering)
        return category_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_general_context())
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

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.views = F('views') + 1
        post.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_general_context())
        return context
