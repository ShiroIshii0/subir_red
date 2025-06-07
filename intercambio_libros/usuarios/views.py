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
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request,usuario)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'usuarios/registrar.html',{'form':form})