from django.shortcuts import render
from django.http import HttpResponse as hr
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import render



def index (req):
    if 'uname' not in req.session :
        if 'uname' not in req.POST:
            temp = loader.get_template('login/login.html')
            context = {
                'err' : '' ,
            }
            return hr(temp.render(context , req))
        else :
            u = User()
            u.username = req.POST['uname']
            u.set_password(req.POST['pass'])
            u.save()
            req.session['uname'] = u.username
            return hr('You are logged in . {} !'.format(u.username))
    else :
        return hr("Wellcome back , {} !".format(req.session['uname']))
def logout (req):
    req.session.pop('uname')
    return hr("Logged out succusfully")