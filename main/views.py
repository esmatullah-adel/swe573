from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader

from items.models import Item
from django.shortcuts import redirect
from django.contrib.auth import logout

def dashboard(request):
  myitems = Item.objects.all().values()
  template = loader.get_template('dashboard.html')
  context = {
    'myitems': myitems,
  }
  return HttpResponse(template.render(context, request))


def logout_view(request):
    if request.method == "POST": 
        logout(request) 
        return HttpResponseRedirect("/")

