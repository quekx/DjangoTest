from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_description = models.TextField()
    article_link = models.URLField()
    publish_time = models.CharField(max_length=200)
    publish_time_normal = models.CharField(max_length=200)

    def __str__(self):
        return self.article_title

