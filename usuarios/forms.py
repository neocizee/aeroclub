from django.forms import ModelForm
from .models import Eventos

class EventosForm(ModelForm):
    class Meta:
        model = Eventos
        fields = ['titulo', 'desc', 'img', 'fecha_evento']
        