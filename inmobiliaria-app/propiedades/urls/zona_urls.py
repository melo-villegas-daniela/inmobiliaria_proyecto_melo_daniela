from django.urls import path
from propiedades.views import zona_views as v

urlpatterns = [
    path('zonas/', v.zona_list, name='zona_list'),
    path('zonas/nueva/', v.zona_create, name='zona_create'),
    path('zonas/<int:pk>/', v.zona_detail, name='zona_detail'),
    path('zonas/<int:pk>/editar/', v.zona_update, name='zona_update'),
    path('zonas/<int:pk>/eliminar/', v.zona_delete, name='zona_delete')]