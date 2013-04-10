import os
from django.db import models
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

def file_name(instance, filename):
    sepFilename = os.path.splitext(filename)
    newFilename = slugify(sepFilename[0]) + sepFilename[1]
    folder = slugify(instance.reference.ship + '-' + str(instance.reference.year))
    return '/'.join([folder, newFilename])

class Reference(models.Model):
    CBH = 'CBH'
    TIK = 'TIK'
    HG = 'HG'
    CBHTIK = 'CBT'
    TIKHG = 'TIH'
    MANAGER_CHOICES = (
        (CBH, 'Claus B. Hansen'),
        (TIK, 'Tina Kjeldgaard'),
        (HG, 'Henrik Graahede'),
        (CBHTIK, 'Claus B. Hansen / Tina Kjeldaard'),
        (TIKHG, 'Tina Kjeldgaard / Henrik Graahede')
    )

    ship = models.CharField(max_length = 200)
    owner = models.CharField(max_length = 200)
    place = models.CharField(max_length = 200)
    constructionType = models.CharField(max_length = 1,
                                        choices = (('n', 'New Building'), ('r','Refurbishment')),
                                        default = 'r')
    year = models.PositiveIntegerField(blank = True, null=True)
    description = models.TextField(blank = True)
    projectManager = models.CharField(max_length = 3,
                                      choices = MANAGER_CHOICES,
                                      blank = True)
    projectAssistant = models.CharField(max_length = 3,
                                        choices = MANAGER_CHOICES,
                                        blank = True)
    onsiteManager = models.CharField(max_length = 3,
                                     choices = MANAGER_CHOICES,
                                     blank = True)
    ongoing = models.BooleanField()
    beforeDD = models.BooleanField()

    def __unicode__(self):
        if self.year:
            return self.ship + " " + str(self.year)
        else:
            return self.ship

class ReferenceImage(models.Model):
    reference = models.ForeignKey(Reference, related_name = 'images')
    image = models.ImageField(upload_to = file_name)
    thumbnail = ImageSpecField(image_field = 'image',
                               processors = [ResizeToFill(160, 120)],
                               format = 'JPEG',
                               options = {'quality': 60},)
