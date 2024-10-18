from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse



def Home(req):
    if req.method == 'POST':
        if req.user.is_authenticated:
            addedMoney = req.POST.get('addedMoney', 0)
            try:
                total_moneySaved = int(addedMoney)
            except ValueError:
                total_moneySaved = 99
            messages.success(req, 'I should have added')
            return render(req, 'Home.html', {'firstname':'Sudip', 'total_moneySaved':total_moneySaved,})
        else:
            messages.success(req, 'I should have redirected')

            return redirect('/Login')
    else:
        user_firstname = ''
        total_moneySaved = 0.00
        messages.success(req, 'This is just exception')
        return render(req, 'Home.html', {'firstname':user_firstname, 'total_moneySaved':total_moneySaved,})
    
    