<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

user={}
temp = loader.get_template('firstapp/index.html')
def num(request):
    return HttpResponse("<h1>+91 8825792941</h1>")
def inx(request):
    return HttpResponse((loader.get_template('firstapp/fist.html')).render({},request))
def login(request):
    global user
    if request.method=="POST":
        print("values are",[x for x in request.POST])
        username = request.POST['email']
        password = request.POST['password'] 
        user[username] = password
        print(user)
        return  HttpResponse(('<h1>Welcome {} ..!</h1>').format(username.upper()))

    else:
        return  HttpResponse(temp.render({},request))
=======
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

user={}
temp = loader.get_template('firstapp/index.html')
def num(request):
    return HttpResponse("<h1>+91 8825792941</h1>")
def inx(request):
    return HttpResponse((loader.get_template('firstapp/fist.html')).render({},request))
def login(request):
    global user
    if request.method=="POST":
        print("values are",[x for x in request.POST])
        username = request.POST['name']
        password = request.POST['pass'] 
        user[username] = password
        print(user)
        return  HttpResponse(('<h1>Welcome {} ..!</h1>').format(username.upper()))

    else:
        return  HttpResponse(temp.render({},request))
>>>>>>> 58c2781f6e12362f31ad786b6796c2773cf0ab3e
