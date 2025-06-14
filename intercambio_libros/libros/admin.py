from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'propietario', 'disponible', 'fecha_creacion')
    list_filter = ('disponible', 'autor')
    search_fields = ('titulo', 'autor', 'descripcion')
    readonly_fields = ('fecha_creacion',)

    fieldsets = (
        (None, {
            'fields': ('titulo', 'autor', 'descripcion', 'portada', 'disponible')
        }),
        ('Propietario y fechas', {
            'fields': ('propietario', 'fecha_creacion'),
            'classes': ('collapse',)
        }),
    )
