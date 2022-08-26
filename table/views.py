from django.shortcuts import render
from django.http import HttpResponse as hr

view_file = open('./view.html')
res = view_file.read()

def index(req):
    return hr(res)
