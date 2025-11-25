# Ex02 Django ORM Web Application
# Date:
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 cars

# PROGRAM

models.py
```
from django.db import models
from django.contrib import admin

class product(models.Model):
    product_name=models.CharField(max_length=20)
    published_date=models.IntegerField()
    fuel_type=models.CharField(max_length=20)
    product_price=models.CharField(max_length=20)

```
admin.py
```
from django.contrib import admin
from .models import product
admin.site.register(product)
```
# OUTPUT

c:\Users\acer\Desktop\web_vs_code\Screenshot (16).png

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
