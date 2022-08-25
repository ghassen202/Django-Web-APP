from django.forms import ModelForm
from .models import workers
class workersform(ModelForm) :
    class Meta :
        model = workers
        fields= ['name','email','department']