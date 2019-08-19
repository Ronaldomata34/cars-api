from django.contrib import admin

from .models import Car, CarModel, CarMake

admin.site.register(Car)
admin.site.register(CarModel)
admin.site.register(CarMake)