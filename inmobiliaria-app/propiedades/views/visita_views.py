from django.shortcuts import get_object_or_404, render
from propiedades.models import Visita

def visita_list(request):
    visitas = Visita.objects.select_related('propiedad')
    return render(request, 'propiedades/visitas/lista.html', {'visitas': visitas})

def visita_detail(request, pk):
    visita = get_object_or_404(Visita, pk=pk)
    return render(request, 'propiedades/visitas/detalle.html', {'visita': visita})