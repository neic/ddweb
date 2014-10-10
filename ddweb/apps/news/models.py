import os
from django.db import models
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

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

    def __unicode__(self):
        return self.headline

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, related_name = 'images')
    image = models.ImageField(upload_to = file_name)
    thumbnail = ImageSpecField(source = 'image',
                               processors = [ResizeToFill(160, 120)],
                               format = 'JPEG',
                               options = {'quality': 60},)
