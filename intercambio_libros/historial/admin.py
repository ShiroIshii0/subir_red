from django.contrib import admin
from .models import Historial

@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'accion', 'fecha', 'solicitud')
    list_filter = ('accion', 'fecha', 'usuario')
    search_fields = ('usuario__username', 'accion', 'solicitud__id')
