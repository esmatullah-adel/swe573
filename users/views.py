from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.template import loader
from django.contrib.auth.decorators import login_required
from items.models import Comment, Item


def login_view(request): 
    if request.method == "POST": 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): 
            login(request, form.get_user())
            return redirect("/")
    else: 
        form = AuthenticationForm()
    return render(request, "users/login.html", { "form": form })


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
            # Print or log the errors for debugging
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {"form": form})


def show_user_profile(request, user_id):
    template = loader.get_template('users/show_user_profile.html')
    # Fetch the main item
    selected_user = get_object_or_404(User, id=user_id)
    total_comments = Comment.objects.filter(user_id=user_id).count()
    total_posts = Item.objects.filter(user=selected_user).count()
    comments = Comment.objects.filter(user_id=user_id)
    posts = Item.objects.filter(user=selected_user)

    context = {
        'selected_user': selected_user,
        'total_posts': total_posts,
        'total_comments': total_comments,
        'posts': posts,
        'comments': comments,
    }
    return HttpResponse(template.render(context, request))