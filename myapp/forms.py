from django import forms
from .models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'year', 'garage']