from django.shortcuts import render
from django.http import HttpResponse as hr
from django.core.mail import EmailMessage as em
import random
import string
from django.contrib.auth.models import User
from django.template.loader import get_template
from .models import tkn

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
            if not hasattr(u , 'tkn') :
                while True:
                    s = randstr()
                    if not len(tkn.objects.filter(tok = s)):
                        t = tkn(user = u , tok = randstr())
                        t.save()
                        break
            return hr("<a href='{}'>Login</a>".format(u.tkn.tok))
        else :
            u = User(email = req.POST['email'])
            u.save()
            while True:
                s = randstr()
                if not len(User.objects.filter(last_name=s)):
                    t = tkn(user = u , tok = randstr())
                    t.save()
                    break
            return hr("<a href='{}'>Login</a>".format(u.tkn.tok))

def login(req , token):
    u = tkn.objects.filter(last_name = token)[0].user
    if u.username == '':
        temp = get_template('logmail/form.html')
        return hr(temp.render({} , req))
    else :
        return hr('wellcome {}'.format(u.username))