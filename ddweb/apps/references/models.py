import os
from django.contrib.contenttypes import generic
from django.db import models
from django.utils.text import slugify
from ddweb.apps.images.models import Image

def file_name(instance, filename):
    sepFilename = os.path.splitext(filename)
    newFilename = slugify(sepFilename[0]) + sepFilename[1]
    folder = slugify(instance.reference.ship + '-' + str(instance.reference.year))
    return '/'.join(['ref', folder, newFilename])

class Reference(models.Model):
    ship = models.CharField(max_length = 200)
    owner = models.CharField(max_length = 200)
    place = models.CharField(max_length = 200)
    constructionType = models.CharField(max_length = 1,
                                        choices = (('n', 'New Building'), ('r','Refurbishment')),
                                        default = 'r')
    year = models.PositiveIntegerField(blank = True, null=True)
    description = models.TextField(blank = True)
    ongoing = models.BooleanField(default = True)
    beforeDD = models.BooleanField(default = False)

    images = generic.GenericRelation(Image)

    class Meta:
        ordering = ['-year', '-id']

    def __unicode__(self):
        if self.year:
            return self.ship + " " + str(self.year)
        else:
            return self.ship
