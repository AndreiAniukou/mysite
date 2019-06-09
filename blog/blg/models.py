from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)#db_index для быстрого поиска
    slug = models.SlugField(max_length=150, unique=True)#разрешает использовать все символы и уникальные индификатры
    body = models.TextField(blank=True, db_index=True)#blanc чтобы поле было пустым разрешить
    date_pub = models.DateTimeField(auto_now_add=True)#auto_now ставит дату при сохранении в бд


    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug}) #генерирует ссылку


    def __str__(self):
        return '{}'.format(self.title)#для вывода