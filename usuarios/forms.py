from django.forms import ModelForm
from django import forms
from .models import Eventos

class EventosForm(ModelForm):
    class Meta:
        model = Eventos
        fields = ['titulo', 'desc', 'img', 'fecha_evento', 'ubicacion']
        labels = {
            'titulo': '',
            'desc': '',
            'fecha_evento': '',
            'ubicacion': '',
            'img': ''
        }
        widgets = {
            'fecha_evento': forms.TextInput(attrs={'type': 'date'})
        }
        