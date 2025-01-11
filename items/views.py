from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from .models import Item
from .models import Material
from .models import Color
from .models import Shape
from .models import Comment
from .models import Currency
from .models import Tag
from .models import TagItem
from .models import MaterialItem
from .models import ColorItem
from .models import ShapeItem
from .models import LengthUnit, Condition, WeightUnit, Hardness
from django.db.models import Max  # Make sure this is imported
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
import json
from datetime import datetime

@login_required(login_url="/users/login/")
def items(request):
  # Query to get items and related lengthunit data
  myitems = Item.objects.filter(user=request.user).select_related('length_unit').values('id', 'name', 'description', 'width', 'height', 'length', 'length_unit__title', 'active')
  template = loader.get_template('show_all_items.html')
  context = {
    'myitems': myitems,
  }
  return HttpResponse(template.render(context, request))

def new_item(request):
    if request.method == 'POST':
        
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        width = request.POST.get('width', '0')
        length = request.POST.get('length', '0')
        height = request.POST.get('height', '0')
        length_unit_id = request.POST.get('length_unit_id', '1')
        weight = request.POST.get('weight', '0')  # Default to '0'
        try:
            weight = float(weight)  # Convert to float, if possible
        except ValueError:
            weight = 0  # Default to 0 if conversion fails
        try:
            width = float(width)  # Convert to float, if possible
        except ValueError:
            width = 0  # Default to 0 if conversion fails
        try:
            length = float(length)  # Convert to float, if possible
        except ValueError:
            length = 0  # Default to 0 if conversion fails
        try:
            height = float(height)  # Convert to float, if possible
        except ValueError:
            height = 0  # Default to 0 if conversion fails
        weight_unit_id = request.POST.get('weight_unit_id', '1')
        price = request.POST.get('price', '0')
        currency_id = request.POST.get('currency_id', '1')
        condition_id = request.POST.get('condition_id', '1')
        hardness_id = request.POST.get('hardness_id', '1')
        taste = request.POST.get('taste', '')
        smell = request.POST.get('smell', '')
        functionality = request.POST.get('functionality', '')
        age = request.POST.get('age', '0')
        latitude = request.POST.get('latitude', '0')
        longitude = request.POST.get('longitude', '0')
        try:
            latitude = float(latitude)  # Convert to float, if possible
        except ValueError:
            latitude = 0  # Default to 0 if conversion fails
        try:
            longitude = float(longitude)  # Convert to float, if possible
        except ValueError:
            longitude = 0  # Default to 0 if conversion fails
        image = request.FILES.get('image', None)
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        item = Item(name=name, description=description, width=width, length=length, height=height, length_unit_id=length_unit_id, weight=weight,
                    weight_unit_id=weight_unit_id, price=price
                    , currency_id=currency_id, taste=taste, smell=smell, latitude=latitude, longitude=longitude, functionality=functionality
                    , age=age, condition_id=condition_id, hardness_id=hardness_id, image=image, date=date)
        # Assign the logged-in user to the item
        item.user = request.user
        # Save the item to the database
        item.save()

        # Get the ID of the newly saved item
        item_id = item.id



        labels_list = request.POST["tag_labels"].split(",")  # List of tag names
        # Get the selected tag IDs (comma-separated string)
        ids_list = request.POST["tag_ids"].split(",")
        # Ensure both lists have the same length (if required)
        if len(labels_list) == len(ids_list):
            # Save each tag with its label and ID
            for label, tag_id in zip(labels_list, ids_list):
                tag, created = Tag.objects.get_or_create(title=label.strip(), tag_id=tag_id.strip())
                TagItem.objects.create(item_id=item_id, tag_id=tag_id.strip())



        selected_materials = request.POST.getlist("materials[]")  # List of selected materials
        for material_id in selected_materials:
                MaterialItem.objects.create(item_id=item_id, material_id=material_id)


        selected_colors = request.POST.getlist("colors[]")  # List of selected colors
        for color_id in selected_colors:
                ColorItem.objects.create(item_id=item_id, color_id=color_id)


        selected_shapes = request.POST.getlist("shapes[]")  # List of selected shapes
        for shape_id in selected_shapes:
                ShapeItem.objects.create(item_id=item_id, shape_id=shape_id)


        return redirect('items')  # Redirect to a list of items or a success page
    else:
    # Use the aggregate function to find the max value of the 'id' field
      item_max_no = Item.objects.aggregate(Max('id'))['id__max']
      item_max_no = (item_max_no or 0) + 1
      materials = Material.objects.all()  # Retrieve all materials
      colors = Color.objects.all()  # Retrieve all colors
      shapes = Shape.objects.all()  # Retrieve all shapes
      currencies = Currency.objects.all()  # Retrieve all currencies
      lengthUnits = LengthUnit.objects.all()  # Retrieve all lengthunits
      weightUnits = WeightUnit.objects.all()  # Retrieve all lengthunits
      conditions = Condition.objects.all()  # Retrieve all lengthunits
      hardnesses = Hardness.objects.all()  # Retrieve all lengthunits
      template = loader.get_template('add_new_item.html')
      context = {
        'item_max_no': item_max_no,
        'materials': materials,
        'colors': colors,
        'shapes': shapes,
        'currencies': currencies,
        'lengthUnits': lengthUnits,
        'weightUnits': weightUnits,
        'conditions': conditions,
        'hardnesses': hardnesses,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
      }
      return HttpResponse(template.render(context, request))


def show_item(request, item_id):
  if request.method == 'POST':
    title = request.POST['comment']
    user = request.user
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    item = get_object_or_404(Item, id=item_id)
    comment = Comment(title=title, item=item, user=user, date=date)
    # Save the comment to the database
    comment.save()
    return redirect('/item/' + str(item_id))  # Redirect to a list of items or a success page
  else:
    template = loader.get_template('show_item.html')
    # Fetch the main item
    item = get_object_or_404(Item, id=item_id)
    
    # Fetch related objects
    length_unit = item.length_unit  # Accessing the related LengthUnit object directly
    weight_unit = WeightUnit.objects.filter(id=item.weight_unit_id).first()
    currency = Currency.objects.filter(id=item.currency_id).first()
    condition = Condition.objects.filter(id=item.condition_id).first()
    hardness = Hardness.objects.filter(id=item.hardness_id).first()

    # Related materials, colors, shapes, and tags
    materials = Material.objects.filter(id__in=MaterialItem.objects.filter(item_id=item_id).values_list('material_id', flat=True))
    colors = Color.objects.filter(id__in=ColorItem.objects.filter(item_id=item_id).values_list('color_id', flat=True))
    shapes = Shape.objects.filter(id__in=ShapeItem.objects.filter(item_id=item_id).values_list('shape_id', flat=True))
    tags = Tag.objects.filter(tag_id__in=TagItem.objects.filter(item_id=item_id).values_list('tag_id', flat=True))
    comments = Comment.objects.filter(item_id=item_id).select_related('user')

    context = {
        'item': item,
        'length_unit': length_unit,
        'weight_unit': weight_unit,
        'currency': currency,
        'condition': condition,
        'hardness': hardness,
        'materials': materials,
        'colors': colors,
        'shapes': shapes,
        'tags': tags,
        'comments': comments,
          'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return HttpResponse(template.render(context, request))

def edit_item(request, item_id):
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

def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == "POST":
        item.delete()
        messages.success(request, "Item deleted successfully.")
        return redirect('items')  # Replace with your item list view name
    return redirect('items')  # Redirect in case of a GET request

def inactivate_item(request, id):
    item = get_object_or_404(Item, id=id)
    if item.active == 1:  # Assuming 'active' is an integer field
        item.active = 0
        messages.success(request, "Item inactivated successfully.")
    else:
        item.active = 1
        messages.success(request, "Item activated successfully.")
    item.save()
    return redirect('items')  # Replace 'items' with your actual item list view name
