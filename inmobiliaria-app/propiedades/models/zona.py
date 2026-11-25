from django.db import models
from django.urls import reverse

class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ['ciudad','nombre']
        verbose_name = 'zona'
        verbose_name_plural = 'zonas'

    def __str__(self):
        return f'{self.nombre} ({self.ciudad})'

    def get_absolute_url(self):
        return reverse('zona_detail', args=[self.pk])