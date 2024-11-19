from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.items, name='items'),
    path('items/new/', views.new_item, name='new_item'),
    # path('item/store/', views.store_item, name='store_item'),
    path('item/show/', views.show_item, name='show_item'),
    path('item/edit/', views.edit_item, name='edit_item'),
]