import os
from dotenv import load_dotenv
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse as hr
from .models import kar
from django.core.paginator import Paginator as pg
from django.shortcuts import redirect
def red (req):
    res = redirect('1/')
    return res
def index(req , page = 1):
    temp = loader.get_template('table/table.html')
    p = pg(kar.objects.all() , 20)
    page_object = p.get_page(page).object_list
    context = {
        'page_object' : page_object ,
    }
    return hr(temp.render(context , req))
def detail(req , id):
    temp = loader.get_template('table/detail.html')
    context = {
        'kar' : kar.objects.all()[id-1] ,
    }
    return hr(temp.render(context , req))