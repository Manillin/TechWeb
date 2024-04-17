from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro


def lista_libri(request):
    templ = "gestione/listalibri.html"
    ctx = {'title': "Lista Libri",
           "listalibri": Libro.objects.all()}

    return render(request, template_name=templ, context=ctx)
