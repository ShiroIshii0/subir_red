from django.db import models
from django.contrib.auth.models import User

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
    propietario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='libros')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
