from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Article(models.Model):
    create_timestamp = models.DateTimeField(verbose_name='Дата создания')
    timestamp = models.DateTimeField(unique=True, verbose_name='Дата изменения')
    language = models.CharField(max_length=255, verbose_name='Язык')
    wiki = models.CharField(max_length=255, verbose_name='Wiki')
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255, verbose_name='Название')
    auxiliary_text = models.TextField(verbose_name='Вспомогательный текст')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
