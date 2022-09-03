from django.shortcuts import render
from django.http import HttpResponse as hr
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import render
from django.contrib.auth import authenticate , login


def index (req):
    if 'uname' not in req.session :
        if 'uname' not in req.POST:
            temp = loader.get_template('login/login.html')
            context = {
                'err' : '' ,
            }
            return hr(temp.render(context , req))
        else :
            un = req.POST['uname']
            pw = req.POST['pass']
            user = authenticate(req , username = un , password = pw)
            if user is not None :
                login(req , user)
                return hr("Logged in successfully. {}".format(req.user.username))
            else :
                return hr("Username or Password invalid")
    else :
        return hr("Wellcome back , {} !".format(req.session['uname']))
def logout (req):
    req.session.pop('uname')
    return hr("Logged out succusfully")