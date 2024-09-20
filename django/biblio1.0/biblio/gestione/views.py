from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Libro
from django.utils import timezone

# Create your views here.


MATTONE_THRESHOLD = 300


def prova(request):
    return HttpResponse('prova <-> prova')


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


def crea_libro(request):

    message = ''

    template = 'gestione/crealibro.html'
    ctx = {
        "title": "Crea Autore",
        "message": message
    }

    if 'autore' in request.GET and 'titolo' in request.GET:
        aut = request.GET['autore']
        tit = request.GET['titolo']
        pag = 100

        try:
            pag = int(request.GET['pagine'])
        except:
            message = 'Pagine non valide, inserimento di pagine di default! (100)'

        l = Libro()
        l.autore = aut
        l.titolo = tit
        l.pagine = pag
        l.data_prestito = timezone.now()

        try:
            l.save()
            message = "Creazione del libro riuscita!" + message
        except Exception as e:
            message = f"Creazione libro fallita [errore: {str(e)}]"

        ctx['message'] = message

    # return render(request, template_name='gestione/crealibro.html',
    #               context={"title": "Crea Autore", "message": message})
    return render(request, template_name=template, context=ctx)


def libro_handler(request, libro_da_modificare: Libro = None):
    msg = ''
    title = 'Elimina Libro'
    templ = 'gestione/modlibro.html'
    ctx = {}

    if libro_da_modificare == None:
        if 'libro' in request.GET:
            s = request.GET['libro']
            s = s[:s.index(':')]
            try:
                l = Libro.objects.get(pk=int(s))
                l.delete()
            except Exception as e:
                msg = "Cancellazione non riuscita: " + str(e)
        ctx = {
            'title': title,
            'listalibri': Libro.objects.all(),
            'message': msg
        }

    else:
        title = 'Modifica Libro'
        print(f'\nstampa parametri dizionario:')
        for key in request.GET:
            print(f'K: {key} -> {request.GET[key]}')

        if 'autore' in request.GET and 'titolo' in request.GET:
            aut = request.GET['autore']
            titl = request.GET['titolo']
            pag = 100
            try:
                pag = int(request.GET['pagine'])
            except:
                msg = 'Pagine invalide, inserimento valore di default (100)'
            libro_da_modificare.autore = aut
            libro_da_modificare.titolo = titl
            libro_da_modificare.pagine = pag

            try:
                libro_da_modificare.save()
                msg = 'Aggiornamento libro riuscito! ' + msg
            except Exception as e:
                msg = f"Errore nella modifica del libro [errore: {e} ]"
        else:
            print("libro fornito da URL")
        ctx = {'title': title, 'libro': libro_da_modificare, 'message': msg}

    return render(request=request, template_name=templ, context=ctx)


def cancella_libro(request):
    return libro_handler(request=request)


def modifica_libro(request, titolo, autore):
    print(f'titolo: {titolo} - autore: {autore}')
    libro = get_object_or_404(Libro, autore=autore, titolo=titolo)
    print(f'Libro ottenuto -> {str(libro)}')

    return libro_handler(request, libro_da_modificare=libro)
