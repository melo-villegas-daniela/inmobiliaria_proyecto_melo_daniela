from django import forms

from propiedades.models import Propiedad


class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = [
            'titulo', 'tipo', 
            'operacion', 'estado', 
            'precio','fecha_publicacion', 
            'zona', 'caracteristicas', 
            'descripcion']

        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'caracteristicas': forms.CheckboxSelectMultiple(),
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor que cero.')
        return precio