from django.shortcuts import render
from .models import*
# Create your views here.

def listar_usuarios(request):
    usuarios = Usuarios.object.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

def listar_animais(request):
    animais = Animais.object.all()
    return render(request, 'animais/lista_animais.html', {'animais': animais})