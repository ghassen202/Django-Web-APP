from asyncio.windows_events import NULL
from django.db import models
from django.contrib import admin
# Create your models here.
class workers(models.Model) :
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=50)
    department=models.CharField(max_length=30)
    fich=models.FileField(upload_to='photos ')
class workersadmin(admin.ModelAdmin) :
    list_display =['name','email','department','fich']
    list_filter =('department',)
    search_fields =['name','email']