from django.contrib import admin
from django.urls import path, include
from usuarios import views as usuarios_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', usuarios_views.home, name='home'),  
    path('usuarios/', include('usuarios.urls')),
    path('libros/', include('libros.urls')),
    path('intercambio/', include(('intercambio.urls', 'intercambio'), namespace='intercambio')),
    path('historial/', include(('historial.urls', 'historial'), namespace='historial')),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
