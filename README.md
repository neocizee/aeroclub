# Aeroclub - Sistema de Gestión para Aeroclub
[![Django](https://img.shields.io/badge/Django-5.0+-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Disabled-999999?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)

> **Nota**: Este proyecto tiene sus raíces en **2023**, desarrollado durante el último año de mi **escuela técnica** como respuesta a una solicitud real de un aeroclub local. Aunque el proyecto original quedó descontinuado, hoy se retoma para ser **refactorizado completamente**, aplicando estándares profesionales, arquitectura limpia y contenerización.

---

## 📋 Descripción

**Plataforma Web para la Gestión y Difusión de Actividades de Aeroclub**

Este proyecto "Aeroclub" fue concebido originalmente para digitalizar la presencia y operaciones de una institución aeronáutica real. El objetivo era crear una plataforma que no solo sirviera como sitio web informativo, sino que también ofreciera herramientas de gestión interna.

### 🎯 Historia y Propósito

Este desarrollo representa un puente entre mi formación académica inicial y mi evolución profesional actual:

- **Origen (2023)**: Iniciado durante las Prácticas Profesionalizantes del último año de la Escuela Técnica.
- **Contexto Real**: Surgió de la necesidad de un dueño de aeroclub que solicitó a los alumnos una solución web.
- **Estado Original**: El proyecto quedó descontinuado tras la etapa escolar.
- **Renacimiento (Actualidad)**: Se retoma el código base para transformarlo en un ejemplo de **buenas prácticas, escalabilidad y mantenibilidad**.



## 🏗️ Estado del Proyecto: En Refactorización Profunda 

> **Objetivo Actual:** Modernizar la base de código heredada (legacy) e implementar una arquitectura de software robusta.

Se está trabajando activamente en la integración de un **Django Boilerplate** profesional sobre la base existente.


## ✨ Características (Planificadas / En Migración)

### ✈️ Gestión Institucional
- Información sobre la flota de aeronaves.
- Historia y autoridades del aeroclub.
- Noticias y eventos.

### 📊 Gestión de Socios y Pilotos (Backend)
- Base de datos de socios.
- Registro de horas de vuelo (Bitácora digital).
- Gestión de cuotas y pagos.

### 📅 Reservas y Operaciones
- Sistema de turnos para uso de aeronaves.
- Calendario de instrucción y cursos.


## 🛠️ Stack Tecnológico

### Backend & Core
- **Framework**: Django 5.0+ (En proceso de actualización)
- **Lenguaje**: Python 3.11+
- **Base de Datos**: PostgreSQL (Migrando desde SQLite)

### Frontend
- **Templating**: Django Templates (Base)
- **Estilos**: TailwindCSS / Bootstrap (En revisión para modernización UI/UX)


## 📦 Instalación y Despliegue (En Desarrollo)

*Las instrucciones de instalación se actualizarán una vez completada la integración de un boilerplate profesional y la configuración de Docker para despliegue en producción.*

### Prerrequisitos (Actuales)
- Python 3.11+


## 📊 Estructura del Proyecto (Actual)

```
aeroclub/
├── djangocrud/             # Configuración principal del proyecto (Settings, URLs)
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── usuarios/               # Aplicación principal (Lógica de usuarios y negocio)
│   ├── models.py           # Modelos de datos
│   ├── views.py            # Controladores/Vistas
│   ├── admin.py            # Configuración del admin
│   ├── forms.py            # Formularios
│   ├── templates/          # Plantillas HTML
│   └── static/             # Archivos estáticos de la app
├── theme/                  # Archivos de tema y estilos globales
├── media/                  # Archivos subidos por usuarios
├── manage.py               # Script de gestión de Django
├── db.sqlite3              # Base de datos local
└── venv/                   # Entorno virtual
```

---

## 📝 Licencia

Este proyecto está bajo una **Licencia Propietaria**.
Ver el archivo [LICENSE](LICENSE) para más detalles sobre los términos de uso, distribución y modificaciones permitidas.

---

## 👨‍💻 Autor [@neocizee](https://github.com/neocizee)

*Este proyecto es una demostración de la capacidad de transformar código legacy académico en una solución de software profesional y moderna.*
