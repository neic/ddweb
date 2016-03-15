from django.contrib.contenttypes import fields
from django.db import models

from ddweb.apps.images.models import Image

class Article(models.Model):
    headline = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    author = models.CharField(max_length=200)

    images = fields.GenericRelation(Image)

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return self.headline
