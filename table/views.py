import os
from dotenv import load_dotenv
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import job , boss , employee
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.contrib.auth import login , logout as lo , authenticate
from django.contrib.auth.decorators import login_required , permission_required
from django.contrib.auth.models import User , Permission

def red (req):
    res = redirect('1/')
    return res
def index(req , page = 1):
    temp = loader.get_template('table/table.html')
    page = Paginator(job.objects.all() , 20)
    page_object = page.get_page(page).object_list
    context = {
        'page_object' : page_object ,
    }
    return HttpResponse(temp.render(context , req))
@login_required()
def detail(req , id):
    temp = loader.get_template('table/detail.html')
    context = {
        'job' : job.objects.filter(id = id)[0]
    }
    return HttpResponse(temp.render(context , req))

def addjob(req):
    pass

def logout(req):
    lo(req)
    return HttpResponse('Logged out successfully')
def login(req):
    pass