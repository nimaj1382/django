import os
from dotenv import load_dotenv
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse as hr
from .models import kar
from django.core.paginator import Paginator as pg

def index(req , page = 1):
    temp = loader.get_template('table/table.html')
    p = pg(range(len(kar.objects.all())) , 20)
    karlist = kar.objects.all()
    context = {
        'kar' : karlist ,
        'p' : p ,
        'page' : page ,
    }
    return hr(temp.render(context , req))