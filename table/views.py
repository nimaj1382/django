import os
from dotenv import load_dotenv
from django.shortcuts import render
from django.http import HttpResponse as hr

load_dotenv()

view_file = open(os.getenv('path_to_html'))
res = view_file.read()

def index(req):
    return hr(res)
