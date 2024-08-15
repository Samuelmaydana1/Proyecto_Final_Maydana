from django import forms
from AppSamuel.models import Autor, Categoria, Libro

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
        fields = ['titulo', 'autor', 'categoria', 'año_de_publicacion', 'descripcion', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'año_de_publicacion': forms.NumberInput(attrs={'max': 2099}),
            'imagen': forms.ClearableFileInput(attrs={'multiple': False}),
        }

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if imagen:
            max_size_mb = 5
            if imagen.size > max_size_mb * 1024 * 1024:
                raise forms.ValidationError(f"El tamaño del archivo no puede superar los {max_size_mb} MB.")
            
            valid_extensions = ['.jpg', '.jpeg', '.png']
            extension = imagen.name.split('.')[-1].lower()
            if f".{extension}" not in valid_extensions:
                raise forms.ValidationError("Solo se permiten archivos JPEG y PNG.")
        
        return imagen

class BuscarLibroForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)