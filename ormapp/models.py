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