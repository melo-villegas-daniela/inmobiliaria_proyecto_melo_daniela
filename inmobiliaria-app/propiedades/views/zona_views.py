from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from propiedades.forms import ZonaForm
from propiedades.models import Zona

def zona_list(request):
    zonas = Zona.objects.all()
    return render(request, 'propiedades/zonas/lista.html', {'zonas': zonas})

def zona_detail(request, pk):
    zona = get_object_or_404(Zona, pk=pk)
    return render(request, 'propiedades/zonas/detalle.html', {
        'zona': zona,
        'propiedades': zona.propiedades.all(),
    })

@login_required
@permission_required('propiedades.add_zona', raise_exception=True)
def zona_create(request):
    if request.method == 'POST':
        form = ZonaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Zona creada exitosamente')
            return redirect('zona_list')
    else:
        form = ZonaForm()
    return render(request, 'propiedades/zonas/formulario.html', {'form': form, 'titulo': 'Nueva zona'})

@login_required
@permission_required('propiedades.change_zona', raise_exception=True)
def zona_update(request, pk):
    zona = get_object_or_404(Zona, pk=pk)
    if request.method == 'POST':
        form = ZonaForm(request.POST, instance=zona)
        if form.is_valid():
            form.save()
            messages.success(request, 'Zona actualizada exitosamente')
            return redirect(zona)
    else:
        form = ZonaForm(instance=zona)
    return render(request, 'propiedades/zonas/formulario.html', {'form': form, 'titulo': 'Editar zona'})

@login_required
@permission_required('propiedades.delete_zona', raise_exception=True)
def zona_delete(request, pk):
    zona = get_object_or_404(Zona, pk=pk)
    if request.method == 'POST':
        try:
            zona.delete()
            messages.success(request, 'Zona eliminada exitosamente')
            return redirect('zona_list')
        except ProtectedError:
            messages.error(request, 'No se puede eliminar: la zona tiene propiedades asociadas.')
            return redirect(zona)
    return render(request, 'propiedades/zonas/confirmar_eliminar.html', {'zona': zona})