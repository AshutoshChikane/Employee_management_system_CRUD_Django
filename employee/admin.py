from django.contrib import admin
from .models import employee

# Register your models here.
@admin.register(employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display =("emp_id","first_name","last_name")
