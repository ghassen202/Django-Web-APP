from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.template import loader
from django.forms import ModelForm
from .models import workers
from .form import workersform
import logging 
import ftplib

# Create your views here.
def index(request) :
  if request.method == "POST" :
    form = workersform(request.POST, request.FILES)
    if form.is_valid() :
      form.save()
      
      ftphost='localhost'
      ftpPort= 21
      ftpUname='gaston'
      ftpPass ='789'

      ftp = ftplib.FTP(timeout=30)
      ftp.connect(ftphost,ftpPort)
      ftp.login(ftpUname,ftpPass)

      ftp.cwd("folder1/abcd")

      localFilePath = "C:/Users/user/Desktop/stage/Media/photos/"+ str(form['fich'].value())
      with open(localFilePath,'rb') as file :
          action = ftp.storbinary(f"STOR {str(form['fich'].value())}",file,blocksize=1024)

      ftp.quit()
      return HttpResponseRedirect('/uploadApp/')  
  else :
    form= workersform()
  #template=loader.get_template('index.html')
  #data = {'employees':['Ghassen','Elyes','Khalil'] }

  return render(request,'index.html',{'form':form,'dataworkers':workers.objects.all()})
  #return HttpResponse(template.render())