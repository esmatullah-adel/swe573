from django.db import models

class Item(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255, null=True)
  size = models.CharField(max_length=255, null=True)
  price = models.CharField(max_length=255, null=True)
