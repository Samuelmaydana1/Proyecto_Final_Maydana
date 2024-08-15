from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from AppSamuel.models import Autor, Libro, Categoria


class InicioView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '')

        # Filtrado de libros, autores y categorías basado en la consulta
        libros = Libro.objects.filter(titulo__icontains=query)
        autores = Autor.objects.filter(
            Q(nombre__icontains=query) | Q(apellido__icontains=query)
        )
        categorias = Categoria.objects.filter(categoria__icontains=query)

        # Renderiza la plantilla con los resultados
        return render(request, 'AppSamuel/index.html', {
            'query': query,
            'libros': libros,
            'autores': autores,
            'categorias': categorias
        })

class AboutView(TemplateView):
    template_name = 'AppSamuel/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra_info'] = 'Aquí puedes agregar información adicional'
        return context

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
    fields =  ["nombre", "apellido", "biografia"]

class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    template_name = "AppSamuel/autor_editar.html"
    success_url = reverse_lazy("ListaAutores")
    fields =  ["nombre", "apellido", "biografia"]

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
    fields =  ["categoria", "descripcion"]

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    template_name = "AppSamuel/categoria_editar.html"
    success_url = reverse_lazy("ListaCategorias")
    fields =  ["categoria", "descripcion"]

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
    fields =  ["titulo", "autor", "categoria", "año_de_publicacion", "descripcion"]

class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = Libro
    template_name = "AppSamuel/libro_editar.html"
    success_url = reverse_lazy("ListaLibros")
    fields =  ["titulo", "autor", "categoria", "año_de_publicacion", "descripcion"]

class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = "AppSamuel/libro_borrar.html"
    success_url = reverse_lazy("ListaLibros")
