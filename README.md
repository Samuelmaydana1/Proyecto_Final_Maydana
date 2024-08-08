# Web "Biblioteca" en Django

## Descripción

Esta aplicación web, desarrollada con Django, permite gestionar libros, autores y categorías. Implementa el patrón MVT (Model-View-Template) y está diseñada para ser un sistema básico para agregar, buscar y listar libros, autores y categorías.

## Funcionalidades

- **Autor**: Permite agregar nuevos autores a la base de datos.
- **Categoría**: Permite agregar nuevas categorías para clasificar libros.
- **Libro**: Permite agregar libros, asociándolos con un autor y una categoría.
- **Buscar Libros**: Permite buscar libros en la base de datos por título, autor o categoría.

## Requisitos

- Python 3.11.9
- Django 4.2

## Instalación

### Clona el Repositorio

```bash
git clone https://github.com/Samuelmaydana1/Proyecto_Final_Maydana.git
cd Proyecto_Final_Maydana
```

### Crea un Entorno Virtual

```bash
python -m venv env
source env/bin/activate  # En Windows, usa `env\Scripts\activate`
```

### Instala las Dependencias

```bash
pip install -r requirements.txt
```

### Configura la Base de Datos

Si estás utilizando la base de datos SQLite (por defecto), no es necesario realizar configuraciones adicionales. Si usas otra base de datos, actualiza la configuración en `Proyecto_final/settings.py`.

### Realiza las Migraciones

```bash
python manage.py migrate
```

### Crea un Superusuario (Opcional)

Para acceder al panel de administración de Django, crea un superusuario con el siguiente comando:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para ingresar el nombre de usuario, correo electrónico y contraseña.

### Ejecuta el Servidor de Desarrollo

```bash
python manage.py runserver
```

Abre tu navegador y visita [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para ver la aplicación en funcionamiento.

## Uso

### Funcionalidades Principales

- **Buscar Libros**: Navega a [http://127.0.0.1:8000/](http://127.0.0.1:8000/) y usa el formulario para buscar libros por título, autor o categoría.
- **Autor**: Navega a [http://127.0.0.1:8000/autor/nuevo/](http://127.0.0.1:8000/autor/nuevo/) y completa el formulario para agregar un nuevo autor.
- **Categoría**: Navega a [http://127.0.0.1:8000/categoria/nuevo/](http://127.0.0.1:8000/categoria/nuevo/) y completa el formulario para agregar una nueva categoría.
- **Libro**: Navega a [http://127.0.0.1:8000/libro/nuevo/](http://127.0.0.1:8000/libro/nuevo/) y completa el formulario para agregar un nuevo libro, seleccionando un autor y una categoría previamente agregados.

## Estructura del Proyecto

- **Proyecto_final/**: Directorio del proyecto principal.
  - `settings.py`: Configuración del proyecto Django.
  - `urls.py`: Rutas del proyecto.
  - `wsgi.py`: Punto de entrada WSGI para servidores de aplicaciones.
- **AppSamuel/**: Aplicación dentro del proyecto.
  - `models.py`: Definición de los modelos (Autor, Categoría, Libro).
  - `views.py`: Definición de las vistas (funcionalidades).
  - `forms.py`: Formularios para la entrada de datos.
  - **`templates/`**: Plantillas HTML.
  - `urls.py`: Rutas específicas de la aplicación.
- **users/**: Aplicación para la gestión de usuarios.
  - `views.py`: Vistas relacionadas con el inicio de sesión, registro y cierre de sesión.
  - **`urls.py`**: Rutas específicas para la autenticación de usuarios.

## Contribución

Si deseas contribuir al proyecto, por favor sigue estos pasos:

1. Haz un Fork del Repositorio.
2. Crea una Nueva Rama.
3. Realiza tus Cambios.
4. Envía un Pull Request.

Asegúrate de seguir el estilo de código y de agregar pruebas para cualquier nueva funcionalidad.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Puedes usar, modificar y distribuir este software bajo los términos de esta licencia.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme:

- **Nombre**: Samuel Maydana
- **Email**: [samuelmaydana1@gmail.com](mailto:samuelmaydana1@gmail.com)
- **GitHub**: [https://github.com/Samuelmaydana1](https://github.com/Samuelmaydana1)