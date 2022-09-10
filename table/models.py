from django.db import models
from django.contrib.auth.models import User
class job (models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    time = models.IntegerField()
    owner = models.CharField(max_length=200)
    detail = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    taken_by = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)

class boss (models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    token = models.CharField(unique=True , max_length=200)

class employee (models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    boss = models.ForeignKey(boss , on_delete=models.CASCADE)
    token = models.CharField(unique=True , max_length=200)

