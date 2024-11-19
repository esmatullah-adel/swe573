from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Item
from .models import Material
from .models import Color
from .models import Shape
from .models import Currency
from .models import MeasurementUnit
from .forms import ItemForm
from django.db.models import Max  # Make sure this is imported
from django.contrib.auth.decorators import login_required

@login_required(login_url="/users/login/")
def items(request):
  myitems = Item.objects.all().values()
  template = loader.get_template('show_all_items.html')
  context = {
    'myitems': myitems,
  }
  return HttpResponse(template.render(context, request))

def new_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)  # Include files in the form
        if form.is_valid():
            # Save the form to the database
            form.save()
            return redirect('items')  # Redirect to a list of items or a success page
        else:
            return render(request, 'add_new_item.html', {'form': form, 'materials': Material.objects.all(), 
                                                         'colors': Color.objects.all(), 'shapes': Shape.objects.all(),
                                                         'currencies': Currency.objects.all(), 'measurementUnits': MeasurementUnit.objects.all(),
                                                         'item_max_no': Item.objects.aggregate(Max('id'))['id__max'] + 1})
    else:
    # Use the aggregate function to find the max value of the 'id' field
      item_max_no = Item.objects.aggregate(Max('id'))['id__max'] + 1
      materials = Material.objects.all()  # Retrieve all materials
      colors = Color.objects.all()  # Retrieve all colors
      shapes = Shape.objects.all()  # Retrieve all shapes
      currencies = Currency.objects.all()  # Retrieve all currencies
      measurementUnits = MeasurementUnit.objects.all()  # Retrieve all measurementunits
      template = loader.get_template('add_new_item.html')
      context = {
        'item_max_no': item_max_no,
        'materials': materials,
        'colors': colors,
        'shapes': shapes,
        'currencies': currencies,
        'measurementUnits': measurementUnits,
      }
      return HttpResponse(template.render(context, request))

# def store_item(request):
#     if request.method == 'POST':
#         form = ItemForm(request.POST, request.FILES)  # Include files in the form
#         if form.is_valid():
#             # Save the form to the database
#             form.save()
#             return redirect('items')  # Redirect to a list of items or a success page
#         else:
#             return render(request, 'add_new_item.html', {'form': form, 'materials': Material.objects.all(), 'colors': Color.objects.all(), 'shapes': Shape.objects.all()})
#     else:
#         form = ItemForm()
#         return render(request, 'add_new_item.html', {'form': form, 'materials': Material.objects.all(), 'colors': Color.objects.all(), 'shapes': Shape.objects.all()})


def show_item(request):
    # Use the aggregate function to find the max value of the 'id' field
  item_max_no = Item.objects.aggregate(Max('id'))['id__max'] + 1
  materials = Material.objects.all()  # Retrieve all materials
  colors = Color.objects.all()  # Retrieve all colors
  shapes = Shape.objects.all()  # Retrieve all shapes
  template = loader.get_template('show_item.html')
  context = {
    'item_max_no': item_max_no,
    'materials': materials,
    'colors': colors,
    'shapes': shapes,
  }
  return HttpResponse(template.render(context, request))

def edit_item(request):
    # Use the aggregate function to find the max value of the 'id' field
  item_max_no = Item.objects.aggregate(Max('id'))['id__max'] + 1
  materials = Material.objects.all()  # Retrieve all materials
  colors = Color.objects.all()  # Retrieve all colors
  shapes = Shape.objects.all()  # Retrieve all shapes
  template = loader.get_template('edit_item.html')
  context = {
    'item_max_no': item_max_no,
    'materials': materials,
    'colors': colors,
    'shapes': shapes,
  }
  return HttpResponse(template.render(context, request))