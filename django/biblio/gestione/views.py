from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
from django.utils import timezone


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


def get_autore(request):
    templ = "gestione/listalibri.html"
    if 'autore' not in request.GET:
        return HttpResponse("Autore non specificato")
    author = request.GET['autore']
    lista_filtrata = Libro.objects.filter(autore__exact=author)

    ctx = {
        'title': "Lista Mattoni",
        'listalibri': lista_filtrata
    }
    return render(request, template_name=templ, context=ctx)


def autore_path(request, autore):
    templ = "gestione/listalibri.html"
    ctx = {
        'title': f"Libri dell'autore: {autore} ",
        'listalibri': Libro.objects.filter(autore__exact=autore)
    }
    return render(request, template_name=templ, context=ctx)


def crea_libro(request):
    templ = 'gestione/crealibro.html'
    mg = ""
    if 'autore' in request.GET and 'titolo' in request.GET:
        aut = request.GET['autore']
        titl = request.GET['titolo']
        try:
            pag = int(request.GET['pagine'])
        except:
            mg = "Numero di pagine invalido, inserimento pagine di default."
            pag = 100  # default value

        l = Libro()
        l.autore = aut
        l.titolo = titl
        l.pagine = pag
        l.data_prestito = timezone.now()

        try:
            l.save()
            mg = "Libro correttamente salvato nel DB"
        except Exception as e:
            mg = "Errore nell'inserimento del libro dentro il DB " + str(e)
            # mg = f"autore: {aut}, titolo: {titl}, pag: {pag} "
    ctx = {
        'title': 'Crea Libro',
        'message': mg
    }
    return render(request=request, template_name=templ, context=ctx)
