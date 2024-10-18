from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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
        
 
       
    
    


def RegisterUser(req):
    if req.method == 'POST':
        firstName = req.POST['firstName']
        LastName = req.POST['LastName']
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password1']
        password2 = req.POST['password2']
        preferences = req.POST['preferences']
        if password != password2:
            messages.error(req, "Passwords do not match")
            return render(req, 'SignUp.html')
        User.objects.create_user(username=username, email=email , password=password)
        user = authenticate(username = username, password = password, first_name = firstName, last_name = LastName)
        login(req, user)
        messages.success(req, ("registration sucessfull"))
        return redirect('/')

    else:
        return render(req, 'SignUp.html' )


def Home(req):
    user_firstname = 'Sudip'
    total_moneySaved = 0.00
    return render(req, 'Home.html', {'firstname':user_firstname, 'total_moneySaved':total_moneySaved,})