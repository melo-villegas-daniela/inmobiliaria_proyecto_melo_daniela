from propiedades.urls.zona_urls import urlpatterns as zona_urls
from propiedades.urls.caracteristica_urls import urlpatterns as caracteristica_urls
from propiedades.urls.propiedad_urls import urlpatterns as propiedad_urls
from propiedades.urls.visita_urls import urlpatterns as visita_urls

urlpatterns = zona_urls + caracteristica_urls + propiedad_urls + visita_urls 