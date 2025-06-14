from django.urls import path
from . import views 

app_name = 'libros'
urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('publico/', views.lista_libros_publico, name='lista_libros_publico'),
    path('crear/', views.crear_libro, name='crear_libro'),
    path('editar/<int:pk>/', views.editar_libro, name='editar_libro'),
    path('eliminar/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),
]
