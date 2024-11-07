# from django.shortcuts import render
# from django.http import HttpResponse

# def users(request):
#     return HttpResponse("Hello world!")
# ************************************
# from django.http import HttpResponse
# from django.template import loader

# def users(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())
# *****************************************
from django.http import HttpResponse
from django.template import loader
from .models import Member

def users(request):
  myusers = Member.objects.all().values()
  template = loader.get_template('all_users.html')
  context = {
    'myusers': myusers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))