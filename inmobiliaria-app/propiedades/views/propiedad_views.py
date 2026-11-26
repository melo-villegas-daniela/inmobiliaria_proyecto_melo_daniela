from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from propiedades.forms import PropiedadForm
from propiedades.models import Propiedad

def puede_modificar(user, propiedad):
    if not user.is_authenticated:
        return False
    es_admin = user.is_superuser or user.groups.filter(name='administradores').exists()
    return es_admin or propiedad.creado_por_id == user.id

def propiedad_list(request):
    propiedades = Propiedad.objects.select_related('zona')
    return render(request, 'propiedades/propiedades/lista.html', {'propiedades': propiedades})

def propiedad_detail(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    return render(request, 'propiedades/propiedades/detalle.html', {
        'propiedad': propiedad,
        'puede_modificar': puede_modificar(request.user, propiedad),
    })

@login_required
@permission_required('propiedades.add_propiedad', raise_exception=True)
def propiedad_create(request):
    if request.method == 'POST':
        form = PropiedadForm(request.POST)
        if form.is_valid():
            propiedad = form.save(commit=False)
            propiedad.creado_por = request.user
            propiedad.save()
            form.save_m2m() 
            messages.success(request, 'Propiedad creada exitosamente')
            return redirect(propiedad)
    else:
        form = PropiedadForm()
    return render(request, 'propiedades/propiedades/formulario.html', {'form': form, 'titulo': 'Nueva propiedad'})

@login_required
@permission_required('propiedades.change_propiedad', raise_exception=True)
def propiedad_update(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    if not puede_modificar(request.user, propiedad):
        raise PermissionDenied
    if request.method == 'POST':
        form = PropiedadForm(request.POST, instance=propiedad)
        if form.is_valid():
            form.save()
            messages.success(request, 'Propiedad actualizada exitosamente')
            return redirect(propiedad)
    else:
        form = PropiedadForm(instance=propiedad)
    return render(request, 'propiedades/propiedades/formulario.html', {'form': form, 'titulo': 'Editar propiedad'})

@login_required
@permission_required('propiedades.delete_propiedad', raise_exception=True)
def propiedad_delete(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    if not puede_modificar(request.user, propiedad):
        raise PermissionDenied
    if request.method == 'POST':
        propiedad.delete()
        messages.success(request, 'Propiedad eliminada exitosamente')
        return redirect('propiedad_list')
    return render(request, 'propiedades/propiedades/confirmar_eliminar.html', {'propiedad': propiedad})