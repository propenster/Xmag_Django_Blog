from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# class Category(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name    

CATEGORY_LIST = ((1,'JavaScript'), (2, 'jQuery'), (3,'Web Design'), (4, 'CSS'))

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category = models.CharField(max_length=255, choices=CATEGORY_LIST)
    published = models.DateField()

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])


