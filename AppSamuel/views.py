from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from AppSamuel.models import Autor, Libro, Categoria


def inicio(request):
    query = request.GET.get('query', '')
    libros = Libro.objects.filter(titulo__icontains=query)
    autores = Autor.objects.filter(
    Q(nombre__icontains=query) | Q(apellido__icontains=query))
    categorias = Categoria.objects.filter(categoria__icontains=query)
    

    return render(request, 'AppSamuel/index.html', {
        'query': query,
        'libros': libros,
        'autores': autores,
        'categorias': categorias
        
    })

def about(request):
    return render(request, 'AppSamuel/about.html')

# Vistas basadas en Clases - Autor
class AutorListView(LoginRequiredMixin, ListView):
    model = Autor
    context_object_name = "autores"
    template_name = "AppSamuel/autor_lista.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class AutorDetailView(LoginRequiredMixin, DetailView):
    model = Autor
    template_name = "AppSamuel/autor_detalle.html"
class AutorCreateView(LoginRequiredMixin, CreateView):
    model = Autor
    template_name = "AppSamuel/autor_crear.html"
    success_url = reverse_lazy("ListaAutores")
    fields =  ["nombre", "apellido"]

class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    template_name = "AppSamuel/autor_editar.html"
    success_url = reverse_lazy("ListaAutores")
    fields =  ["nombre", "apellido"]

class AutorDeleteView(LoginRequiredMixin, DeleteView):
    model = Autor
    template_name = "AppSamuel/autor_borrar.html"
    success_url = reverse_lazy("ListaAutores")

# Vistas basadas en Clases - Categoria
class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    context_object_name = "categorias"
    template_name = "AppSamuel/categoria_lista.html"

class CategoriaDetailView(LoginRequiredMixin, DetailView):
    model = Categoria
    template_name = "AppSamuel/categoria_detalle.html"

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = "AppSamuel/categoria_crear.html"
    success_url = reverse_lazy("ListaCategorias")
    fields =  ["categoria"]

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    template_name = "AppSamuel/categoria_editar.html"
    success_url = reverse_lazy("ListaCategorias")
    fields =  ["categoria"]

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = "AppSamuel/categoria_borrar.html"
    success_url = reverse_lazy("ListaCategorias")

# Vistas basadas en Clases - Libro
class LibroListView(LoginRequiredMixin, ListView):
    model = Libro
    context_object_name = "libros"
    template_name = "AppSamuel/libro_lista.html"

class LibroDetailView(LoginRequiredMixin, DetailView):
    model = Libro
    template_name = "AppSamuel/libro_detalle.html"

class LibroCreateView(LoginRequiredMixin, CreateView):
    model = Libro
    template_name = "AppSamuel/libro_crear.html"
    success_url = reverse_lazy("ListaLibros")
    fields =  ["titulo", "autor", "categoria", "año_de_publicacion"]

class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = Libro
    template_name = "AppSamuel/libro_editar.html"
    success_url = reverse_lazy("ListaLibros")
    fields =  ["titulo", "autor", "categoria", "año_de_publicacion"]

class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = "AppSamuel/libro_borrar.html"
    success_url = reverse_lazy("ListaLibros")
