from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def benvenuto(request):
    return HttpResponse("Benvenuto nella gestione!")
