from django.db import models
from django.contrib import admin

class product(models.Model):
    product_name=models.CharField(max_length=20)
    published_date=models.IntegerField()
    fuel_type=models.CharField(max_length=20)
    product_price=models.CharField(max_length=20)
