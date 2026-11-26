# Sistema de Gestión Inmobiliaria

Aplicación web desarrollada con **Python y Django** para administrar información de propiedades inmobiliarias. El proyecto permite consultar propiedades, zonas, características y visitas, además de gestionar usuarios y permisos.

## Tecnologías

- Python
- Django 6.1.3
- PostgreSQL
- Psycopg 3
- python-dotenv
- HTML y CSS

Las dependencias de Python están especificadas en `inmobiliaria-app/requirements.txt`.

## Estructura del repositorio

La estructura siguiente corresponde a los archivos incluidos en este repositorio:

```text
inmobiliaria_proyecto_melo_daniela/
├── .gitignore
└── inmobiliaria-app/
    ├── cargar_datos.py
    ├── crear_grupos.py
    ├── manage.py
    ├── requirements.txt
    ├── config/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── propiedades/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── tests.py
        ├── forms/
        │   ├── __init__.py
        │   ├── caracteristica_form.py
        │   ├── propiedad_form.py
        │   ├── registro_form.py
        │   ├── visita_form.py
        │   └── zona_form.py
        ├── migrations/
        │   ├── __init__.py
        │   └── 0001_initial.py
        ├── models/
        │   ├── __init__.py
        │   ├── caracteristica.py
        │   ├── propiedad.py
        │   ├── visita.py
        │   └── zona.py
        ├── static/
        │   └── propiedades/
        │       └── css/
        │           └── estilos.css
        ├── templates/
        │   ├── 403.html
        │   └── propiedades/
        │       ├── base.html
        │       ├── auth/
        │       │   ├── login.html
        │       │   └── registro.html
        │       ├── caracteristicas/
        │       │   ├── detalle.html
        │       │   └── lista.html
        │       ├── propiedades/
        │       │   ├── confirmar_eliminar.html
        │       │   ├── detalle.html
        │       │   ├── formulario.html
        │       │   └── lista.html
        │       ├── visitas/
        │       │   ├── detalle.html
        │       │   └── lista.html
        │       └── zonas/
        │           ├── confirmar_eliminar.html
        │           ├── detalle.html
        │           ├── formulario.html
        │           └── lista.html
        ├── urls/
        │   ├── __init__.py
        │   ├── auth_urls.py
        │   ├── caracteristica_urls.py
        │   ├── propiedad_urls.py
        │   ├── visita_urls.py
        │   └── zona_urls.py
        └── views/
            ├── __init__.py
            ├── auth_views.py
            ├── caracteristica_views.py
            ├── propiedad_views.py
            ├── visita_views.py
            └── zona_views.py
```

## Funcionalidades

### Gestión de propiedades

- Listar y consultar el detalle de las propiedades.
- Registrar, editar y eliminar propiedades, de acuerdo con los permisos del usuario.
- Clasificar las propiedades por tipo: casa, departamento, terreno o local comercial.
- Registrar la operación como venta o arriendo.
- Manejar los estados disponible, reservada y vendida o arrendada.
- Asociar una propiedad con una zona y con una o varias características.
- Registrar precio, fecha de publicación y descripción.
- Validar que el precio sea mayor que cero.

### Zonas y características

- Consultar el listado y el detalle de zonas.
- Crear, editar y eliminar zonas según los permisos.
- Consultar las características disponibles.
- Asociar características a las propiedades.
- Evitar la eliminación de una zona que tenga propiedades relacionadas.

### Visitas

- Consultar el listado y el detalle de visitas.
- Consultar visitas asociadas a una propiedad.
- Visualizar el nombre de la persona interesada, la fecha y el estado de la visita.

Los estados definidos para una visita son: pendiente, realizada y cancelada.

### Usuarios y permisos

- Registro de usuarios.
- Inicio y cierre de sesión.
- Uso de los permisos de Django para restringir operaciones.
- Separación de permisos mediante los grupos `administradores` y `consultores`.
- Los usuarios administradores o los creadores de una propiedad pueden modificar o eliminar esa propiedad, siempre que también cuenten con el permiso correspondiente.

### Panel de administración

Django Admin está habilitado para administrar los modelos `Zona`, `Caracteristica`, `Propiedad` y `Visita`.

## Requisitos previos

Antes de ejecutar el proyecto, instala o configura:

- Python 3.12 o superior (según los requisitos de Django 6.1).
- PostgreSQL.
- `pip`.
- Un entorno virtual de Python.

## Instalación y configuración

Los comandos de esta sección se ejecutan desde la carpeta `inmobiliaria-app`.

### 1. Clonar el repositorio

```bash
git clone https://github.com/melo-villegas-daniela/inmobiliaria_proyecto_melo_daniela.git
cd inmobiliaria_proyecto_melo_daniela/inmobiliaria-app
```

### 2. Crear y activar un entorno virtual

En Linux o macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

En Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Crear la base de datos PostgreSQL

Crea una base de datos en PostgreSQL. Por ejemplo, puedes llamarla `inmobiliaria_db`.

En una consola de PostgreSQL, un ejemplo de creación sería:

```sql
CREATE DATABASE inmobiliaria_db;
```

Utiliza el nombre, usuario, contraseña, host y puerto correspondientes a tu instalación.

### 5. Configurar las variables de entorno

El archivo `config/settings.py` carga un archivo `.env` ubicado en la carpeta `inmobiliaria-app` y obtiene de él los datos de conexión a PostgreSQL.

Crea `inmobiliaria-app/.env` con este contenido de ejemplo y reemplaza los valores por los de tu entorno:

```dotenv
DB_NAME=inmobiliaria_db
DB_USER=tu_usuario_postgres
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
```

El repositorio no incluye un archivo `.env.example`; el archivo `.env` está excluido por el `.gitignore`. No publiques contraseñas ni otros datos privados.

### 6. Aplicar las migraciones

```bash
python manage.py migrate
```

### 7. Cargar los datos de prueba

El script `cargar_datos.py` crea usuarios de demostración, zonas, características, propiedades y visitas de ejemplo.

```bash
python manage.py shell < cargar_datos.py
```

### 8. Crear los grupos y asignar permisos

Después de cargar los usuarios, ejecuta:

```bash
python manage.py shell < crear_grupos.py
```

Este script crea los grupos `administradores` y `consultores`, asigna permisos de la aplicación y agrega a los usuarios existentes `administrador1`, `consultor1` y `consultor2` a sus respectivos grupos.

### 9. Iniciar el servidor

```bash
python manage.py runserver
```

Abre en el navegador:

- Aplicación: http://127.0.0.1:8000/
- Administración de Django: http://127.0.0.1:8000/admin/

## Rutas principales

| Ruta | Descripción |
|---|---|
| `/` | Listado de propiedades |
| `/propiedades/nueva/` | Crear una propiedad |
| `/propiedades/<id>/` | Detalle de una propiedad |
| `/propiedades/<id>/editar/` | Editar una propiedad |
| `/propiedades/<id>/eliminar/` | Eliminar una propiedad |
| `/zonas/` | Listado de zonas |
| `/zonas/nueva/` | Crear una zona |
| `/caracteristicas/` | Listado de características |
| `/visitas/` | Listado de visitas |
| `/registro/` | Registro de usuario |
| `/login/` | Inicio de sesión |
| `/logout/` | Cierre de sesión |
| `/admin/` | Panel de administración |

Las rutas de edición, creación y eliminación requieren autenticación y los permisos definidos en Django.

## Modelos de datos

- **Zona:** almacena el nombre, la ciudad y una descripción opcional.
- **Caracteristica:** registra nombres de características que pueden asociarse a varias propiedades.
- **Propiedad:** almacena título, tipo, operación, estado, precio, fecha de publicación y descripción. Se relaciona con una zona, varias características y el usuario que la creó.
- **Visita:** registra la propiedad visitada, el nombre de la persona interesada, la fecha, el estado y el usuario que creó el registro.

## Scripts incluidos

| Archivo | Propósito |
|---|---|
| `cargar_datos.py` | Crear usuarios y registros de ejemplo para probar la aplicación. |
| `crear_grupos.py` | Crear los grupos de usuarios y asignar permisos. |

Los scripts se ejecutan mediante `manage.py shell`, después de aplicar las migraciones. Ejecuta primero `cargar_datos.py` y luego `crear_grupos.py`.

## Pruebas

El archivo `propiedades/tests.py` está incluido en el proyecto, pero actualmente contiene únicamente la plantilla inicial de Django; no hay casos de prueba implementados allí.

## Consideraciones de seguridad

- `config/settings.py` contiene actualmente una `SECRET_KEY` de desarrollo escrita directamente en el archivo y `DEBUG = True`. Antes de desplegar el proyecto, configura una clave secreta privada mediante variables de entorno, desactiva `DEBUG` y define `ALLOWED_HOSTS`.
- `cargar_datos.py` incluye contraseñas fijas para cuentas de demostración. Son únicamente para pruebas locales: cámbialas o elimina esas cuentas antes de usar el sistema en un entorno real.
- No subas el archivo `.env` al repositorio.

## Autora

**Daniela Alejandra Melo Villegas**
