from django import forms
from propiedades.models import Caracteristica


class CaracteristicaForm(forms.ModelForm):
    class Meta:
        model = Caracteristica
        fields = ['nombre']
        widgets = {'nombre': forms.TextInput(attrs={'placeholder': 'Ej. Piscina'})}