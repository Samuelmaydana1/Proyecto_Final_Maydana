from django.urls import path
from AppSamuel import views

urlpatterns = [
    path('', views.InicioView.as_view(), name='Inicio' ),
    path('about', views.AboutView.as_view(), name='About'),
]

# Autor
urlpatterns += [
    path('autor/listar', views.AutorListView.as_view(), name='ListaAutores'),
    path('autor/nuevo',views.AutorCreateView.as_view(), name='NuevoAutor'),
    path('autor/<int:pk>',views.AutorDetailView.as_view(), name='DetalleAutor'),
    path('autor/<int:pk>/editar',views.AutorUpdateView.as_view(), name='EditarAutor'),
    path('autor/<int:pk>/borrar',views.AutorDeleteView.as_view(), name='BorrarAutor')
]

# Categoría
urlpatterns += [
    path('categoria/listar', views.CategoriaListView.as_view(), name='ListaCategorias'),
    path('categoria/nuevo',views.CategoriaCreateView.as_view(), name='NuevaCategoria'),
    path('categoria/<int:pk>',views.CategoriaDetailView.as_view(), name='DetalleCategoria'),
    path('categoria/<int:pk>/editar',views.CategoriaUpdateView.as_view(), name='EditarCategoria'),
    path('categoria/<int:pk>/borrar',views.CategoriaDeleteView.as_view(), name='BorrarCategoria')
]

# Libro
urlpatterns += [
    path('libro/listar', views.LibroListView.as_view(), name='ListaLibros'),
    path('libro/nuevo',views.LibroCreateView.as_view(), name='NuevoLibro'),
    path('libro/<int:pk>',views.LibroDetailView.as_view(), name='DetalleLibro'),
    path('libro/<int:pk>/editar',views.LibroUpdateView.as_view(), name='EditarLibro'),
    path('libro/<int:pk>/borrar',views.LibroDeleteView.as_view(), name='BorrarLibro')
]