from django.db import models

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

    ship = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    constructionType = models.CharField(max_length=1,
                                        choices=(('n', 'New Building',),('r','Refurbishment',),),
                                        default='r')
    year = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    projectManager = models.CharField(max_length=3,
                                      choices=MANAGER_CHOICES,
                                      blank=True)
    projectAssistant = models.CharField(max_length=3,
                                      choices=MANAGER_CHOICES,
                                      blank=True)
    onsiteManager = models.CharField(max_length=3,
                                      choices=MANAGER_CHOICES,
                                      blank=True)
    ongoing = models.BooleanField()
    beforeDD = models.BooleanField()

    def __unicode__(self):
        if self.year:
            return self.ship + " " + str(self.year)
        else:
            return self.ship
