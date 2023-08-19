from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def register(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email has been taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username has been taken')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save();
                messages.info(request, 'User has been created')
        else:
            messages.info(request, 'password does not match')
        return redirect('register')
    
    else:
        return render(request, 'register.html')