from django.db import models
from django.urls import reverse

class Caracteristica(models.Model):
    nombre = models.CharField(max_length=60, unique=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'nombre'
        verbose_name_plural = 'nombres'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('caracteristica_detail', args=[self.pk])