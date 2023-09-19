from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import EventosForm
from .models import Eventos
from django.contrib.auth.decorators import login_required
from django import forms
import os
# Create your views here.


def home(request):
    eventos = Eventos.objects.filter()
    return render(request, 'home.html', {
        'eventos': eventos
    })


def registro(request):
    if request.method == "GET":
        return render(request, 'usuario/registro.html', {
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
                return render(request, 'usuario/registro.html', {
                    'form': UserCreationForm,
                    'error': "El usuario ya existe"
                })
        return render(request, 'usuario/registro.html', {
            'form': UserCreationForm,
            'error': "Las contraseñas no coinciden"
        })

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')


def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'usuario/iniciar_sesion.html', {
            'form': AuthenticationForm
        })
    else:
        usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            return render(request, 'usuario/iniciar_sesion.html', {
                'form': AuthenticationForm,
                'error': 'La contraseña es incorrecta'
            })
        else:
            login(request, usuario)
            return redirect('home')

@login_required
def eventos(request):
    eventos = Eventos.objects.all()
    return render(request, 'eventos/main.html', {
        'eventos': eventos
    })
    
@login_required
def eventos_detail(request, evento_id):
    if request.method == "GET":
        eventos = get_object_or_404(Eventos, pk=evento_id, usuario=request.user)
        form = EventosForm(instance=eventos)
        return render(request, 'eventos/detail.html', {
            'eventos': eventos,
            'form': form
        })
    else:
        try:
            ##Este evento solo se podra actualizar por el usuario que la hizo
            eventos = get_object_or_404(Eventos, pk=evento_id, usuario=request.user)
            form = EventosForm(request.POST, instance=eventos)
            form.save()
            return redirect('eventos')
        except ValueError:
            print(request.POST)
            return render(request, 'eventos/detail.html', {
                'eventos': eventos,
                'form': form,
                'error': "Error actualizando el evento"
            })

@login_required        
def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Eventos, pk=evento_id, usuario=request.user)
    if request.method == "POST":
        evento.delete()
        return redirect('eventos')

@login_required
def crear_evento(request):
    if request.method == 'GET':
        return render(request, 'eventos/crear.html', {
            'form': EventosForm
        })
    else:
        form = EventosForm(request.POST, request.FILES)
        if form.is_valid():
            n_evento = form.save(commit=False)
            n_evento.usuario_id = request.user.id
            n_evento.save()
            return redirect('eventos')

