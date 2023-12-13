"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from usuarios import views
from django.conf.urls.static import static 
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registro/',  views.registro, name='registro'),
    path('cerrar_sesion/',  views.cerrar_sesion, name='cerrar_sesion'),
    path('iniciar_sesion/',  views.iniciar_sesion, name='iniciar_sesion'),
    
    path('eventos/',  views.eventos, name='eventos'),
    path('eventos/crear/',  views.crear_evento, name='crear_evento'),
    path('eventos/<int:evento_id>/',  views.eventos_detail, name='eventos_detail'),
    path('eventos/<int:evento_id>/eliminar/',  views.eliminar_evento, name='eliminar_evento'),
    
    path('noticias/',  views.noticias, name='noticias'),
    path('noticias/crear/',  views.crear_noticia, name='crear_noticia'),
    path('noticias/<int:noticia_id>/',  views.noticias_detail, name='noticias_detail'),
    path('noticias/<int:noticia_id>/eliminar/',  views.eliminar_noticia, name='eliminar_noticia'),
    
    path('desarrollando/',  views.desarrollo, name='desarrollo'),
    
    
    path("__reload__/", include("django_browser_reload.urls")),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
