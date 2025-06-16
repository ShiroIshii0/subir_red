from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'descripcion', 'portada', 'disponible']
class TelefonoForm(forms.Form):
    telefono = forms.CharField(label="Número de celular", max_length=20)