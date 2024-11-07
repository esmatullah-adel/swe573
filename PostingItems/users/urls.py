from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('users/details/<int:id>', views.details, name='details'),
]