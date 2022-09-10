from django.db import models
from django.contrib.auth.models import User
class tkn (models.Model):
    user = models.OneToOneField(User , models.CASCADE)
    tok = models.CharField(max_length=200)
