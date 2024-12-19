from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader

from items.models import Item
from django.shortcuts import redirect
from django.contrib.auth import logout
from items.models import Material
from items.models import Color
from items.models import Shape
from items.models import Currency, LengthUnit, WeightUnit, Condition, Hardness, ColorItem, MaterialItem, ShapeItem, TagItem
from django.http import JsonResponse
import json

def dashboard(request):
  if request.method == 'POST':
    data = json.loads(request.body)

    # Extract fields from the request
    id = data.get('id', '').strip()
    name = data.get('name', '').strip()
    description = data.get('description', '').strip()
    width = data.get('width', '').strip()
    min_width = data.get('min_width', '').strip()
    max_width = data.get('max_width', '').strip()
    length = data.get('length', '').strip()
    min_length = data.get('min_length', '').strip()
    max_length = data.get('max_length', '').strip()
    height = data.get('height', '').strip()
    min_height = data.get('min_height', '').strip()
    max_height = data.get('max_height', '').strip()
    length_unit_id = data.get('length_unit_id', '')  # Do not use .strip() on this field
    weight = data.get('weight', '').strip()
    min_weight = data.get('min_weight', '').strip()
    max_weight = data.get('max_weight', '').strip()
    weight_unit_id = data.get('weight_unit_id', '')  # Do not use .strip() on this field
    price = data.get('price', '').strip()
    min_price = data.get('min_price', '').strip()
    max_price = data.get('max_price', '').strip()
    currency_id = data.get('currency_id', '')  # Do not use .strip() on this field
    condition_id = data.get('condition_id', '')  # Do not use .strip() on this field
    hardness_id = data.get('hardness_id', '')  # Do not use .strip() on this field
    taste = data.get('taste', '').strip()
    smell = data.get('smell', '').strip()
    functionality = data.get('functionality', '').strip()
    age = data.get('age', '').strip()
    min_age = data.get('min_age', '').strip()
    max_age = data.get('max_age', '').strip()
    date = data.get('date', '').strip()
    latitude = data.get('latitude', '').strip()
    longitude = data.get('longitude', '').strip()
    active = data.get('active', '')  # Do not use .strip() on this field
    # Get the list of selected materials from the POST data
    selected_materials = data.get("materials[]", [])  # List of selected material IDs
    selected_colors = data.get("colors[]", [])  # List of selected colors
    selected_shapes = data.get("shapes[]", [])  # List of selected shapes
    selected_tags_ids = data.get("tag_ids", []).split(",")  # List of selected shapes
    # Remove empty strings from selected_tags_ids because when no tags select selected_tags_ids contains ['']
    selected_tags_ids = [tag_id for tag_id in selected_tags_ids if tag_id]

    # Build filter criteria dynamically
    filter_criteria = {}
    if id:
        filter_criteria['id'] = id
    if name:
        filter_criteria['name__icontains'] = name
    if latitude:
        filter_criteria['latitude__icontains'] = latitude
    if longitude:
        filter_criteria['longitude__icontains'] = longitude
    if description:
        filter_criteria['description__icontains'] = description
    if width:
        filter_criteria['width'] = width
        if length_unit_id:
          filter_criteria['length_unit_id'] = length_unit_id
    if length:
        filter_criteria['length'] = length
        if length_unit_id:
          filter_criteria['length_unit_id'] = length_unit_id
    if height:
        filter_criteria['height'] = height
        if length_unit_id:
          filter_criteria['length_unit_id'] = length_unit_id
    if weight:
        filter_criteria['weight'] = weight
        if weight_unit_id:
          filter_criteria['weight_unit_id'] = weight_unit_id
    if price:
        filter_criteria['price'] = price
        if currency_id:
          filter_criteria['currency_id'] = currency_id
    if condition_id:
        filter_criteria['condition_id'] = condition_id
    if hardness_id:
        filter_criteria['hardness_id'] = hardness_id
    if taste:
        filter_criteria['taste__icontains'] = taste
    if smell:
        filter_criteria['smell__icontains'] = smell
    if functionality:
        filter_criteria['functionality__icontains'] = functionality
    if age:
        filter_criteria['age'] = age
    if date:
        filter_criteria['date__icontains'] = date
    if active:
        filter_criteria['active'] = active


    if min_price:
        filter_criteria['price__gte'] = min_price  # Minimum price filter
    if max_price:
        filter_criteria['price__lte'] = max_price  # Maximum price filter
    if min_age:
        filter_criteria['age__gte'] = min_age  # Minimum age filter
    if max_age:
        filter_criteria['age__lte'] = max_age  # Maximum age filter
    if min_width:
        filter_criteria['width__gte'] = min_width  # Minimum width filter
    if max_width:
        filter_criteria['width__lte'] = max_width  # Maximum width filter
    if min_height:
        filter_criteria['height__gte'] = min_height  # Minimum height filter
    if max_height:
        filter_criteria['height__lte'] = max_height  # Maximum height filter
    if min_length:
        filter_criteria['length__gte'] = min_length  # Minimum length filter
    if max_length:
        filter_criteria['length__lte'] = max_length  # Maximum length filter
    if min_weight:
        filter_criteria['weight__gte'] = min_weight  # Minimum weight filter
    if max_weight:
        filter_criteria['weight__lte'] = max_weight  # Maximum weight filter

    # Filter by materials if selected_materials is not empty
    if selected_materials:
        # Filter items where the related materials match the selected materials
        filter_criteria['id__in'] = Item.objects.filter(
            id__in=MaterialItem.objects.filter(material_id__in=selected_materials).values('item_id')
        ).values('id')
    if selected_colors:
        # Filter items where the related colors match the selected colors
        filter_criteria['id__in'] = Item.objects.filter(
            id__in=ColorItem.objects.filter(color_id__in=selected_colors).values('item_id')
        ).values('id')
    if selected_shapes:
        # Filter items where the related shapes match the selected shapes
        filter_criteria['id__in'] = Item.objects.filter(
            id__in=ShapeItem.objects.filter(shape_id__in=selected_shapes).values('item_id')
        ).values('id')
    if selected_tags_ids:
        # Filter items where the related tags match the selected tags
        filter_criteria['id__in'] = Item.objects.filter(
            id__in=TagItem.objects.filter(tag_id__in=selected_tags_ids).values('item_id')
        ).values('id')

    print("Filter Criteria:", filter_criteria)
    # Apply filters and get results
    myitems = list(Item.objects.filter(**filter_criteria).order_by('-id').values())

    return JsonResponse({'success': True, 'items': myitems})
  else:
    myitems = Item.objects.all().order_by('-id').values()
    materials = Material.objects.all()  # Retrieve all materials
    colors = Color.objects.all()  # Retrieve all colors
    shapes = Shape.objects.all()  # Retrieve all shapes
    currencies = Currency.objects.all()  # Retrieve all currencies
    lengthUnits = LengthUnit.objects.all()  # Retrieve all lengthunits
    weightUnits = WeightUnit.objects.all()  # Retrieve all lengthunits
    conditions = Condition.objects.all()  # Retrieve all lengthunits
    hardnesses = Hardness.objects.all()  # Retrieve all lengthunits
    template = loader.get_template('dashboard.html')
    context = {
      'myitems': myitems,
      'materials': materials,
      'colors': colors,
      'shapes': shapes,
      'currencies': currencies,
      'lengthUnits': lengthUnits,
      'weightUnits': weightUnits,
      'conditions': conditions,
      'hardnesses': hardnesses,
    }
    return HttpResponse(template.render(context, request))


def logout_view(request):
    if request.method == "POST": 
        logout(request) 
        return HttpResponseRedirect("/")

