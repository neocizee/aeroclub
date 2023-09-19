from django.contrib import admin
from .models import Eventos, Noticias

class EventosAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_carga",)
    
class NoticiasAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_carga",)
# Register your models here.
admin.site.register(Eventos, EventosAdmin)
admin.site.register(Noticias, NoticiasAdmin)