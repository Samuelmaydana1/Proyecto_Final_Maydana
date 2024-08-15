# Web "Biblioteca" en Django

## Descripción

Esta aplicación web, desarrollada con Django, permite gestionar libros, autores y categorías. Implementa el patrón MVT (Model-View-Template) y está diseñada para ser un sistema básico para agregar, buscar y listar libros, autores y categorías.

## Funcionalidades Principales

- **Autor**: Permite agregar nuevos autores, listar, editar y eliminar autores.
- **Categoría**: Permite agregar nuevas categorías, listar, editar y eliminar categorías.
- **Libro**: Permite agregar nuevos libros, listar, editar y eliminar libros, y asociarlos con autores y categorías existentes.
- **Usuarios**: Permite gestionar el inicio de sesión, registro, edición de perfil y cambio de contraseña de los usuarios.

## Requisitos

- Python 3.11.9
- Django 4.2
- Pillow 10.4.0

## Instalación

### Clona el Repositorio

```bash
git clone https://github.com/Samuelmaydana1/Proyecto_Final_Maydana.git
cd Proyecto_Final_Maydana
```

### Crea un Entorno Virtual

```bash
pip install pipenv
pipenv install
```

### Instala las Dependencias

```bash
pipenv install -r requirements.txt
```

### Configura la Base de Datos

Si estás utilizando la base de datos SQLite (por defecto), no es necesario realizar configuraciones adicionales. Si usas otra base de datos, actualiza la configuración en `Proyecto_final/settings.py`.

### Realiza las Migraciones

Primero, accede al entorno virtual creado por pipenv:

```bash
pipenv shell
```

Luego, ejecuta las migraciones:

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
  - `urls.py`: Rutas específicas de la aplicación Samuel.
- **users/**: Aplicación para la gestión de usuarios.
  - `views.py`: Vistas relacionadas con el inicio de sesión, registro, edición de perfil y cambio de contraseña.
  - **`urls.py`**: Rutas específicas para la autenticación de usuarios.

## Rutas de la Aplicación

### Rutas de Usuarios

- **Inicio de sesión**
  - **URL:** `/login/`
  - **Descripción:** Permite a los usuarios iniciar sesión en la aplicación.

- **Registro de usuario**
  - **URL:** `/register/`
  - **Descripción:** Permite a los nuevos usuarios registrarse en la aplicación.

- **Cierre de sesión**
  - **URL:** `/logout/`
  - **Descripción:** Permite a los usuarios cerrar sesión. Redirige a la página principal después del cierre.

- **Edición de perfil**
  - **URL:** `/editar_perfil/`
  - **Descripción:** Permite a los usuarios editar su perfil.

- **Confirmación de eliminación**
  - **URL:** `/confirmar_eliminacion/`
  - **Descripción:** Página para confirmar la eliminación de una cuenta.

- **Cambio de contraseña**
  - **URL:** `/cambiar_pass/`
  - **Descripción:** Permite a los usuarios cambiar su contraseña.

### Rutas de la Aplicación Samuel

- **Inicio**
  - **URL:** `/`
  - **Descripción:** Página principal de la aplicación.

- **Acerca de**
  - **URL:** `/about`
  - **Descripción:** Página que proporciona información sobre el autor.

### Rutas de Autor

- **Lista de autores**
  - **URL:** `/autor/listar`
  - **Descripción:** Muestra una lista de todos los autores.

- **Nuevo autor**
  - **URL:** `/autor/nuevo`
  - **Descripción:** Formulario para añadir un nuevo autor.

- **Detalle del autor**
  - **URL:** `/autor/<int:pk>`
  - **Descripción:** Muestra los detalles de un autor específico.

- **Editar autor**
  - **URL:** `/autor/<int:pk>/editar`
  - **Descripción:** Formulario para editar la información de un autor existente.

- **Borrar autor**
  - **URL:** `/autor/<int:pk>/borrar`
  - **Descripción:** Confirma y ejecuta la eliminación de un autor.

### Rutas de Categoría

- **Lista de categorías**
  - **URL:** `/categoria/listar`
  - **Descripción:** Muestra una lista de todas las categorías.

- **Nueva categoría**
  - **URL:** `/categoria/nuevo`
  - **Descripción:** Formulario para añadir una nueva categoría.

- **Detalle de categoría**
  - **URL:** `/categoria/<int:pk>`
  - **Descripción:** Muestra los detalles de una categoría específica.

- **Editar categoría**
  - **URL:** `/categoria/<int:pk>/editar`
  - **Descripción:** Formulario para editar una categoría existente.

- **Borrar categoría**
  - **URL:** `/categoria/<int:pk>/borrar`
  - **Descripción:** Confirma y ejecuta la eliminación de una categoría.

### Rutas de Libro

- **Lista de libros**
  - **URL:** `/libro/listar`
  - **Descripción:** Muestra una lista de todos los libros.

- **Nuevo libro**
  - **URL:** `/libro/nuevo`
  - **Descripción:** Formulario para añadir un nuevo libro.

- **Detalle del libro**
  - **URL:** `/libro/<int:pk>`
  - **Descripción:** Muestra los detalles de un libro específico.

- **Editar libro**
  - **URL:** `/libro/<int:pk>/editar`
  - **Descripción:** Formulario para editar la información de un libro existente.

- **Borrar libro**
  - **URL:** `/libro/<int:pk>/borrar`
  - **Descripción:** Confirma y ejecuta la eliminación de un libro.

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