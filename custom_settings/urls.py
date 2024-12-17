from django.urls import path
from . import views

urlpatterns = [
    path('currency/new/', views.new_currency, name='new_currency'),
    path('width/new/', views.new_width, name='new_width'),
    path('weight/new/', views.new_weight, name='new_weight'),
    path('shape/new/', views.new_shape, name='new_shape'),
    path('color/new/', views.new_color, name='new_color'),
    path('material/new/', views.new_material, name='new_material'),
]