from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def register(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:

            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username Taken Already')
                return redirect('register')

            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email taken already')
                return redirect('register')

            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save();
                messages.info(request, 'User Created')

        else:
            messages.info(request, 'password not matching')
            return redirect ('register')

    else:
        return render(request, 'register.html')