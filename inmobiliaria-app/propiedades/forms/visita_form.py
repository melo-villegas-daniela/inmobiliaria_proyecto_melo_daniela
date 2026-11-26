from django import forms
from propiedades.models import Visita

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['propiedad', 'nombre_interesado', 'fecha', 'estado']
        widgets = {'fecha': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')}