from django.shortcuts import render, redirect
from django.http import HttpResponse
from items.models import Currency, Material, Shape, Color, WeightUnit, LengthUnit, Condition, Hardness
from django.template import loader
from django.db.models import Max  # Make sure this is imported
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/users/login/")
def new_currency(request):
    if request.method == 'POST':
        # Get form data, use .get() to avoid KeyError
        currency_id = request.POST.get('id')
        title = request.POST.get('title')
        
        if currency_id and title:
            # Create a new Currency object and save it
            currency = Currency(id=currency_id, title=title)
            currency.save()

        return redirect('/')  # Redirect to a list of currencys or a success page
    else:
    # Use the aggregate function to find the max value of the 'id' field
      currency_max_no = Currency.objects.aggregate(Max('id'))['id__max']
      currency_max_no = (currency_max_no or 0) + 1
      template = loader.get_template('currencies/add_new_currency.html')
      context = {
        'currency_max_no': currency_max_no,
      }
      return HttpResponse(template.render(context, request))



@login_required(login_url="/users/login/")
def new_width(request):
    if request.method == 'POST':
        # Get form data, use .get() to avoid KeyError
        width_id = request.POST.get('id')
        title = request.POST.get('title')
        
        if width_id and title:
            # Create a new Width object and save it
            width = LengthUnit(id=width_id, title=title)
            width.save()

        return redirect('/')  # Redirect to a list of widths or a success page
    else:
    # Use the aggregate function to find the max value of the 'id' field
      width_max_no = LengthUnit.objects.aggregate(Max('id'))['id__max']
      width_max_no = (width_max_no or 0) + 1
      template = loader.get_template('width_units/add_new_width.html')
      context = {
        'width_max_no': width_max_no,
      }
      return HttpResponse(template.render(context, request))



@login_required(login_url="/users/login/")
def new_weight(request):
    if request.method == 'POST':
        # Get form data, use .get() to avoid KeyError
        weight_id = request.POST.get('id')
        title = request.POST.get('title')
        
        if weight_id and title:
            # Create a new Weight object and save it
            weight = WeightUnit(id=weight_id, title=title)
            weight.save()

        return redirect('/')  # Redirect to a list of weights or a success page
    else:
    # Use the aggregate function to find the max value of the 'id' field
      weight_max_no = WeightUnit.objects.aggregate(Max('id'))['id__max']
      weight_max_no = (weight_max_no or 0) + 1
      template = loader.get_template('weight_units/add_new_weight.html')
      context = {
        'weight_max_no': weight_max_no,
      }
      return HttpResponse(template.render(context, request))



@login_required(login_url="/users/login/")
def new_material(request):
    if request.method == 'POST':
        # Get form data, use .get() to avoid KeyError
        material_id = request.POST.get('id')
        title = request.POST.get('title')
        
        if material_id and title:
            # Create a new Material object and save it
            material = Material(id=material_id, title=title)
            material.save()

        return redirect('/')  # Redirect to a list of materials or a success page
    else:
    # Use the aggregate function to find the max value of the 'id' field
      material_max_no = Material.objects.aggregate(Max('id'))['id__max']
      material_max_no = (material_max_no or 0) + 1
      template = loader.get_template('materials/add_new_material.html')
      context = {
        'material_max_no': material_max_no,
      }
      return HttpResponse(template.render(context, request))



@login_required(login_url="/users/login/")
def new_color(request):
    if request.method == 'POST':
        # Get form data, use .get() to avoid KeyError
        color_id = request.POST.get('id')
        title = request.POST.get('title')
        
        if color_id and title:
            # Create a new Color object and save it
            color = Color(id=color_id, title=title)
            color.save()

        return redirect('/')  # Redirect to a list of colors or a success page
    else:
    # Use the aggregate function to find the max value of the 'id' field
      color_max_no = Color.objects.aggregate(Max('id'))['id__max']
      color_max_no = (color_max_no or 0) + 1
      template = loader.get_template('colors/add_new_color.html')
      context = {
        'color_max_no': color_max_no,
      }
      return HttpResponse(template.render(context, request))



@login_required(login_url="/users/login/")
def new_shape(request):
    if request.method == 'POST':
        # Get form data, use .get() to avoid KeyError
        shape_id = request.POST.get('id')
        title = request.POST.get('title')
        
        if shape_id and title:
            # Create a new Shape object and save it
            shape = Shape(id=shape_id, title=title)
            shape.save()

        return redirect('/')  # Redirect to a list of shapes or a success page
    else:
    # Use the aggregate function to find the max value of the 'id' field
      shape_max_no = Shape.objects.aggregate(Max('id'))['id__max']
      shape_max_no = (shape_max_no or 0) + 1
      template = loader.get_template('shapes/add_new_shape.html')
      context = {
        'shape_max_no': shape_max_no,
      }
      return HttpResponse(template.render(context, request))


def new_hardness(request):
    if request.method == 'POST':
        # Get form data, use .get() to avoid KeyError
        hardness_id = request.POST.get('id')
        title = request.POST.get('title')
        
        if hardness_id and title:
            # Create a new Hardness object and save it
            hardness = Hardness(id=hardness_id, title=title)
            hardness.save()

        return redirect('/')  # Redirect to a list of hardnesss or a success page
    else:
    # Use the aggregate function to find the max value of the 'id' field
      hardness_max_no = Hardness.objects.aggregate(Max('id'))['id__max']
      hardness_max_no = (hardness_max_no or 0) + 1
      template = loader.get_template('hardness/add_new_hardness.html')
      context = {
        'hardness_max_no': hardness_max_no,
      }
      return HttpResponse(template.render(context, request))



def new_condition(request):
    if request.method == 'POST':
        # Get form data, use .get() to avoid KeyError
        condition_id = request.POST.get('id')
        title = request.POST.get('title')
        
        if condition_id and title:
            # Create a new Condition object and save it
            condition = Condition(id=condition_id, title=title)
            condition.save()

        return redirect('/')  # Redirect to a list of conditions or a success page
    else:
    # Use the aggregate function to find the max value of the 'id' field
      condition_max_no = Condition.objects.aggregate(Max('id'))['id__max']
      condition_max_no = (condition_max_no or 0) + 1
      template = loader.get_template('condition/add_new_condition.html')
      context = {
        'condition_max_no': condition_max_no,
      }
      return HttpResponse(template.render(context, request))


