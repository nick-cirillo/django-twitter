from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Tweet

def main_view(request):
    return render(request, 'main.html' )

def splash_view(request):
    return render(request, 'splash.html')

def login_view(request):
    username, password = request.POST['username'], request.POST['password']

    user = authenticate(username=username, password=password)
    
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return redirect('/splash?error=LoginError')

def signup_view(request):
    user = User.objects.create_user(
        username=request.POST['username'],
        password=request.POST['password'],
        email=request.POST['email'],
    )
    login(request, user)
    return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/splash')

def tweet_list(request):
    tweets = Tweet.objects.order_by('created_at')
    return render(request, 'templates/main.html', {'tweets': tweets})