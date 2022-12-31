from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def logIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Successfully loged in")
            return render(request, 'index.html', {'user': user})
        else:
            messages.info(request, 'Wrong Credentials..')
            print("Wrong...")
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def logOut(request):
    logout(request)
    return render(request, 'index.html')