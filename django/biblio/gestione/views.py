from django.shortcuts import render, get_object_or_404
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

    print(f"\nStampa valori dizionario: {list(request.GET.values())} \n")
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


def libro_handler(request, libro_da_modificare: Libro = None):
    msg = ""
    # ctx = {
    #     'title': 'Errore modifica',
    #     'libro': libro_da_modificare,
    #     'message': 'Qualcosa andato storto -> ' + str(libro_da_modificare)
    # }

    title = "Elimina Libro"
    templ = 'gestione/delmodlibro.html'

    if libro_da_modificare == None:
        if 'libro' in request.GET:
            s = request.GET['libro']
            s = s[:s.index('s')]
            try:
                l = Libro.objects.get(pk=int(s))
                l.delete()
            except Exception as E:
                msg = "Cancellazione non riuscita: " + str(E)
        ctx = {
            'title': title,
            'listalibri': Libro.objects.all(),
            'message': msg
        }
    else:
        title = 'Modifica Libro'
        if 'autore' in request.GET and 'titolo' in request.GET:
            aut = request.GET['autore']
            titl = request.GET['titolo']
            pag = 100
            try:
                pag = int(request.GET['pagine'])
            except:
                msg = "Pagine fallback a valore di default"

            libro_da_modificare.autore = aut
            libro_da_modificare.titolo = titl
            libro_da_modificare.pagine = pag

            try:
                libro_da_modificare.save()
                msg = "Aggiornamento Libro riusito! " + "??" + msg
            except Exception as E:
                msg = "Errore nella modifica del libro " + str(E)

            ctx = {
                'title': title,
                'libro': libro_da_modificare,
                'message': msg
            }
    return render(request=request, template_name=templ, context=ctx)


def cancella_libro(request):
    return libro_handler(request=request)


def modifica_libro(request, titolo, autore):
    libro = get_object_or_404(Libro, autore=autore, titolo=titolo)

    print(f"\nStampa valori dizionario: {list(request.GET.values())} \n")

    return libro_handler(request, libro_da_modificare=libro)
