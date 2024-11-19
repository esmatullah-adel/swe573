from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.template import loader
from django.contrib.auth.decorators import login_required


def login_view(request): 
    if request.method == "POST": 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): 
            login(request, form.get_user())
            return redirect("/")
    else: 
        form = AuthenticationForm()
    return render(request, "users/login.html", { "form": form })

@login_required(login_url="/users/login/")

def users(request):
  myusers = User.objects.all().values()
  template = loader.get_template('users/show_all_users.html')
  context = {
    'myusers': myusers,
  }
  return HttpResponse(template.render(context, request))


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:users")
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {"form": form})


def logout_view(request):
    if request.method == "POST": 
        logout(request) 
        return redirect("/")