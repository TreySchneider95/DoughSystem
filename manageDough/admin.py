from django.contrib import admin
from .models import Unit

# Register your models here.

myModels = [Unit]
admin.site.register(myModels)