# Generated by Django 3.0.8 on 2020-07-23 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0031_auto_20200720_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, help_text='525x300px', upload_to='blogs/%Y/%m', verbose_name='Ảnh bìa'),
        ),
    ]