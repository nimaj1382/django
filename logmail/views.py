from django.shortcuts import render
from django.http import HttpResponse as hr
from django.core.mail import send_mail

def index(req):
    send_mail(
        'Title',
        'A message about login',
        'me@mysite.com',
        ['nimaj1382@gmail.com']
    )
    return hr("Email sent successfully")