from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'accounts/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return redirect('register')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            print('logged in')
            return redirect('index')
        else:
            print('not logged in')
    return render(request, 'accounts/login.html',)


def logoutpage(request):
    logout(request)
    print('logged out')
    return redirect('login')
