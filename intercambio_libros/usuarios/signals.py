# usuarios/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from usuarios.models import PerfilUsuario

@receiver(post_save, sender=User)
def crear_actualizar_perfil(sender, instance, created, **kwargs):
    if created:
        # Crea el perfil con rol 'administrador' si es superusuario, sino 'usuario'
        rol = 'administrador' if instance.is_superuser else 'usuario'
        PerfilUsuario.objects.create(user=instance, rol=rol)
    else:
        # Opcional: Actualiza perfil si quieres sincronizar algo
        instance.perfilusuario.save()
