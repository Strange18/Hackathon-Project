from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import Registerform, loginForm
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login, logout
import requests,os
# from django.core.mail import send_mail
# from django.conf import settings



# for signup

def signup(request):
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = Registerform()
    return render(request, 'signup.html', {'form': form})

# for login


def login_user(request):
    form = loginForm()
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Either Username or Password is Incorrect'
                return render(request, 'login.html', {'msg': message, 'form': form})
    return render(request, 'login.html', {'form': form})


# for logout
def logout_user(request):
    logout(request)
    return redirect('home')


# def send_email():
#     subject = 'Welcome to our Website '
#     message = f'Hi! {username} We will Help you To make our Country Better Day By Day '
#     from_email = settings.EMAIL_HOST_USER
#     recipient_list = [request.email]
#     send_mail(subject, message, from_email,
#               recipient_list, fail_silently=False)
