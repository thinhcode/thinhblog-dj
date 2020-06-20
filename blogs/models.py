from django.db import models
from django.contrib.auth.models import User


class Ad(models.Model):
    AD_STYLE = [
        ('1', '300x250px'),
        ('2', '468x60px'),
        ('3', '728x90px'),
        ('4', '300x600px'),
    ]
    style = models.CharField(verbose_name='Định dạng', max_length=1, choices=AD_STYLE)
    content = models.TextField(verbose_name='Code')
    publish = models.BooleanField(verbose_name='Công khai', default=True)

    def __str__(self):
        return self.get_style_display()


class Author(models.Model):
    user = models.OneToOneField(verbose_name='Người dùng', to=User, on_delete=models.CASCADE)
    display_name = models.CharField(verbose_name='Tên hiển thị', max_length=50)
    avatar = models.ImageField(verbose_name='Ảnh đại diện', upload_to='blogs/%Y/%m', blank=True)

    def __str__(self):
        return self.display_name


class Category(models.Model):
    title = models.CharField(verbose_name='Tiêu đề', max_length=200)
    slug = models.SlugField(verbose_name='Đường dẫn')

    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(verbose_name='Tiêu đề', max_length=200)
    slug = models.SlugField(verbose_name='Đường dẫn')
    description = models.CharField(verbose_name='Mô tả', max_length=300, blank=True)
    content = models.TextField(verbose_name='Nội dung', blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(verbose_name='Tiêu đề', max_length=200)
    slug = models.SlugField(verbose_name='Đường dẫn')
    author = models.ForeignKey(verbose_name='Tác giả', to=Author, on_delete=models.CASCADE, default=1)
    description = models.CharField(verbose_name='Mô tả', max_length=300, blank=True)
    content = models.TextField(verbose_name='Nội dung', blank=True)
    categories = models.ForeignKey(verbose_name='Danh mục', to=Category, on_delete=models.SET_NULL, null=True)
    tags = models.CharField(verbose_name='Thẻ', max_length=200, help_text='Cách nhau bởi dấu ,', blank=True)
    thumbnail = models.ImageField(verbose_name='Ảnh bìa', upload_to='blogs/%Y/%m', help_text='350x200px', blank=True)
    publish = models.BooleanField(verbose_name='Công khai', default=True)

    def __str__(self):
        return self.title


class Setting(models.Model):
    ads = models.ManyToManyField(verbose_name='Quảng cáo', to=Ad, blank=True)
    google_code = models.TextField(blank=True)

    def __str__(self):
        return 'Cài đặt'
