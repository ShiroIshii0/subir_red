from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Libro
from .forms import LibroForm  # Necesitaremos este formulario más abajo

#lista de libros publicos
def lista_libros_publico(request):
    libros = Libro.objects.filter(disponible=True)
    return render(request, 'libros/lista_libros_publico.html', {'libros': libros})


@login_required
def lista_libros(request):
    libros = Libro.objects.filter(propietario=request.user)
    return render(request, 'libros/lista_libros.html', {'libros': libros})

#crear un libro
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LibroForm, TelefonoForm
from .models import PerfilUsuario

@login_required
def crear_libro(request):
    perfil = request.user.perfil  
    if request.method == 'POST':
        form_libro = LibroForm(request.POST, request.FILES)
        form_telefono = TelefonoForm(request.POST)
        if form_libro.is_valid() and form_telefono.is_valid():
            libro = form_libro.save(commit=False)
            libro.propietario = request.user
            libro.telefono = form_telefono.cleaned_data['telefono'] 
            libro.save()
            perfil.telefono = form_telefono.cleaned_data['telefono']  
            perfil.save()
            return redirect('libros:lista_libros')  
    else:
        form_libro = LibroForm(initial={'disponible': True})
        form_telefono = TelefonoForm(initial={'telefono': perfil.telefono})  
    return render(request, 'libros/crear_libro.html', {
        'form': form_libro,
        'telefono_form': form_telefono
    })




#editar libro
@login_required
def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk, propietario=request.user)
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libros:lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/editar_libro.html', {'form': form})


from django.core.exceptions import PermissionDenied

@login_required
def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)

    if libro.propietario != request.user and not request.user.is_superuser:
        raise PermissionDenied  # solo propietario o superusuario puede borrar

    if request.method == 'POST':
        libro.delete()
        return redirect('libros:lista_libros')

    return render(request, 'libros/eliminar_libro.html', {'libro': libro})
