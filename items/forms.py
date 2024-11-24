# forms.py
from django import forms
from .models import Item, Material, Color, Shape

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['id','name','description','tag','width','length','height','measurement_unit_id','price','currency_id','taste','smell','material_id','color_id','shape_id','image']

    # Optionally, add custom validation or other fields if needed.