from datetime import date, timedelta
from decimal import Decimal
from django.contrib.auth.models import User
from propiedades.models import Zona, Caracteristica, Propiedad, Visita

usuarios = {}
for username, password, es_super in [
    ('admin', 'admin', True),
    ('administrador1', 'Admin12345', False),
    ('consultor1', 'Consul12345', False),
    ('consultor2', 'Consul12345', False),
]:
    user, creado = User.objects.get_or_create(
        username=username, defaults={'email': f'{username}@inmobiliaria.test'}
    )
    if creado:
        user.set_password(password)
        user.is_staff = es_super
        user.is_superuser = es_super
        user.save()
    usuarios[username] = user

zonas = []
for nombre, ciudad in [
    ('La Carolina', 'Quito'), ('Cumbayá', 'Quito'), ('Centro Histórico', 'Quito'),
    ('Samborondón', 'Guayaquil'), ('Urdesa', 'Guayaquil'),
]:
    zona, _ = Zona.objects.get_or_create(nombre=nombre, ciudad=ciudad)
    zonas.append(zona)

caracs = {}
for nombre in ['Piscina', 'Garaje', 'Ascensor', 'Jardín', 'Seguridad 24h']:
    caracs[nombre], _ = Caracteristica.objects.get_or_create(nombre=nombre)

datos = [
    ('Departamento moderno en La Carolina', 'departamento', 'venta', '125000.00', 0, ['Ascensor', 'Garaje'], 'administrador1'),
    ('Casa familiar en Cumbayá', 'casa', 'venta', '240000.00', 1, ['Jardín', 'Garaje', 'Seguridad 24h'], 'administrador1'),
    ('Local comercial en el Centro', 'local', 'arriendo', '1200.00', 2, ['Seguridad 24h'], 'consultor1'),
    ('Terreno en Samborondón', 'terreno', 'venta', '90000.00', 3, ['Jardín'], 'consultor1'),
    ('Departamento amoblado en Urdesa', 'departamento', 'arriendo', '650.00', 4, ['Ascensor', 'Piscina'], 'consultor2'),
]
propiedades = []
for titulo, tipo, operacion, precio, z, nombres, autor in datos:
    prop, _ = Propiedad.objects.get_or_create(
        titulo=titulo,
        defaults={
            'tipo': tipo, 'operacion': operacion, 'precio': Decimal(precio),
            'zona': zonas[z], 'creado_por': usuarios[autor],
            'descripcion': 'Propiedad de ejemplo para pruebas.',
        },
    )
    prop.caracteristicas.set([caracs[n] for n in nombres])
    propiedades.append(prop)

for i, interesado in enumerate(['Ana Pérez', 'Luis Mora', 'Carla Ruiz', 'Diego Vega', 'Sofía León']):
    Visita.objects.get_or_create(
        propiedad=propiedades[i], nombre_interesado=interesado,
        defaults={'fecha': date.today() + timedelta(days=i + 1), 'creado_por': usuarios['admin']},
    )

print('Datos de prueba cargados.')