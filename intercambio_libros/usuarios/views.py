from django.shortcuts import render,redirect


#importando loguat
from django.contrib.auth import logout,login

#importacionde form
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'usuarios/home.html')


def salir(request):
    logout(request)
    return redirect('home')

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.is_superuser = False
            usuario.is_staff = False
            usuario.save()
            # El perfil se crea automáticamente con rol 'usuario' por la señal
            login(request, usuario)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registrar.html', {'form': form})