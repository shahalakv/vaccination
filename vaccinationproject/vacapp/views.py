from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from vacapp.form import UserForm, NurseForm
from vacapp.models import Vaccination


# Create your views here.
def index(request):
    return render(request, 'index.html')


def user_reg(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_user = True
            user.save()
            return redirect('index')
    return render(request, 'user_reg.html', {'form': form})

def nurse_reg(request):
    form = NurseForm()
    if request.method == 'POST':
        form = NurseForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_nurse = True
            user.save()
        return redirect('index')
    return render(request, 'nurse_reg.html', {'form': form})

def nurse_page(request):
    return render(request, 'nursetemp/base.html')

def user_page(request):
    return render(request, 'usertemp/base.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print(user)
            login(request, user)
            if user.is_staff:
                return redirect('admin_page')
            elif user.is_user:
                return redirect('user_page')
            elif user.is_nurse:
                return redirect('nurse_page')
        else:
            messages.error(request, 'invalid')
    return render(request, 'login_view.html')

def logout_view(request):
    logout(request)
    return redirect('index')

