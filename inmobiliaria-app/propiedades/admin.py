from django.contrib import admin
from propiedades.models import Zona, Caracteristica, Propiedad, Visita

@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad')
    list_filter = ('ciudad',)
    search_fields = ('nombre', 'ciudad')

@admin.register(Caracteristica)
class CaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 
                    'tipo', 
                    'operacion', 
                    'precio', 
                    'zona', 
                    'estado', 
                    'creado_por')
    list_filter = ('tipo', 'operacion', 'estado', 'zona')
    search_fields = ('titulo', 'descripcion')
    filter_horizontal = ('caracteristicas',)

@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ('propiedad', 'nombre_interesado', 'fecha', 'estado')
    list_filter = ('estado', 'fecha')
    search_fields = ('nombre_interesado', 'propiedad__titulo')

