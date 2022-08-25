from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.forms import ModelForm
from .models import workers
from .form import workersform
# Create your views here.
def index(request) :
  if request.method == "POST" :
    form = workersform(request.POST).save()
    return redirect('/uploadApp')
  else :
    form= workersform
  #template=loader.get_template('index.html')
  #data = {'employees':['Ghassen','Elyes','Khalil'] }
  return render(request,'index.html',{'form':form,'dataworkers':workers.objects.all()})
  #return HttpResponse(template.render())