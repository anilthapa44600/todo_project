from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password')
        return render(request, 'users/login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Account created for ' + form.cleaned_data['username'])
                return redirect('login')
        context = {'form':form}
        return render(request, 'users/register.html', context )


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')