from django.contrib.contenttypes import fields
from django.db import models

from ddweb.apps.images.models import Image

class Reference(models.Model):
    ship = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    constructionType = models.CharField(
        max_length=1,
        choices=(('n', 'New Building'), ('r', 'Refurbishment')),
        default='r')
    year = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    ongoing = models.BooleanField(default=True)
    beforeDD = models.BooleanField(default=False)

    images = fields.GenericRelation(Image)

    class Meta:
        ordering = ['-year', '-id']

    def __unicode__(self):
        if self.year:
            return self.ship + " " + str(self.year)
        else:
            return self.ship
