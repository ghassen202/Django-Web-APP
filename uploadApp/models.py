from django.db import models
from django.contrib import admin
# Create your models here.
class workers(models.Model) :
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=50)
    department=models.CharField(max_length=30)
class workersadmin(admin.ModelAdmin) :
    list_display =['name','email','department']
    list_filter =('department',)
    search_fields =['name','email']