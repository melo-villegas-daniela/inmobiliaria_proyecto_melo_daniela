from django.shortcuts import get_object_or_404, render
from propiedades.models import Caracteristica

def caracteristica_list(request):
    return render(request, 'propiedades/caracteristicas/lista.html', {
        'caracteristicas': Caracteristica.objects.all(),
    })

def caracteristica_detail(request, pk):
    caracteristica = get_object_or_404(Caracteristica, pk=pk)
    return render(request, 'propiedades/caracteristicas/detalle.html', {
        'caracteristica': caracteristica,
        'propiedades': caracteristica.propiedades.all(),
    })