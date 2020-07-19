from datetime import date, timedelta
from django.db.models import F, Q
from django.views.generic import base, ListView, DetailView
from django.utils.translation import gettext_lazy as _
from .models import Ad, Category, Post, Setting


def get_ad_queryset(style_id: int):
    return Ad.objects.filter(style__exact=str(style_id)).last()


def get_top_posts(capacity: int):
    past_date = date.today() - timedelta(days=30)
    return Post.objects.filter(timestamp__date__gte=past_date).order_by('-views')[:capacity]


# Generic Context Mixin
class GenCtxMixin(base.ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

        context['top_posts'] = get_top_posts(3)
        return context


class SearchView(GenCtxMixin, ListView):
    model = Post
    template_name = 'blogs/index.html'
    ordering = ['-timestamp']
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
        context['search_query'] = self.request.GET.get('q', '')
        return context


class CategoryListView(GenCtxMixin, ListView):
    model = Post
    template_name = 'blogs/index.html'
    ordering = ['-timestamp']
    paginate_by = 2

    def get_queryset(self):
        category_list = Post.objects.filter(categories__slug=self.kwargs.get('slug'))
        ordering = self.get_ordering()
        if ordering:
            category_list = category_list.order_by(*ordering)
        return category_list


class PostListView(GenCtxMixin, ListView):
    model = Post
    template_name = 'blogs/index.html'
    ordering = ['-timestamp']
    paginate_by = 2


class PostDetailView(GenCtxMixin, DetailView):
    model = Post
    template_name = 'blogs/single.html'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.views = F('views') + 1
        post.save()
        return super().get(request, *args, **kwargs)
