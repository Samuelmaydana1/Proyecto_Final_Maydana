from django.db import models
from django.core.validators import MaxValueValidator

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    biografia = models.TextField(null=True, blank=True, verbose_name="Biografía")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Categoria(models.Model):
    categoria = models.CharField(max_length=100, verbose_name="Categoría")
    descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción")

    def __str__(self):
        return self.categoria

class Libro(models.Model):
    titulo = models.CharField(max_length=200, verbose_name=("Título"))
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE, null=True, blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, null=True, blank=True)
    año_de_publicacion = models.PositiveIntegerField(validators=[MaxValueValidator(2099)], verbose_name=("Año de publicación"))
    descripcion = models.TextField(null=True, blank=True, verbose_name=("Descripción"))
    imagen = models.ImageField(upload_to='libros/', null=True, blank=True, verbose_name=("Imagen"))

    def __str__(self):
        return f"{self.titulo} ({self.año_de_publicacion})"

    def delete(self, *args, **kwargs):
        if self.imagen:
            self.imagen.delete(save=False)
        super().delete(*args, **kwargs)