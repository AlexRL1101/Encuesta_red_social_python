from django import forms
from django.forms import ModelForm

from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee

        fields = ('Correo', 'Edad',
                  'Sexo', 'Social', 'Facebook', 'WhatsApp', 'Twitter', 'Instagram', 'Tiktok')

        widgets = {
            'Correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Su correo electronico', 'type': 'email'}),
            'Edad': forms.Select(attrs={'class': 'form-control'}),
            'Sexo': forms.Select(attrs={'class': 'form-control'}),
            'Social': forms.Select(attrs={'class': 'form-control'}),
            'Facebook': forms.Select(attrs={'class': 'form-control'}),
            'WhatsApp': forms.Select(attrs={'class': 'form-control'}),
            'Twitter': forms.Select(attrs={'class': 'form-control'}),
            'Instagram': forms.Select(attrs={'class': 'form-control'}),
            'Tiktok': forms.Select(attrs={'class': 'form-control'}),
        }
