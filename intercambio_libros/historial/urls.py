from django.urls import path
from . import views

app_name = 'historial'

urlpatterns = [
    path('', views.listar_historial, name='listar_historial'),
]

