from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
        if request.method == 'POST':
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                            password=password1)
            user.save()
            print("user created")
            messages.info(request, 'user created')
            return redirect('/')
        else:
            return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password']
        user = auth.authenticate(username=username,password=password1)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'invalid details')
            return redirect('login')
    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')