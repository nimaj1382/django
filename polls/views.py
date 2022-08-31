from django.shortcuts import render
from django.http import HttpResponse as hr
from .models import question
from django.template import loader


def index(request):
    que = question.objects.all()[question_id]
    return hr(que.question_text)