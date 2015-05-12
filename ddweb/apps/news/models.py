from django.contrib.contenttypes import generic
from django.db import models

from ddweb.apps.images.models import Image

class Article(models.Model):
    headline = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    author = models.CharField(max_length=200)

    images = generic.GenericRelation(Image)

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return self.headline
