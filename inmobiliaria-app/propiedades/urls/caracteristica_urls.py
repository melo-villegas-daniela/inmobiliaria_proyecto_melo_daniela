from django.urls import path

from propiedades.views import caracteristica_views as v

urlpatterns = [
    path('caracteristicas/', v.caracteristica_list, name='caracteristica_list'),
    path('caracteristicas/<int:pk>/', v.caracteristica_detail, name='caracteristica_detail')]