from django.contrib import admin

# Register your models here.
from .models import Department,Course,Register

admin.site.register(Department)

admin.site.register(Course)

admin.site.register(Register)