from django.db import models
from django.contrib.auth.models import User
from libros.models import Libro

class SolicitudIntercambio(models.Model):
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitudes_enviadas')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitudes_recibidas')
    libro_ofrecido = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='intercambios_ofrecidos')
    libro_solicitado = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='intercambios_solicitados')
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('aceptado', 'Aceptado'),
        ('rechazado', 'Rechazado')
    ], default='pendiente')
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud de {self.solicitante.username} a {self.receptor.username}"
