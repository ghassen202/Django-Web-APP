from django.contrib import admin
from .models import workers
from .models import workersadmin
# Register your models here.
admin.site.register(workers,workersadmin)