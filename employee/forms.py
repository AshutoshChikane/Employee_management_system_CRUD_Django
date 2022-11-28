from django import forms
from .models import employee
class new_employee(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'


class edit_employee(forms.ModelForm):
    class Meta():
        model=employee        
        fields=("phone",)

