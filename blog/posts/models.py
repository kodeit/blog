from django.conf import settings
from django.db import models

from posts.utils import *


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    visit_count = models.BigIntegerField(default='0')
    slug = models.SlugField(max_length=40, unique=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,)
    category = models.ManyToManyField(Category)

    def get_category(self):
        return "\n".join([cat.name for cat in self.category.all()])

    class Meta:
        ordering = ["-created"]
