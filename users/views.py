from django.shortcuts import render ,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate , login
from django.contrib import auth

def signup(request):
    
    return render(request, 'users/signup.html', {})



def user_login(request):
    if request.method == "POST":
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request , username=username , password=password)
        if user is not None :
            login(request , user)
            
    else:
        form = LoginForm()

    return render(request, 'users/user_login.html', {})


def logout(request):
    auth.logout(request)
    return redirect('users:login')
