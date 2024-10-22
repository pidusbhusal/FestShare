from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserAccount
from .models import Event


# we havn't been able to fetch the data from database yet
def Home(req):
    if req.method == 'POST':
        if req.user.is_authenticated:
            user_account = UserAccount
            firstName = UserAccount.objects.filter(user = req.user ).first().firstName
            addedMoney = req.POST.get('addedMoney', 0)
            try:
                total_moneySaved = int(addedMoney)
            except ValueError:
                total_moneySaved = 99
            messages.success(req, 'I should have added')
            return render(req, 'Home.html', {'firstname':firstName, 'total_moneySaved':total_moneySaved,})
        else:
            messages.success(req, 'I should have redirected')

            return redirect('/Login')
    else:
        if req.user.is_authenticated:
            user = UserAccount.objects.filter(user = req.user ).first()
            firstName = user.firstName
            total_moneySaved = user.NetWorth
            return render(req, 'Home.html', {'firstname':firstName, 'total_moneySaved':total_moneySaved,})
        firstName = ''
        total_moneySaved = 0.00
        return render(req, 'Home.html', {'firstname':firstName, 'total_moneySaved':total_moneySaved,})
    
    