"""
URL configuration for biblio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import *

app_name = 'gestione'

# NOTA: È buona pratica mettere '/' dopo ogni URL per evitare 404 indesiderati!

urlpatterns = [
    path('', benvenuto, name='benvenuto'),
    path('listalibri/', lista_libri, name='listalibri'),
    path('mattoni/', mattoni, name='mattoni'),
    path('autore/', get_autore, name='get_autore'),
    path('autore/<str:autore>/', autore_param_path, name='autorepath'),
    path('crealibro/', crea_libro, name='crealibro'),
    path('cancellalibro/', cancella_libro, name='cancellalibro'),
    path('modificalibro/<str:titolo>/<str:autore>/',
         modifica_libro, name='modificalibro'),
    path('prova/', prova, name='prova')
]
