from django.urls import path
from . import views

app_name = 'intercambio'

urlpatterns = [
    path('crear/', views.crear_solicitud, name='crear_solicitud'),
    path('listar/', views.listar_solicitudes, name='listar_solicitudes'),
    path('detalle/<int:solicitud_id>/', views.detalle_solicitud, name='detalle_solicitud'),
    path('aceptar/<int:solicitud_id>/', views.aceptar_solicitud, name='aceptar_solicitud'),
    path('rechazar/<int:solicitud_id>/', views.rechazar_solicitud, name='rechazar_solicitud'),
]

