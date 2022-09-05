from django.shortcuts import render
from django.http import HttpResponse as hr
from django.core.mail import EmailMessage as em
import random
import string
from django.contrib.auth.models import User
from django.template.loader import get_template

ltrs = string.ascii_letters + string.digits
def randstr ():
    return (''.join(random.choice(ltrs) for i in range(16)))

def index(req):
    if 'email' not in req.POST:
        temp = get_template('logmail/mail.html')
        return hr(temp.render({} , req))
    else :
        u = User.objects.filter(email = req.POST['email'])
        if len(u):
            u = u[0]
            if u.last_name == '' :
                while True:
                    s = randstr()
                    if not len(User.objects.filter(last_name = s)):
                        u.last_name = randstr()
                        u.save()
                        break
            return hr("<a href='{}'>Login</a>".format(u.last_name))
        else :
            u = User(email = req.POST['email'])
            while True:
                s = randstr()
                if not len(User.objects.filter(last_name=s)):
                    u.last_name = randstr()
                    u.save()
                    break
            return hr("<a href='{}'>Login</a>".format(u.last_name))

def login(req , token):
    u = User.objects.filter(last_name = token)[0]
    if u.username == '':
        temp = get_template('logmail/form.html')
        return hr(temp.render({} , req))