from django.conf import settings
from django.db import models
from django.urls import reverse


class Visita(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'pendiente', 'Pendiente'
        REALIZADA = 'realizada', 'Realizada'
        CANCELADA = 'cancelada', 'Cancelada'

    propiedad = models.ForeignKey(
        'propiedades.Propiedad', on_delete=models.CASCADE, related_name='visitas'
    )
    nombre_interesado = models.CharField(max_length=120)
    fecha = models.DateField()
    estado = models.CharField(max_length=10, choices=Estado.choices, default=Estado.PENDIENTE)
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT,
        related_name='visitas_creadas')

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'visita'
        verbose_name_plural = 'visitas'

    def __str__(self):
        return f'{self.nombre_interesado} - {self.propiedad}'

    def get_absolute_url(self):
        return reverse('visita_detail', args=[self.pk])