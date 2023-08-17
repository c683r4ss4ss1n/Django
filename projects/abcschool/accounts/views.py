from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.

def register(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(email = email).exists():
                print('Username has been taken')
            elif User.objects.filter(user_name=user_name).exists():
                print('email has been taken')
            else:
                user = User.objects.create_user(username=user_name, password=password, confirm_password=confirm_password, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('User has been created')
        else:
            print('password does not match')
        return redirect('/accounts/register')
    
    else:
        return render(request, 'register.html')