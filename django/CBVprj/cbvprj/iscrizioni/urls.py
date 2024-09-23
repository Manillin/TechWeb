from django.urls import path
from . import views

app_name = "iscrizioni"

urlpatterns = [

    path("listastudenti/", views.ListaStudentiView.as_view(), name="listastudenti"),

    # function view equivalente
    path("listastudentif/", views.lista_studenti_function, name="listastudentif"),

    # esercizio 1
    path("listainsegnamenti/", views.ListaInsegnamentiView.as_view(),
         name="listainsegnamenti"),


    path("insegnamentiattivi/", views.ListaInsegnamentiAttivi.as_view(),
         name="insegnamentiattivi"),
    path("studenticonta/", views.ListaStudentiIscritti.as_view(),
         name="studentiiscritti"),


    # CreateView:
    path("creastudente/", views.CreateStudenteView.as_view(), name="creastudente"),
    path("creainsegnamento/", views.CreateInsegnamentoView.as_view(),
         name="creainsegnamento"),

    # DetailView:
    path("insegnamento/<pk>/",
         views.DetailInsegnamentoView.as_view(), name="insegnamento"),
    # UpdateView:
    path("editinsegnamento/<pk>/",
         views.UpdateInsegnamentoView.as_view(), name="editinsegnamento"),

    path("cancellainsegnamento/<pk>/",
         views.DeleteInsegnamentoView.as_view(), name="cancellainsegnamento"),
    path("cancellastudente/<pk>/",
         views.DeleteStudenteView.as_view(), name="cancellastudente"),

    # Cerca studente by cognome
    path("studente/<str:surname>/",
         views.ListStudenteBySurname.as_view(), name="studente"),

    # esercizio complesso
    path("cercastudente/", views.cerca_studenti, name="cercastudente"),
    path("cercastudente/<str:name>/<str:surname>/",
         views.ListStudenteByNameAndSurname.as_view(), name="studentecercato")

]
