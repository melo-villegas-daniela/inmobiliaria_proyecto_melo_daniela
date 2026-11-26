from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

class Propiedad(models.Model):
    class Tipo(models.TextChoices):
        CASA = 'casa', 'Casa'
        DEPARTAMENTO = 'departamento', 'Departamento'
        TERRENO = 'terreno', 'Terreno'
        LOCAL = 'local', 'Local comercial'

    class Operacion(models.TextChoices):
            VENTA = 'venta', 'Venta'
            ARRIENDO = 'arriendo', 'Arriendo'

    class Estado(models.TextChoices):
            DISPONIBLE = 'disponible', 'Disponible'
            RESERVADA = 'reservada', 'Reservada'
            CERRADA = 'cerrada', 'Vendida o arrendada'

    titulo = models.CharField(max_length=150)
    tipo = models.CharField(max_length=20, choices=Tipo.choices)
    operacion = models.CharField(max_length=10, choices=Operacion.choices)
    estado = models.CharField(max_length=12, choices=Estado.choices, default=Estado.DISPONIBLE)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_publicacion = models.DateField(default=timezone.localdate)
    descripcion = models.TextField(blank=True)
    zona = models.ForeignKey(
        'propiedades.Zona', 
        on_delete=models.PROTECT, 
        related_name='propiedades')
    caracteristicas = models.ManyToManyField(
        'propiedades.Caracteristica', 
        blank=True, 
        related_name='propiedades')
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        related_name='propiedades_creadas')

    class Meta:
        ordering= ['-fecha_publicacion', 'titulo']
        verbose_name = 'propiedad'
        verbose_name_plural = 'propiedades'

    def __str__(self):
          return self.titulo

    def get_absolute_url(self):        
        return reverse('propiedad_detail', args=[self.pk])