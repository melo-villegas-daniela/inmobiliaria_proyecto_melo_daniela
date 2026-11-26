from django.urls import path
from propiedades.views import visita_views as v

urlpatterns = [
    path('visitas/', v.visita_list, name='visita_list'),
    path('visitas/<int:pk>/', v.visita_detail, name='visita_detail')]