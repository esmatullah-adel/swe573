from django.urls import path
from . import views

urlpatterns = [
    path('item/', views.items, name='items'),
    path('item/new/', views.new_item, name='new_item'),
    path('item/<int:item_id>/', views.show_item, name='show_item'),
    path('item/edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('item/<int:id>/delete/', views.delete_item, name='delete_item'),
]