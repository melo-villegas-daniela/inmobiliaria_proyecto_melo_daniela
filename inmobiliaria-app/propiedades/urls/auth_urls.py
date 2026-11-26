from django.urls import path
from propiedades.views import auth_views as v

urlpatterns = [
    path('registro/', v.registro, name='registro'),
    path('login/', v.login_view, name='login'),
    path('logout/', v.logout_view, name='logout')]