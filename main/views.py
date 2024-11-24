from django.http import HttpResponse

from django.template import loader

from items.models import Item

def dashboard(request):
  myitems = Item.objects.all().values()
  template = loader.get_template('dashboard.html')
  context = {
    'myitems': myitems,
  }
  return HttpResponse(template.render(context, request))

