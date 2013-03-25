from django.db import models

class Reference(models.Model):
    ship = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    constructionType = models.CharField(max_length=1, choices=(('n', 'New Building',),('r','Refurbishment',),), default='r')
    year = models.PositiveIntegerField(blank=True, null=True)
    description = models.CharField(max_length=10000)
    projectManager = models.CharField(max_length=200)
    projectAssistant = models.CharField(max_length=200)
    onsiteManager = models.CharField(max_length=200)
    ongoing = models.BooleanField()
    beforeDD = models.BooleanField()

    def __unicode__(self):
        if self.year:
            return self.ship + " " + str(self.year)
        else:
            return self.ship
