from django.db import models

class LengthUnit(models.Model):
  title = models.CharField(max_length=255, null=True)

class WeightUnit(models.Model):
  title = models.CharField(max_length=255, null=True)

class Item(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255, null=True)
  functionality = models.CharField(max_length=255, null=True)
  taste = models.CharField(max_length=255, null=True)
  smell = models.CharField(max_length=255, null=True)
  age = models.CharField(max_length=255, null=True)
  width = models.IntegerField(default=0)
  length = models.IntegerField(default=0)
  height = models.IntegerField(default=0)
  length_unit = models.ForeignKey(LengthUnit, on_delete=models.CASCADE, default=1)
  weight = models.IntegerField(default=0)
  weight_unit_id = models.IntegerField(default=1)
  price = models.IntegerField(default=0)
  currency_id = models.IntegerField(default=1)
  hardness_id = models.IntegerField(default=1)
  condition_id = models.IntegerField(default=1)
  image = models.ImageField(default='fallback.png', blank=True)
  latitude = models.FloatField(null=True)
  longitude = models.FloatField(null=True)
    

class Material(models.Model):
  title = models.CharField(max_length=255, null=True)

class Color(models.Model):
  title = models.CharField(max_length=255, null=True)

class Shape(models.Model):
  title = models.CharField(max_length=255, null=True)

class Currency(models.Model):
  title = models.CharField(max_length=255, null=True)

class Tag(models.Model):
  title = models.CharField(max_length=255)
  tag_id = models.CharField(max_length=255)

class TagItem(models.Model):
  item_id = models.CharField(max_length=255)
  tag_id = models.CharField(max_length=255)

class MaterialItem(models.Model):
  item_id = models.CharField(max_length=255)
  material_id = models.CharField(max_length=255)

class ColorItem(models.Model):
  item_id = models.CharField(max_length=255)
  color_id = models.CharField(max_length=255)

class ShapeItem(models.Model):
  item_id = models.CharField(max_length=255)
  shape_id = models.CharField(max_length=255)

class Comment(models.Model):
  title = models.CharField(max_length=255)
  item_id = models.CharField(max_length=255)
  user_id = models.CharField(max_length=255, null=True)
  date = models.CharField(max_length=255, null=True)

class Condition(models.Model):
  title = models.CharField(max_length=255)

class Hardness(models.Model):
  title = models.CharField(max_length=255)
