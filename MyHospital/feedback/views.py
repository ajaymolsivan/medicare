from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import FeedbackForm


# Create your views here.


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
def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('/')
    else:
        f = FeedbackForm()
    return render(request, 'feedback.html', {'form': f})
def aboutus(request):
    return render(request, 'aboutus.html')
def contact(request):
    return render(request, 'contact.html')
