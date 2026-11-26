from django.urls import path
from propiedades.views import propiedad_views as v

urlpatterns = [
    path('', v.propiedad_list, name='propiedad_list'),
    path('propiedades/nueva/', v.propiedad_create, name='propiedad_create'),
    path('propiedades/<int:pk>/', v.propiedad_detail, name='propiedad_detail'),
    path('propiedades/<int:pk>/editar/', v.propiedad_update, name='propiedad_update'),
    path('propiedades/<int:pk>/eliminar/', v.propiedad_delete, name='propiedad_delete')]