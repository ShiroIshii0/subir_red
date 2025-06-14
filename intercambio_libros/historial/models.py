from django.db import models
from django.contrib.auth.models import User
from intercambio.models import SolicitudIntercambio

class Historial(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='historiales')
    solicitud = models.ForeignKey(SolicitudIntercambio, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    accion = models.CharField(max_length=50, choices=[
        ('solicitud_enviada', 'Solicitud enviada'),
        ('solicitud_aceptada', 'Solicitud aceptada'),
        ('solicitud_rechazada', 'Solicitud rechazada'),
        ('libro_intercambiado', 'Libro intercambiado'),
    ])

    def __str__(self):
        return f"{self.usuario.username} - {self.accion} - {self.fecha.strftime('%Y-%m-%d')}"
