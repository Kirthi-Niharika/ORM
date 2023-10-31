# Ex02 Django ORM Web Application
## Date: 25.09.2023

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM

```
Models.py 

from django.db import models
from django.contrib import admin
class Football (models.Model):
    jno=models.IntegerField()
    name=models.CharField(max_length=100)
    team=models.CharField(max_length=100)
    age=models.IntegerField()
    win=models.IntegerField()

class FootballAdmin(admin.ModelAdmin):
    list_display=('jno','name','team','age','win')

Admin.py

from django.contrib import admin
from .models import Football,FootballAdmin
admin.site.register(Football,FootballAdmin)

```

## OUTPUT

![Alt text](exp2a.png)
![Alt text](exp2b.png)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully

