from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import EventosForm
from .models import Eventos

# Create your views here.


def home(request):
    eventos = Eventos.objects.filter()
    return render(request, 'home.html', {
        'eventos': eventos
    })

def registro(request):
    if request.method == "GET":
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                usuario = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                usuario.save()
                login(request, usuario)
                return redirect('home')
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': "El usuario ya existe"
                })
        return render(request, 'registro.html', {
            'form': UserCreationForm,
            'error': "Las contraseñas no coinciden"
        })
        
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'iniciar_sesion.html', {
            'form': AuthenticationForm
        })
    else:
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            return render(request, 'iniciar_sesion.html', {
                'form': AuthenticationForm,
                'error': 'La contraseña es incorrecta'
            })
        else:
            login(request, usuario)
            return redirect('home')


def eventos(request):
    eventos = Eventos.objects.all()
    return render(request, 'eventos.html', {
        'eventos': eventos
    })

def crear_evento(request):
    if request.method == 'GET':
        return render(request, 'crear_evento.html', {
            'form': EventosForm
        })
    else:
        try:
            form = EventosForm(request.POST)
            n_evento = form.save(commit=False)
            n_evento.usuario_id = request.user.id
            n_evento.save()
            return redirect('eventos')
        except:
            return render(request, 'crear_evento.html', {
                'form': EventosForm,
                'error': "Error al crear el evento"
            })