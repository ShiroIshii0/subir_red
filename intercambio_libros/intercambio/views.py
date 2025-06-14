from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SolicitudIntercambio
from libros.models import Libro
from historial.models import Historial  # 👈 Importa el historial

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

        # Crear historial
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

def listar_solicitudes(request):
    solicitudes = SolicitudIntercambio.objects.all()
    return render(request, 'intercambio/listar_solicitudes.html', {'solicitudes': solicitudes})

@login_required
def detalle_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudIntercambio, id=solicitud_id)
    return render(request, 'intercambio/detalle_solicitud.html', {'solicitud': solicitud})

@login_required
def aceptar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudIntercambio, id=solicitud_id)
    if solicitud.estado == 'pendiente':
        solicitud.estado = 'aceptado'
        solicitud.save()

        # Crear historial
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
    if solicitud.estado == 'pendiente':
        solicitud.estado = 'rechazado'
        solicitud.save()

        # Crear historial
        Historial.objects.create(
            usuario=request.user,
            solicitud=solicitud,
            accion='solicitud_rechazada'
        )

        messages.success(request, '¡Solicitud rechazada!')

    return redirect('intercambio:listar_solicitudes')


