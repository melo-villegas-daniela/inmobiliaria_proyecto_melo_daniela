from django.contrib.auth.models import Group, Permission, User

permisos = Permission.objects.filter(content_type__app_label='propiedades')

administradores, _ = Group.objects.get_or_create(name='administradores')
administradores.permissions.set(permisos)

consultores, _ = Group.objects.get_or_create(name='consultores')
consultores.permissions.set(
    permisos.filter(codename__startswith='view')
    | permisos.filter(codename__in=['add_propiedad', 'change_propiedad', 'delete_propiedad'])
)

asignaciones = [
    ('administrador1', administradores),
    ('consultor1', consultores),
    ('consultor2', consultores),
]
for username, grupo in asignaciones:
    usuario = User.objects.filter(username=username).first()
    if usuario:
        usuario.groups.add(grupo)

print('Grupos y permisos creados.')