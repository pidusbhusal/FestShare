from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse


def sayHello(req):
    return HttpResponse('Hello')
# Create your views here.


def Login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username = username , password = password)
        if user is not None:
            login(req, user)
            messages.success(req, 'Log in Sucessfull')

            return redirect('/')
        else:
            messages.success(req, ("there was an error Logging in"))
            return render(req, 'Login.html', {'message':'invalid credentials'})
    else : 
        return render(req,'Login.html', {'message':''})
             

def LogOut(req):
    logout(req)
    messages.success(req, 'Logged Out Sucessfully ')
    return redirect('/')
        
 
       
    
    


def SignUp(req):
    return render(req, 'SignUp.html' )

def CreateNewUser(req):
    name = req.POST['name']
    email = req.POST['email']
    password = req.POST['password']
    preferences = req.POST['preferences']
    return render(req, 'GreetUser.html', {'name':name, "email":email, "preferences":preferences , "password":password})

def Home(req):
    return render(req, 'Home.html')