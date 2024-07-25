from django.contrib import admin

# Register your models here.
from .models import Postion, Employee

admin.site.register(Postion)
admin.site.register(Employee)