from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.http import HttpResponse


def sayHello(req):
    return HttpResponse('Hello')
# Create your views here.


def Login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        # checking if all the field are filled
        if not username or not password:
            messages.error(req, 'Username and password are required')
            return render(req, 'Login.html')

        # try authenticating user
        user = authenticate(req, username = username , password = password)

        # if user exist 
        if user is not None:
            login(req, user)
            messages.success(req, 'Log in Sucessfull')
            return redirect('/Home')
        else:
            # Failed
            messages.error(req, ("Invalid Username or password"))
            return render(req, 'Login.html', {'message':'invalid credentials'})
    
    return render(req,'Login.html', {'message':''}) # this will work if it is not POST 
             

def LogOut(req):
    logout(req)
    messages.success(req, 'Logged Out Sucessfully ')
    return redirect('/')
        
 
       
    
    


def RegisterUser(req):
    if req.method == 'POST':

        # get user info from the post   
        firstName = req.POST['firstName']
        LastName = req.POST['LastName']
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password1']
        password2 = req.POST['password2']
        preferences = req.POST['preferences']

       
        
        # Confirm Password
        if password != password2:
            messages.error(req, "Passwords do not match")
            return render(req, 'SignUp.html')

        # validating password
        try:
            validate_password(password)
        except ValidationError as e:
            for error in e:
                messages.error(req, error)
            return render(req, 'SignUp.html')

        # Checking if the user already exist
        if User.objects.filter(username = username).exists():
            messages.error(req, 'That User Already Exist')
            return render(req, 'SignUp.html')

        if User.objects.filter(email = email).exists():
            messages.error(req, 'That email is already in user')
            return render(req, 'SignUp.html')

        # creating user object for authentication
        user = User.objects.create_user(username=username, email=email , password=password)  #creating object of this user
        user.first_name = firstName
        user.last_name = LastName
        user.save()

        #auto logging in the user 
        login(req, user)

        # filling userdata in models for app user
        user_account = UserAccount(user = req.user, firstName = firstName, lastname = LastName, email = email, preferences = preferences)
        user_account.save()

        # verify the registration
        messages.success(req, ("registration sucessfull"))
        return redirect('/')

    else:
        return render(req, 'SignUp.html' )


