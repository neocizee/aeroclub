from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Eventos(models.Model):
    titulo = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='imgs_eventos', default='static/assets/logo.png')
    fecha_evento = models.DateTimeField(null=True)
    ubicacion = models.TextField(blank=True)
    
    fecha_carga = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '[ Por ' + self.usuario.username + ' ] - ' + self.titulo
    
class Noticias(models.Model):
    titulo = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='imgs_noticias', default='static/assets/logo.png')
    fecha_carga = models.DateTimeField(auto_now=True)
    fecha_noticia = models.DateField(null=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return '[ Por ' + self.usuario.username + ' ] - ' + self.titulo 