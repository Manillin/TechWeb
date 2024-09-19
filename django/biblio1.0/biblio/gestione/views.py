from django.http import HttpResponse
from django.shortcuts import render
from .models import Libro
# Create your views here.


MATTONE_THRESHOLD = 300


def benvenuto(request):
    return HttpResponse("Benvenuto nella gestione!")


def lista_libri(request):
    templ = "gestione/listalibri.html"
    ctx = {
        'tile': 'Lista di Libri',
        'listalibri': Libro.objects.all(),
    }
    return render(request, template_name=templ, context=ctx)


def mattoni(request):
    templ = "gestione/listalibri.html"

    lista_filtrata = Libro.objects.filter(pagine__gte=MATTONE_THRESHOLD)
    # <alternativa:> lista_filtrata = Libro.objects.exlude(pagine__lt = MATTONE_THRESHOLD)

    ctx = {'title': 'Lista Mattoni',
           'listalibri': lista_filtrata}

    return render(request, template_name=templ, context=ctx)


def get_autore(request):
    templ = "gestione/listalibri.html"

    if 'autore' not in request.GET:
        return HttpResponse('Non hai inserito un autore')

    autore = request.GET['autore']
    lista_filtrata = Libro.objects.filter(autore__iexact=autore)

    if len(lista_filtrata) == 0:
        return HttpResponse('Questo autore non ha libri')

    ctx = {'title': f'Lista libri di {autore}',
           'listalibri': lista_filtrata}

    return render(request, template_name=templ, context=ctx)


def autore_param_path(request, autore):
    templ = 'gestione/listalibri.html'

    lista_filtrata = Libro.objects.filter(autore__iexact=autore)
    if len(lista_filtrata) == 0:
        return HttpResponse('Questo autore non ha libri')

    ctx = {'title': f'Lista libri di {autore}',
           'listalibri': lista_filtrata}

    return render(request, template_name=templ, context=ctx)
