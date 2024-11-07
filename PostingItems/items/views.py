from django.http import HttpResponse
from django.template import loader
from .models import Item

def items(request):
  myitems = Item.objects.all().values()
  template = loader.get_template('show_all_items.html')
  context = {
    'myitems': myitems,
  }
  return HttpResponse(template.render(context, request))
