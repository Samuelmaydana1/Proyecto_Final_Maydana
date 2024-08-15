from django import forms
from AppSamuel.models import Autor, Categoria, Libro
from datetime import datetime

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'biografia']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria', 'descripcion']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'categoria', 'año_de_publicacion', 'descripcion']
        widgets = {
            'año_de_publicacion': forms.NumberInput(attrs={'max': datetime.now().year}),
        }

class BuscarLibroForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)