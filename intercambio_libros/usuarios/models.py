from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class PerfilUsuario(models.Model):
    ROL_CHOICES = [
        ('administrador', 'Administrador'),
        ('usuario', 'Usuario'),
        ('moderador', 'Moderador'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='usuario')
    telefono = models.CharField("Teléfono", max_length=20, blank=True, null=True)
    direccion = models.CharField("Dirección", max_length=255, blank=True, null=True)
    ciudad = models.CharField("Ciudad", max_length=100, blank=True, null=True)
    pais = models.CharField("País", max_length=100, blank=True, null=True)
    reputacion = models.IntegerField("Reputación", default=0)
    fecha_registro = models.DateTimeField("Fecha de registro", auto_now_add=True)
    avatar = models.ImageField("Foto de perfil", upload_to='avatars/', blank=True, null=True)

    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuarios'

    def __str__(self):
        return f"{self.usuario.username} - {self.get_rol_display()}"

    def es_administrador(self):
        return self.rol == 'administrador'

    def es_usuario(self):
        return self.rol == 'usuario'

    def es_moderador(self):
        return self.rol == 'moderador'


# Señales fuera de la clase
@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        rol = 'administrador' if instance.is_superuser else 'usuario'
        PerfilUsuario.objects.create(usuario=instance, rol=rol)

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    if hasattr(instance, 'perfil'):
        instance.perfil.save()
