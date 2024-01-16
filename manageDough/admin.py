from django.contrib import admin
from .models import Unit, InventoryRaw, Calcs

# Register your models here.

myModels = [Unit, InventoryRaw, Calcs]
admin.site.register(myModels)