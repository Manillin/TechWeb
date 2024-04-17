from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro


def lista_libri(request):
    templ = "gestione/listalibri.html"
    ctx = {'title': "Lista Libri",
           "listalibri": Libro.objects.all()}

    return render(request, template_name=templ, context=ctx)


MATTONE_THRESHOLD = 300


def mattoni(request):
    templ = "gestione/listalibri.html"
    lista_filtrata = Libro.objects.filter(pagine__gte=MATTONE_THRESHOLD)
    # lista_filtrata = Libro.objects.filter(pagine__lt=MATTONE_THRESHOLD)
    # pagine è attributo e tramite __ si accedono alle operazioni:
    #         pagine__gt -> greater than; pagine__lt -> less than;

    ctx = {
        'title': "Lista Mattoni",
        'listalibri': lista_filtrata
    }
    return render(request, template_name=templ, context=ctx)
