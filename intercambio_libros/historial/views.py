from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Historial  # 👈 asegúrate de importar tu modelo Historial

@login_required
def listar_historial(request):
    historial = Historial.objects.filter(usuario=request.user).order_by('-fecha')
    return render(request, 'historial/listar_historial.html', {'historial': historial})