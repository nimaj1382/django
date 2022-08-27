from django.db import models

class question(models.Model):
    question_text = models.CharField(max_length=200)

class choice(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

