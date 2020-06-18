from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(verbose_name='Người dùng', to=User, on_delete=models.CASCADE)
    disName = models.CharField(verbose_name='Tên hiển thị', max_length=50)
    avatar = models.ImageField(verbose_name='Ảnh đại diện', upload_to='blogs/%Y/%m', blank=True)

    def __str__(self):
        return self.disName

class Category(models.Model):
    title = models.CharField(verbose_name='Tiêu đề', max_length=200)
    slug = models.SlugField(verbose_name='Đường dẫn')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(verbose_name='Tiêu đề', max_length=200)
    slug = models.SlugField(verbose_name='Đường dẫn')
    author = models.ForeignKey(verbose_name='Tác giả', to=Author, on_delete=models.CASCADE, default=1)
    desc = models.TextField(verbose_name='Mô tả', blank=True)
    cats = models.ForeignKey(verbose_name='Danh mục', to=Category, on_delete=models.SET_NULL, null=True)
    tags = models.CharField(verbose_name='Thẻ', max_length=200, help_text='Cách nhau bởi dấu ,', blank=True)
    thumbnail = models.ImageField(verbose_name='Ảnh bìa', upload_to='blogs/%Y/%m', help_text='350x200px', blank=True)

    def __str__(self):
        return self.title
