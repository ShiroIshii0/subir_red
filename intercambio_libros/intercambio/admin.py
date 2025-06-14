from django.contrib import admin
from .models import SolicitudIntercambio

@admin.register(SolicitudIntercambio)
class SolicitudIntercambioAdmin(admin.ModelAdmin):
    list_display = ('id', 'solicitante', 'receptor', 'libro_ofrecido', 'libro_solicitado', 'estado', 'fecha_solicitud')
    list_filter = ('estado',)
    search_fields = ('solicitante__username', 'receptor__username')
