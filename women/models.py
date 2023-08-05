from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=100, verbose_name='Имя')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='persons', blank=True, verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_publish = models.BooleanField(default=True, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return f"\nЗаголовок: {self.title}\n" \
               f"Опубликовано: {self.is_publish}\n"

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Женщины'
        verbose_name_plural = 'Женщины'
        ordering = ['-time_create']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']