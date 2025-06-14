from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import PerfilUsuario

# Inline para mostrar y editar el perfil de usuario directamente desde el formulario de usuario.
class PerfilUsuarioInline(admin.StackedInline):
    model = PerfilUsuario
    can_delete = False
    verbose_name_plural = 'Perfil de Usuario'
    fk_name = 'usuario'

# Extendemos el UserAdmin para incluir el PerfilUsuario.
class UserAdmin(BaseUserAdmin):
    inlines = (PerfilUsuarioInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'mostrar_rol', 'reputacion')
    list_select_related = ('perfil',)

    def mostrar_rol(self, instance):
        return instance.perfil.get_rol_display() if hasattr(instance, 'perfil') else 'No asignado'
    mostrar_rol.short_description = 'Rol'

    def reputacion(self, instance):
        return instance.perfil.reputacion if hasattr(instance, 'perfil') else 'N/A'
    reputacion.short_description = 'Reputación'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super(UserAdmin, self).get_inline_instances(request, obj)

# Desregistramos el UserAdmin original y registramos el
admin.site.unregister(User)
admin.site.register(User, UserAdmin)