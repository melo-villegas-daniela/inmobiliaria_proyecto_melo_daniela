from django import forms
from propiedades.models import Zona

class ZonaForm(forms.ModelForm):
    class Meta:
        model = Zona
        fields = ['nombre', 'ciudad', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej. La Carolina'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }