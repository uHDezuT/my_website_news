from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(
        'Заголовок новости',
        max_length=100,
        help_text='Введите заголовок новости'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='news',
        blank=True,
        null=True,
        verbose_name='Группа',
        help_text='Группа, к которой будет относиться новость'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='news',
        verbose_name='Автор'
    )
    body = models.TextField(
        'Текст новости',
        max_length=3000,
        help_text='Введите текст новости'
    )
    image = models.ImageField(
        'Изображение',
        upload_to='news_image/',
        help_text='Добавьте изображение',
        blank=True
    )
    publish_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.title[:20]
