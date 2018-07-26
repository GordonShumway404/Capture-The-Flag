from __future__ import unicode_literals
from django.contrib import messages
from django.conf.urls.static import static
from django.shortcuts import render, redirect, HttpResponse
from .models import User
import bcrypt

def index(request):
    return render(request, 'ctf_app/index.html')

def register(request):
    #get user data from post request form
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        try:
            del request.session['user_id']
        except KeyError:
            pass
        return redirect(index)
    #if no errors in registration validation, redirect user to the welcome page & set post data
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect(level1)

def login(request):
    #get user data from post request form
    result = User.objects.validate_login(request.POST)
    #check for errors in login validation and create messages / redirect users if so
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect(index)
    #if no errors in registration validation, redirect user to the welcome page & set post data
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect(level1)

def level1(request):
    return render(request, 'ctf_app/level1.html')

def firstFlag(request):
    flag = 'CODING'

    if request.POST['test'] == flag:
        return redirect(level2)

    return render(request, 'ctf_app/level1.html')
def level2(request):
    return render(request, 'ctf_app/level2.html')

def Hell(request):
    return render(request, 'ctf_app/Hell.html')

def HellLogic(request):
    flag = 'MySQL'
    if request.POST['test2'] == flag:
        return redirect(level3)
    else:
        return render(request, 'ctf_app/Hell.html')

    return render(request, 'ctf_app/Hell.html')
def level3(request):
    return render(request, 'ctf_app/level3.html')

def level3Logic(request):
    flag = '121714281715123116'
    if request.POST['test3'] == flag:
        return redirect(level4)
    return render(request, 'ctf_app/level3.html')

def level4(request):
    return render(request, 'ctf_app/level4.html')
def level4Logic(request):
    flag = '15'
    if request.POST['test4'] == flag:
        return redirect(level5)
    return render(request, 'ctf_app/level4.html')

def level5(request):
    return render(request, 'ctf_app/level5.html')

def level5Logic(request):
    flag = 'LOVELOVELOVE'
    if request.POST['test5'] == flag:
        return redirect(youWin)
    return render(request, 'ctf_app/level5.html')

def youWin(request):
    return render(request, 'ctf_app/youWin.html')
