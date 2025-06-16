from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import SolicitudIntercambio
from libros.models import Libro
from historial.models import Historial

@login_required
def crear_solicitud(request):
    if request.method == 'POST':
        libro_ofrecido_id = request.POST.get('libro_ofrecido')
        libro_solicitado_id = request.POST.get('libro_solicitado')
        libro_ofrecido = get_object_or_404(Libro, id=libro_ofrecido_id)
        libro_solicitado = get_object_or_404(Libro, id=libro_solicitado_id)

        solicitud = SolicitudIntercambio.objects.create(
            solicitante=request.user,
            receptor=libro_solicitado.propietario,
            libro_ofrecido=libro_ofrecido,
            libro_solicitado=libro_solicitado
        )

        Historial.objects.create(
            usuario=request.user,
            solicitud=solicitud,
            accion='solicitud_enviada'
        )

        messages.success(request, '¡Solicitud enviada con éxito!')
        return redirect('intercambio:listar_solicitudes')
    
    libros_disponibles = Libro.objects.filter(disponible=True).exclude(propietario=request.user)
    mis_libros = Libro.objects.filter(propietario=request.user)
    return render(request, 'intercambio/crear_solicitud.html', {
        'libros_disponibles': libros_disponibles,
        'mis_libros': mis_libros
    })

@login_required
def listar_solicitudes(request):
    # Ver solo solicitudes del usuario (opcional, según lógica)
    solicitudes = SolicitudIntercambio.objects.filter(receptor=request.user) | SolicitudIntercambio.objects.filter(solicitante=request.user)
    return render(request, 'intercambio/listar_solicitudes.html', {'solicitudes': solicitudes})

def detalle_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudIntercambio, id=solicitud_id)
    if request.user != solicitud.solicitante and request.user != solicitud.receptor:
        messages.warning(request, "No tienes permiso para ver los detalles de esta solicitud.")
        return redirect('intercambio:listar_solicitudes')

    return render(request, 'intercambio/detalle_solicitud.html', {'solicitud': solicitud})
@login_required
def aceptar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudIntercambio, id=solicitud_id)

    # Solo el receptor puede aceptar
    if solicitud.receptor != request.user:
        messages.warning(request, "No tienes permiso para aceptar esta solicitud.")
        return redirect('intercambio:listar_solicitudes')

    if solicitud.estado == 'pendiente':
        solicitud.estado = 'aceptado'
        solicitud.save()

        Historial.objects.create(
            usuario=request.user,
            solicitud=solicitud,
            accion='solicitud_aceptada'
        )
        messages.success(request, '¡Solicitud aceptada!')

    return redirect('intercambio:listar_solicitudes')


@login_required
def rechazar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudIntercambio, id=solicitud_id)

    # Solo el receptor puede rechazar
    if solicitud.receptor != request.user:
        messages.warning(request, "No tienes permiso para rechazar esta solicitud.")
        return redirect('intercambio:listar_solicitudes')

    if solicitud.estado == 'pendiente':
        solicitud.estado = 'rechazado'
        solicitud.save()

        Historial.objects.create(
            usuario=request.user,
            solicitud=solicitud,
            accion='solicitud_rechazada'
        )
        messages.success(request, '¡Solicitud rechazada!')

    return redirect('intercambio:listar_solicitudes')
