from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    biografia = models.TextField(null=True, blank=True, verbose_name="Biografía")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción")

    def __str__(self):
        return self.categoria

class Libro(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    año_de_publicacion = models.PositiveIntegerField()
    descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción")
    
    def __str__(self):
        return f"{self.titulo} ({self.año_de_publicacion})"
