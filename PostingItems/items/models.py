from django.db import models

class Item(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255, null=True)
  tag = models.CharField(max_length=255, null=True)
  width = models.CharField(max_length=255, null=True)
  length = models.CharField(max_length=255, null=True)
  height = models.CharField(max_length=255, null=True)
  measurement_unit_id = models.IntegerField(default=0)
  price = models.CharField(max_length=255, null=True)
  currency_id = models.IntegerField(default=0)
  taste = models.CharField(max_length=255, null=True)
  smell = models.CharField(max_length=255, null=True)
  material_id = models.IntegerField(default=0)
  color_id = models.IntegerField(default=0)
  shape_id = models.IntegerField(default=0)
  image = models.ImageField(default='fallback.png', blank=True)

class Material(models.Model):
  title = models.CharField(max_length=255, null=True)

class Color(models.Model):
  title = models.CharField(max_length=255, null=True)

class Shape(models.Model):
  title = models.CharField(max_length=255, null=True)

class MeasurementUnit(models.Model):
  title = models.CharField(max_length=255, null=True)

class Currency(models.Model):
  title = models.CharField(max_length=255, null=True)
