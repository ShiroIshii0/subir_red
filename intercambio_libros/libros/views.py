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
@login_required
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.propietario = request.user
            libro.save()
            return redirect('libros:lista_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/crear_libro.html', {'form': form})


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


#eliminar libro
@login_required
def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk, propietario=request.user)
    if request.method == 'POST':
        libro.delete()
        return redirect('libros:lista_libros')
    return render(request, 'libros/eliminar_libro.html', {'libro': libro})
