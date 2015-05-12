import os
from django.contrib.contenttypes import generic
from django.db import models
from django.utils.text import slugify

from ddweb.apps.images.models import Image

def file_name(instance, filename):
    sepFilename = os.path.splitext(filename)
    newFilename = slugify(sepFilename[0]) + sepFilename[1]
    folder = slugify(instance.article.headline + '-' + str(instance.article.date))
    return '/'.join(['news', folder, newFilename])

class Article(models.Model):
    headline = models.CharField(max_length = 200)
    date = models.DateTimeField()
    description = models.TextField(blank = True)
    author = models.CharField(max_length = 200)

    images = generic.GenericRelation(Image)

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return self.headline
