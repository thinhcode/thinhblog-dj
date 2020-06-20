from django.contrib import admin
from .models import Ad, Author, Category, Page, Post, Setting

admin.site.register(Ad)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Post)
admin.site.register(Setting)
