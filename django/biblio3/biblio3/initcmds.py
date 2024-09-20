from gestione.models import Libro, Copia
from django.utils import timezone
from datetime import datetime, timedelta
import time
from threading import Timer


def init_db():
    if len(Libro.objects.all()) != 0:
        print("DB già istanziato!\n")
        return

    def func_time(off_year=None, off_month=None, off_day=None):
        if off_year == 0 and off_month == 0 and off_day == 0:
            return None
        tz = timezone.now()
        out = datetime(tz.year-off_year, tz.month-off_month,
                       tz.day-off_day, tz.hour, tz.minute, tz.second)
        return out

    libridict = {
        'autori': ["Alessandro Manzoni", "George Orwell", "Omero", "George Orwell", "Omero"],
        'titoli': ["Promessi Sposi", "1984", "Odissea", "La Fattoria degli Animali", "Illiade"],
        'pagine': [832, 328, 414, 141, 263],
    }

    date = [func_time(y, m, d) for y in range(2)
            for m in range(2) for d in range(2)]

    for i in range(5):
        l = Libro()
        for k in libridict:
            if k == 'autori':
                l.autore = libridict[k][i]
            if k == 'titoli':
                l.titolo = libridict[k][i]
            if k == 'pagine':
                l.pagine = libridict[k][i]
        l.save()
        for d in date:
            c = Copia()
            c.scaduto = False
            c.libro = l
            c.data_prestito = d
            c.save()

    print("Dump DB:\n")
    time.sleep(0.4)
    print(Libro.objects.all())
    print(Copia.objects.all())


def erase_db():
    Libro.objects.all().delete()
    Copia.objects.all().delete()


def controllo_scadenza():
    MAX_PRESTITO_GIORNI = 15
    print("Controllo copie scadute in corso...")
    time.sleep(0.4)

    for l in Libro.objects.all():
        s0 = l.copie.filter(scaduto=False).exclude(data_prestito=None)
        for c in s0:
            dt = datetime(timezone.now().year,
                          timezone.now().month, timezone.now().day).date()
            if (dt - c.data_prestito) > timedelta(days=MAX_PRESTITO_GIORNI):
                c.scaduto = True
                c.save()
                print(c)


def start_controllo_scadenza(check_time_in_seconds):
    Timer(check_time_in_seconds, controllo_scadenza).start()
