from django.db import models

class kar (models.Model):
    name = models.CharField(max_length=200)
    arzesh = models.IntegerField()
    zaman = models.IntegerField()
    saheb = models.CharField(max_length=200)
    tozih = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')