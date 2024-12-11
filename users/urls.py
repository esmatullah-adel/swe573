from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('users/', views.users, name='users'),
    path('users/register/', views.register_view, name='register'),
    path('users/login/', views.login_view, name='login'),
    path('user_profile/<int:user_id>/', views.show_user_profile, name='show_user_profile'),
]