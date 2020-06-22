from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Ad(models.Model):
    AD_STYLE = [
        ('1', '300x250px'),
        ('2', '468x60px'),
        ('3', '728x90px'),
        ('4', '300x600px'),
    ]
    style = models.CharField(_('Định dạng'), max_length=1, choices=AD_STYLE)
    html_code = models.TextField()

    class Meta:
        verbose_name = _('Quảng cáo')
        verbose_name_plural = _('Quảng cáo')

    def __str__(self):
        return self.get_style_display()


class Author(models.Model):
    user = models.OneToOneField(to=User, verbose_name=_('Người dùng'), on_delete=models.CASCADE)
    display_name = models.CharField(_('Tên hiển thị'), max_length=50)
    avatar = models.ImageField(_('Ảnh đại diện'), upload_to='blogs/%Y/%m', blank=True)

    class Meta:
        verbose_name = _('Người dùng')
        verbose_name_plural = _('Người dùng')

    def __str__(self):
        return self.display_name


class Category(models.Model):
    title = models.CharField(_('Tiêu đề'), max_length=200)
    slug = models.SlugField(_('Đường dẫn'))

    class Meta:
        verbose_name = _('Danh mục')
        verbose_name_plural = _('Danh mục')

    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(_('Tiêu đề'), max_length=200)
    slug = models.SlugField(_('Đường dẫn'))
    description = models.CharField(_('Mô tả'), max_length=300, blank=True)
    content = models.TextField(_('Nội dung'), blank=True)

    class Meta:
        verbose_name = _('Trang')
        verbose_name_plural = _('Trang')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(_('Tiêu đề'), max_length=200)
    slug = models.SlugField(_('Đường dẫn'))
    author = models.ForeignKey(to=Author, verbose_name=_('Tác giả'), on_delete=models.CASCADE, default=1)
    description = models.CharField(_('Mô tả'), max_length=300, blank=True)
    content = models.TextField(_('Nội dung'), blank=True)
    categories = models.ForeignKey(to=Category, verbose_name=_('Danh mục'), on_delete=models.SET_NULL, null=True)
    tags = models.CharField(_('Thẻ'), max_length=200, help_text='Cách nhau bởi dấu ,', blank=True)
    thumbnail = models.ImageField(_('Ảnh bìa'), upload_to='blogs/%Y/%m', help_text='350x200px', blank=True)
    publish = models.BooleanField(_('Công khai'), default=True)

    class Meta:
        verbose_name = _('Bài viết')
        verbose_name_plural = _('Bài viết')

    def __str__(self):
        return self.title


class Setting(models.Model):
    ads = models.ManyToManyField(to=Ad, verbose_name=_('Quảng cáo'), blank=True)
    google_code = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    email = models.EmailField(max_length=50, blank=True)
    github = models.URLField(blank=True)

    class Meta:
        verbose_name = _('Cài đặt')
        verbose_name_plural = _('Cài đặt')

    def __str__(self):
        return str(_('Thiết lập'))
